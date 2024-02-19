#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#Petwee is an ORM/ODM module for Google Cloud Datastore/MongoDB, featuring a compatible interface with Peewee.
#Author: cdhigh <http://github.com/cdhigh>
#Repository: <https://github.com/cdhigh/petwee>
#==================================================
import copy, datetime
from collections import defaultdict

try:
    from google.cloud import datastore
    from google.cloud.datastore import Key
    from google.cloud.datastore import query as qr
except ImportError:
    datastore = None

try:
    import pymongo
    from bson.objectid import ObjectId
except ImportError:
    pymongo = None

#from tests.fake_datastore import *

__version__ = '0.1.0'

class DoesNotExist(Exception):
    pass

class NosqlClient(object):
    def bind(self, models):
        for model in models:
            model.bind(self)
    def drop_tables(self, models, **kwargs):
        for model in models:
            self.drop_table(model)
    def create_tables(self, models):
        return True
    def is_closed(self):
        return False
    def connect(self, **kwargs):
        return True
    @classmethod
    def op_map(cls, op):
        return op
    
class DatastoreClient(NosqlClient):
    def __init__(self, project=None, namespace=None, credentials=None, _http=None):
        self.project = project or os.getenv("GOOGLE_CLOUD_PROJECT", None)
        self.credentials = credentials
        self.namespace = namespace
        self._http = _http
        self.client = datastore.Client(project=self.project, namespace=self.namespace, credentials=self.credentials, _http=self._http)
    
    @classmethod
    def db_id_name(cls):
        return "__key__"

    def insert_one(self, model_class, data: dict):
        entity = self.create_entity(data, kind=model_class._meta.name)
        self.client.put(entity)
        return entity.key.to_legacy_urlsafe().decode()

    def insert_many(self, model_class, datas: list):
        ids = []
        kind = model_class._meta.name
        for batch in self.split_batches(datas, 500):
            entities = [self.create_entity(data, kind=kind) for data in batch]
            self.client.put_multi(entities)
            ids.extend([e.key.to_legacy_urlsafe().decode() for e in entities])
        return ids

    def update_one(self, model):
        only_dirty = bool(model._key)
        data = model.dicts(remove_id=True, db_value=True, only_dirty=only_dirty)
        entity = self.create_entity(data, kind=model._meta.name, key=model._key)
        if data:
            self.client.put(entity)
            model.clear_dirty(list(data.keys()))
        return entity.key.to_legacy_urlsafe().decode()
        
    def delete_one(self, model):
        if model._key:
            self.client.delete(model._key)

    def delete_many(self, models):
        keys = [e._key for e in models if e._key]
        if keys:
            self.client.delete_multi(keys)

    def execute(self, queryObj, page_size=500, parent_key=None):
        model_class = queryObj.model_class
        kind = model_class._meta.name
        query = self.get_query(kind, parent_key)
        self.apply_query_condition(queryObj, query)

        limit = queryObj._limit
        batch_size = min(page_size, limit) if limit else page_size
        yield from self.query_fetch(query, batch_size, limit, model_class)

    #count aggregation query
    def count(self, queryObj, parent_key=None):
        count_query = self.get_aggregation_query(queryObj, parent_key).count()
        with count_query.fetch() as query_result:
            return next(query_result).value if query_result else 0

    #sum aggregation query
    def sum(self, queryObj, field, parent_key=None):
        field = field.name if isinstance(field, Field) else field
        sum_query = self.get_aggregation_query(queryObj, parent_key).sum(field)
        with sum_query.fetch() as query_result:
            return next(query_result).value if query_result else 0

    #avg aggregation query
    def avg(self, queryObj, field, parent_key=None):
        field = field.name if isinstance(field, Field) else field
        sum_query = self.get_aggregation_query(queryObj, parent_key).avg(field)
        with sum_query.fetch() as query_result:
            return next(query_result).value if query_result else 0

    #generate model instance(model_class!=None) or entity(model_class=None)
    def query_fetch(self, query, batch_size=500, limit=0, model_class=None):
        cursor = None
        count = 0
        while True:
            last_entity = None
            result = query.fetch(start_cursor=cursor, limit=batch_size)

            for entity in result:
                last_entity = self.make_instance(model_class, entity) if model_class else entity
                yield last_entity
                count += 1
            cursor = result.next_page_token
            if not cursor or (last_entity is None) or (limit and (count >= limit)):
                break

    #make Model instance from database data
    def make_instance(self, model_class, raw):
        key = raw.key
        inst = model_class(_key=key)
        fields = inst._meta.fields
        for field_name, value in raw.items():
            if field_name in fields:
                setattr(inst, field_name, fields[field_name].python_value(value))
            else:
                setattr(inst, field_name, value)
        inst.clear_dirty(list(fields.keys()))
        setattr(inst, inst._meta.primary_key, key.to_legacy_urlsafe().decode())
        return inst

    def get_query(self, kind, parent_key=None):
        return self.client.query(kind=kind, ancestor=parent_key)

    def get_aggregation_query(self, queryObj, parent_key=None):
        kind = queryObj.model_class._meta.name
        query = self.get_query(kind, parent_key)
        self.apply_query_condition(queryObj, query)
        return self.client.aggregation_query(query=query)

    def apply_query_condition(self, queryObj, query):
        #[['name', 'NOT_IN', ['xx', 'yy']], ['age', '>', 28]]
        for ft in queryObj.flat_filters():
            query.add_filter(filter=qr.PropertyFilter(*ft))

        if queryObj._projection:
            query.projection = queryObj._projection
        if queryObj._order:
            query.order = queryObj._order
        if queryObj._distinct:
            query.distinct_on = queryObj._distinct
        return query

    #split a large list into some small list
    def split_batches(self, entities, batch_size):
        return [entities[i:i + batch_size] for i in range(0, len(entities), batch_size)]

    #create datastore entity instance
    def create_entity(self, data: dict, kind=None, key=None, parent_key=None):
        if not key:
            key = self.generate_key(kind, parent_key=parent_key)
        entity = datastore.Entity(key=key)
        entity.update(data)
        return entity

    def atomic(self, **kwargs):
        return self.client.transaction(**kwargs)

    def transaction(self, **kwargs):
        return self.client.transaction(**kwargs)

    def generate_key(self, kind, identifier=None, parent_key=None):
        if identifier:
            return self.client.key(kind, identifier, parent=parent_key)
        else:
            return self.client.key(kind, parent=parent_key)

    def ensure_key(self, key, kind=None):
        if isinstance(key, Key):
            return key
        elif kind and (isinstance(key, int) or key.isdigit()):
            return self.generate_key(kind, int(key))
        else:
            return Key.from_legacy_urlsafe(key)

    def drop_table(self, model):
        kind = model._meta.name if isinstance(model, BaseModel) else model
        query = self.get_query(kind)
        query.projection = ['__key__']
        keys = []
        cursor = None
        while True:
            result = query.fetch(start_cursor=cursor, limit=500)
            keys.extend([entity.key for entity in result])
            cursor = result.next_page_token
            if not cursor:
                break
        if keys:
            self.client.delete_multi(keys)

    def close(self):
        self.client.close()

class MongoDbClient(NosqlClient):
    def __init__(self, project, host=None, port=None, username=None, password=None):
        self.project = project
        self.host = host or 'localhost'
        self.port = port or 27017
        if self.host.startswith('mongodb://'):
            self.client = pymongo.MongoClient(self.host)
        else:
            self.client = pymongo.MongoClient(host=self.host, port=self.port, username=username, password=password)
        self._db = self.client[project]
    
    @classmethod
    def db_id_name(cls):
        return "_id"

    @classmethod
    def op_map(cls, op):
        return {'=': '$eq', '!=': '$ne', '<': '$lt', '>': '$gt', '<=': '$lte',
            '>=': '$gte', 'IN': '$in', 'NOT_IN': '$nin'}.get(op, op)

    #InsertOneResult has inserted_id property
    def insert_one(self, model_class, data: dict):
        id_ = self._db[model_class._meta.name].insert_one(data).inserted_id
        return str(id_)

    #InsertManyResult has inserted_ids property
    def insert_many(self, model_class, datas: list):
        ids = self._db[model_class._meta.name].insert_many(datas).inserted_ids
        return [str(id_) for id_ in ids]
        
    def update_one(self, model):
        id_ = getattr(model, model._meta.primary_key, None)
        if id_: #update
            data = model.dicts(remove_id=True, db_value=True, only_dirty=True)
            if data:
                self._db[model._meta.name].update({'_id': ObjectId(id_)}, {'$set': data})
                model.clear_dirty(list(data.keys()))
            return id_
        else: #insert
            data = model.dicts(remove_id=True, db_value=True)
            model.clear_dirty(list(data.keys()))
            return self.insert_one(model.__class__, data)
     
    def delete_one(self, model):
        if model._id:
            self._db[model._meta.name].delete_one({'_id': model._id})

    def delete_many(self, models):
        for model in models:
            self.delete_one(model)
        
    def execute(self, queryObj, page_size=500, parent_key=None):
        model_class = queryObj.model_class
        collection = self._db[model_class._meta.name]
        sort = [(item[1:], pymongo.DESCENDING) if item.startswith('-') else (item, pymongo.ASCENDING) for item in queryObj._order]
        projection = self.build_projection(queryObj)

        with collection.find(queryObj.filters(), projection=projection) as cursor:
            if sort:
                cursor = cursor.sort(sort)
            if queryObj._limit:
                cursor = cursor.limit(queryObj._limit)
            for item in cursor:
                yield self.make_instance(model_class, item)

    def count(self, queryObj, parent_key=None):
        return self._db[queryObj.model_class._meta.name].count_documents(queryObj.filters())

    #make Model instance from database data
    def make_instance(self, model_class, raw):
        inst = model_class()
        fields = inst._meta.fields
        for field_name, value in raw.items():
            if field_name in fields:
                setattr(inst, field_name, fields[field_name].python_value(value))
            else:
                setattr(inst, field_name, value)
        inst.clear_dirty(list(fields.keys()))
        setattr(inst, inst._meta.primary_key, str(inst._id)) #set primary_key
        return inst

    #make projection dict to fetch some field only
    def build_projection(self, queryObj):
        proj = queryObj._projection
        result = {}
        if proj:
            _meta = queryObj.model_class._meta
            for field_name in _meta.fields.keys():
                if (field_name != _meta.primary_key) and (field_name not in proj):
                    result[field_name] = 0
            return result
        else:
            return None

    def ensure_key(self, key, kind=None):
        if isinstance(key, ObjectId):
            return key
        else:
            return ObjectId(key)

    def atomic(self, **kwargs):
        return self.client.start_session(**kwargs)

    def transaction(self, **kwargs):
        return self.client.start_session(**kwargs)

    def drop_table(self, model):
        model = model._meta.name if isinstance(model, BaseModel) else model
        self._db.drop_collection(model)

    def close(self):
        self.client.close()

class FieldDescriptor(object):
    def __init__(self, field):
        self.field_inst = field
        self.field_name = field.name

    def __get__(self, instance, instance_type=None):
        if instance:
            return instance._data.get(self.field_name)
        return self.field_inst

    def __set__(self, instance, value):
        field_name = self.field_name
        if self.field_inst.enforce_type and not self.field_inst.check_type(value):
            raise ValueError(f'Trying to set a different type of value to "{field_name}"')
        instance._data[field_name] = value
        instance._dirty[field_name] = True

class BaseModel(type):
    inheritable_options = ['client', 'order_by', 'primary_key']

    def __new__(cls, name, bases, attrs):
        if not bases:
            return super(BaseModel, cls).__new__(cls, name, bases, attrs)

        meta_options = {}
        meta = attrs.pop('Meta', None)
        if meta:
            meta_options.update((k, v) for k, v in meta.__dict__.items() if not k.startswith('_'))
            #for compatibilty, app code use the name "database", convert to "client" here
            if 'database' in meta_options:
                client = meta_options.pop('database', None)
                meta_options['client'] = client

        for b in bases:
            base_meta = getattr(b, '_meta', None)
            if not base_meta:
                continue
            
            for (k, v) in base_meta.__dict__.items():
                if k in cls.inheritable_options and k not in meta_options:
                    meta_options[k] = v

            for (k, v) in b.__dict__.items():
                if isinstance(v, FieldDescriptor) and k not in attrs:
                    attrs[k] = copy.deepcopy(v.field_inst)

        meta_options.setdefault('client', None)
        meta_options.setdefault('primary_key', 'id')
        attrs[meta_options['primary_key']] = PrimaryKeyField()

        # initialize the new class and set the magic attributes
        cls = super(BaseModel, cls).__new__(cls, name, bases, attrs)
        cls._meta = ModelOptions(cls, **meta_options)
        cls._data = None
        cls._dirty = None

        # replace the fields with field descriptors, calling the add_to_class hook
        for name, attr in cls.__dict__.items():
            if isinstance(attr, Field):
                attr.add_to_class(cls, name)
        
        cls._meta.prepared()
        return cls

class ModelOptions(object):
    def __init__(self, cls, client=None, order_by=None, primary_key='id', **kwargs):
        self.model_class = cls
        self.name = cls.__name__
        self.fields = {}
        self.defaults = {}
        self.client = client #database here is actually a database client
        self.order_by = order_by
        self.primary_key = primary_key
        
    def prepared(self):
        for field in self.fields.values():
            if field.default is not None:
                self.defaults[field] = field.default

    def get_default_dict(self):
        return self.defaults

#Used for overloading arithmetic operators
def arith_op(op, reverse=False):
    def inner(self, other):
        return UpdateExpr(other, op, self) if reverse else UpdateExpr(self, op, other)
    return inner

#Used for overloading comparison operators
def comp_op(op):
    def inner(self, other):
        return self._generate_filter(op, other)
    return inner

class Field(object):
    def __init__(self, default=None, enforce_type=False, **kwargs):
        self.default = default if callable(default) else lambda: default
        self.enforce_type = enforce_type
    
    def __eq__(self, other):
        return ((other.__class__ == self.__class__) and (other.name == self.name) and 
            (other.model == self.model))

    def __hash__(self):
        return hash((self.model.__name__, self.name))

    def check_type(self, value):
        return True

    def add_to_class(self, klass, name):
        self.name = name
        self.model = klass
        klass._meta.fields[name] = self
        setattr(klass, name, FieldDescriptor(self))

    def db_value(self, value):
        return value

    @classmethod
    def python_value(self, value):
        return value

    __eq__ = comp_op('=')
    __ne__ = comp_op('!=')
    __lt__ = comp_op('<')
    __gt__ = comp_op('>')
    __le__ = comp_op('<=')
    __ge__ = comp_op('>=')
    in_ = comp_op('IN')
    not_in = comp_op('NOT_IN')
    
    def between(self, other1, other2):
        if other1 <= other2:
            return [self._generate_filter(">", other1), self._generate_filter("<", other2)]
        else:
            return [self._generate_filter("<", other1), self._generate_filter(">", other2)]

    def _generate_filter(self, op, other):
        if self.enforce_type and not self.check_type(other):
            raise ValueError("Comparing field {} with '{}' of type {}".format(self.name, other, type(other)))
        return Filter(self.name, op, other)

    def asc(self):
        return self.name
        
    def desc(self):
        return '-{}'.format(self.name)

    __add__ = arith_op('+')
    __sub__ = arith_op('-')
    __mul__ = arith_op('*')
    __truediv__ = arith_op('/')
    __floordiv__ = arith_op('//')
    __mod__ = arith_op('%')
    __pow__ = arith_op('**')
    __lshift__ = arith_op('<<')
    __rshift__ = arith_op('>>')
    __and__ = arith_op('&')
    __or__ = arith_op('|')
    __xor__ = arith_op('^')
    __radd__ = arith_op('+', reverse=True)
    __rsub__ = arith_op('-', reverse=True)
    __rmul__ = arith_op('*', reverse=True)

class PrimaryKeyField(Field):
    def _generate_filter(self, op, other):
        other = self.model._meta.client.ensure_key(other)
        return Filter(self.model._meta.client.db_id_name(), op, other)

class BooleanField(Field):
    pass

class IntegerField(Field):
    def check_type(self, value):
        return isinstance(value, int)

BigIntegerField = IntegerField
SmallIntegerField = IntegerField
BitField = IntegerField
TimestampField = IntegerField
IPField = IntegerField

class FloatField(Field):
    def check_type(self, value):
        return isinstance(value, float)

DoubleField = FloatField
DecimalField = FloatField

class CharField(Field):
    def check_type(self, value):
        return isinstance(value, str)

TextField = CharField
FixedCharField = CharField
UUIDField = CharField

class BlobField(Field):
    pass

class DateTimeField(Field):
    def check_type(self, value):
        return isinstance(value, datetime.datetime)

class DateField(Field):
    def check_type(self, value):
        return isinstance(value, datetime.date)

class TimeField(Field):
    def check_type(self, value):
        return isinstance(value, datetime.time)

class JSONField(Field):
    def check_type(self, value):
        json_types = [bool, int, float, str, list, dict, tuple]
        return any(isinstance(value, json_type) for json_type in json_types)

    @classmethod
    def list_default(cls):
        return []
        
    @classmethod
    def dict_default(cls):
        return {}

class Model(object, metaclass=BaseModel):
    def __init__(self, **kwargs):
        self._key = kwargs.get('_key', None)
        self._data = dict((f.name, v()) for f, v in self._meta.defaults.items())
        self._dirty = {'__key__': True, '_id': True}
        for name, value in kwargs.items():
            setattr(self, name, value)

    @classmethod
    def create(cls, **kwargs):
        inst = cls(**kwargs)
        return inst.save()

    @classmethod
    def select(cls, *args):
        return QueryBuilder(cls, *args)

    @classmethod
    def delete(cls):
        return DeleteQueryBuilder(cls, gatattr(cls, cls._meta.primary_key, None))

    @classmethod
    def update(cls, *args, **kwargs):
        return UpdateQueryBuilder(cls, cls.combine_args_kwargs(*args, **kwargs))

    @classmethod
    def insert(cls, *args, **kwargs):
        return InsertQueryBuilder(cls, cls.combine_args_kwargs(*args, **kwargs))
        
    @classmethod
    def insert_many(cls, datas: list):
        return InsertQueryBuilder(cls, datas)

    @classmethod
    def combine_args_kwargs(cls, *args, **kwargs):
        if (len(args) > 1) or (args and not isinstance(args[0], dict)):
            raise ValueError('The keyword argument have to be a dict')
        args = args[0] if args else {}
        args.update(kwargs)
        return dict(((f.name if isinstance(f, Field) else f), v) for f, v in args.items())
        
    @classmethod
    def get(cls, query=None):
        sq = cls.select()
        if query:
            sq = sq.where(query)
        return sq.get()

    @classmethod
    def get_or_none(cls, query=None):
        try:
            return cls.get(query)
        except DoesNotExist:
            return None

    @classmethod
    def get_by_key(cls, key):
        return cls.select().filter_by_key(key).first()

    @classmethod
    def get_by_id(cls, sid):
        return cls.select().filter_by_id(sid).first()
        
    def save(self, **kwargs):
        id_ = self.client.update_one(self)
        setattr(self, self._meta.primary_key, id_)
        return self

    def delete_instance(self, **kwargs):
        self.client.delete_one(self)

    @property
    def client(self):
        return self._meta.client

    #Convert model into a dict
    #: params only=[Model.title, ...]
    #: params exclude=[Model.title, ...]
    #: remove_id - remove key and id field from dict
    #: db_value - if prepared for saving to db
    #: only_dirty - export items unsaved only
    def dicts(self, **kwargs):
        only = [x.name for x in kwargs.get('only', [])]
        exclude = [x.name for x in kwargs.get('exclude', [])]
        should_skip = lambda n: (n in exclude) or (only and (n not in only))
        db_value = kwargs.get('db_value', False)
        only_dirty = kwargs.get('only_dirty', False)

        data = {}
        for name, field in self._meta.fields.items():
            if not should_skip(name) and (not only_dirty or self._dirty.get(name, False)):
                value = getattr(self, name, None)
                data[name] = field.db_value(value) if db_value else value

        if kwargs.get('remove_id'):
            data.pop('_key', None)
            data.pop('id', None)
            data.pop('_id', None)
        return data

    @classmethod
    def bind(cls, client):
        cls._meta.client = client
        
    @classmethod
    def create_table(cls, **kwargs):
        pass

    @classmethod
    def drop_table(cls, **kwargs):
        self.client.drop_table(cls._meta.name)

    def atomic(self, **kwargs):
        return self.client.transaction(**kwargs)

    def clear_dirty(self, field_name):
        field_name = field_name if isinstance(field_name, list) else [field_name]
        excluded = ['__key__', '_id', self.client.db_id_name()]
        for name in field_name:
            if name not in excluded:
                self._dirty[name] = False

class Filter:
    def __init__(self, item, op, value):
        self.item = item
        self.op = op
        self.value = value

    def __repr__(self):
        return "<Filter: {} {} {}>".format(self.item, self.op, self.value)
    
    def __and__(self, rhs):
        assert(isinstance(rhs, Filter))
        return [self, rhs]

    def __rand__(self, lhs):
        assert(isinstance(lhs, list))
        lhs.append(self)
        return lhs


class QueryBuilder:
    def __init__(self, model_class, *args):
        self.model_class = model_class
        _meta = model_class._meta
        self.kind = _meta.name
        self.client = _meta.client
        self._filters = []
        self._projection = []
        for field in args:
            if isinstance(field, PrimaryKeyField):
                self._projection.append(self.client.db_id_name())
            elif isinstance(field, Field):
                self._projection.append(field.name)
            elif field:
                self._projection.append(field)
        self._order = []
        self._distinct = []
        self._limit = 0

    def where(self, *filters):
        for flt in filters:
            if isinstance(flt, list):
                self._filters.extend(flt)
            else:
                assert(isinstance(flt, Filter))
                self._filters.append(flt)
        return self

    def filter_by_key(self, key):
        if key:
            key = self.client.ensure_key(key, self.kind)
            self._filters.append(Filter(self.client.db_id_name(), "=", key))
        return self

    def filter_by_id(self, id_):
        return self.filter_by_key(id_)

    def order_by(self, *fields):
        self._order.extend([(field.name if isinstance(field, Field) else field) for field in fields])
        return self

    def limit(self, limit: int):
        self._limit = limit
        return self

    def distinct_on(self, field):
        distinct_field = field.name if isinstance(field, Field) else field
        self._distinct = [distinct_field]
        return self

    def execute(self, page_size=500, parent_key=None):
        return self.client.execute(self, page_size=page_size, parent_key=parent_key)
        
    def first(self):
        result = None
        try:
            result = next(self.execute(page_size=1))
        except TypeError:
            pass
        except StopIteration:
            pass
        return result

    def get(self):
        return self.first()

    def count(self):
        return self.client.count(self)

    #convert multiple "!=" to "not in"
    #return a nested dict {item: {op: [value1, value2]}, item: {op: value}}
    def filters(self):
        merged = {}
        for ft in self._filters:
            item, op, value = ft.item, ft.op, ft.value
            merged.setdefault(item, {})
            merged[item].setdefault(op, [])
            merged[item][op].append(value)

        #convert multiple "!=" to "not in"
        val_map = {'>': max, '>=': max, '<': min, '<=': min}
        for item, sub_dict in merged.items():
            for op, value in list(sub_dict.items()):
                new_val = val_map.get(op, lambda x: x[0] if (len(x) == 1) else x)(value)
                new_op = 'NOT_IN' if ((op == '!=') and (len(value) > 1)) else op
                new_op = self.client.op_map(new_op)
                if (new_op != op) or (new_val != value):
                    sub_dict.pop(op, None)
                    if new_op not in sub_dict:
                        sub_dict[new_op] = new_val
                    elif isinstance(sub_dict[new_op], list):
                        sub_dict[new_op].append(new_val)
                    else:
                        sub_dict[new_op] = [sub_dict[new_op], new_val]
        return merged

    #{'name': {'NOT_IN': ['xx', 'yy']}, 'age': {'>': 28}} convert to 
    #[['name', 'NOT_IN', ['xx', 'yy']], ['age', '>', 28]]
    def flat_filters(self):
        merged = self.filters()
        result = []
        for item, sub_dict in merged.items():
            for op, value in sub_dict.items():
                result.append([item, op, value])
        return result

    def __iter__(self):
        return iter(self.execute())

    def __repr__(self):
        return f"<QueryBuilder filters: {self._filters}, ordered by: {self._order}>"

class DeleteQueryBuilder(QueryBuilder):
    def execute(self):
        self.client.delete_many([e for e in super().execute()])

    def __repr__(self):
        return f"<DeleteQueryBuilder filters: {self._filters}>"

class InsertQueryBuilder:
    def __init__(self, model_class, to_insert):
        self.model_class = model_class
        self.client = model_class._meta.client
        self.to_insert = to_insert

    def execute(self):
        if isinstance(self.to_insert, list):
            return self.client.insert_many(self.model_class, self.to_insert)
        elif self.to_insert: #dict
            return self.client.insert_one(self.model_class, self.to_insert)

    def __iter__(self):
        ids = self.execute()
        return iter(ids if isinstance(ids, list) else [ids])

class UpdateQueryBuilder(QueryBuilder):
    def __init__(self, model_class, to_update):
        super().__init__(model_class)
        self._update = to_update #is a dict

    def execute(self):
        for e in super().execute():
            get_field = e._meta.fields.get
            for field_name, value in self._update.items():
                field = get_field(field_name, None)
                if field:
                    if isinstance(value, UpdateExpr):
                        value = eval(str(value))
                    setattr(e, field_name, value)
            self.client.update_one(e)

    def __repr__(self):
        return f"<UpdateQueryBuilder filters: {self._filters}>"

    def __add__(self, other):
        return UpdateExpr(self, other)

class UpdateExpr:
    def __init__(self, inst, op, other):
        self.inst = inst
        self.op = op
        self.other = other

    __add__ = arith_op('+')
    __sub__ = arith_op('-')
    __mul__ = arith_op('*')
    __truediv__ = arith_op('/')
    __floordiv__ = arith_op('//')
    __mod__ = arith_op('%')
    __pow__ = arith_op('**')
    __lshift__ = arith_op('<<')
    __rshift__ = arith_op('>>')
    __and__ = arith_op('&')
    __or__ = arith_op('|')
    __xor__ = arith_op('^')
    __radd__ = arith_op('+', reverse=True)
    __rsub__ = arith_op('-', reverse=True)
    __rmul__ = arith_op('*', reverse=True)

    def __str__(self):
        inst = self.inst
        if isinstance(inst, Field):
            inst = f'e.{inst.name}'
        elif isinstance(inst, str):
            inst = f'"{inst}"'
            
        other = self.other
        if isinstance(other, Field):
            other = f'e.{other.name}'
        elif isinstance(other, str):
            other = f'"{other}"'
        
        return f'({inst} {self.op} {other})'

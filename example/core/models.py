from peewee import CharField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import Model
from peewee import SqliteDatabase

database = SqliteDatabase(":memory:", pragmas={"foreign_keys": 1})


class BaseModel(Model):
    class Meta(object):
        database = database


class Account(BaseModel):
    first_name = CharField(null=False)
    last_name = CharField(null=False)
    age = IntegerField(null=True)


class Picture(BaseModel):
    account_id = ForeignKeyField(Account, backref="pictures")
    image = CharField(unique=True)

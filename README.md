# peewee_seed
peewee_seed is a seed library which provides initial data to database using peewee.
With reference to the [Django fixture](https://docs.djangoproject.com/en/2.1/howto/initial-data/)

[![CircleCI](https://circleci.com/gh/takehaya/peewee_seeds.svg?style=svg)](https://circleci.com/gh/takehaya/peewee_seeds)
[![PyPI version](https://badge.fury.io/py/peewee-seed.svg)](https://badge.fury.io/py/peewee-seed)
## usage

### simple seeds
- file envs
```
/myapp
  __init__.py
  seeds_entry.py
  models.py
  /fixtures
    accounts.yaml
```
``` yaml
# accounts.yaml
- model : myapp.models.Account
  id: 1
  fields:
    first_name: John
    last_name: Smith
    age: 20
```
```python
# models.py
from peewee import CharField
from peewee import IntegerField
from peewee import Model
from peewee import SqliteDatabase

database = SqliteDatabase(":memory:", pragmas={"foregin_keys": 1})


class BaseModel(Model):
    class Meta(object):
        database = database


class Account(BaseModel):
    first_name = CharField(null=False)
    last_name = CharField(null=False)
    age = IntegerField(null=True)
```
- seeds entry file
``` python
# seeds_entry.py
from peewee_seeds import PeeweeSeed
from myapp.models import database


def main():
    path = '/path/to/fixtures'
    
    # seeds instance
    seeds = PeeweeSeed(database, path, ['accounts.yaml'])
    
    # load fixture for create table
    seeds.create_table_all()
    
    # load fixture for db input
    seeds.db_data_input()


if __name__ == '__main__':
    main()
```
- Run command
```
python seeds_entroy.py
```



### other example

```python
from peewee_seed import PeeweeSeed
from myapp.models import database

# seeds instance
seeds = PeeweeSeed()

# set path
seeds.set_path('/path/to/fixtures')

# set use fixture name
seeds.set_fixture_files(['accounts.yaml', 'pictures.yaml'])

# loading fixture file data
fixtures_row_data = seeds.load_fixture_files()

# fixture  purification
fields, models_namelist = seeds.load_fixture(fixtures_row_data[0])

# fixtures purification
fields, models_namelist = seeds.load_fixtures(fixtures_row_data)

# set database session
seeds.set_database(database)

# base on fixtures, create tables
seeds.create_table_all()

# fixtures data to db input
seeds.db_data_input(fixtures_row_data)

# base on fixtures, drop tables 
seeds.drop_table_all()
```

### direct inputdata seed
``` python
# body is dict data
# create & seed
seed = PeeweeSeed(db)
_, models = seed.load_fixtures([body])
seed.create_table_all(models)

seed.db_data_input([body])

# body is modelpath(same to fixtures)
# drop
seed = PeeweeSeed(db)

models = body["models"]
seed.drop_table_all(models)
```

#### error: Foreign key constraint

```python

# seed
seed.db_data_input([body], foreign_key_checks=True)

# db drop
seed.drop_table_all(models, foreign_key_checks=True)


```
# peewee_seed
peewee_seed is a seed library which provides initial data to database using peewee.

## usage

### simple seeds

``` python
from peewee_seeds import PeeweeSeeds
from myapp.models import database


def main():
    path = '/path/to/fixtures'
    
    # seeds instance
    seeds = PeeweeSeeds(database, path, ['accounts.yaml'])
    
    # load fixture for create table
    seeds.create_table_all()
    
    # load fixture for db input
    seeds.db_data_input()


if __name__ == '__main__':
    main()
```

### other example

```python
from peewee_seeds import PeeweeSeeds
from myapp.models import database

# seeds instance
seeds = PeeweeSeeds()

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
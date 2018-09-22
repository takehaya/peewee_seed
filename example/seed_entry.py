import os
from argparse import ArgumentParser

from peewee_seed import PeeweeSeed
from example.core.models import database

# user_setting field
paths = [
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")
]
fixture_files = [
    ['accounts.yaml', 'pictures.yaml']
]

# seeds instance
seed = PeeweeSeed(database)


def peewee_seeds_run(flag_str):
    for path, fixture_file in zip(paths, fixture_files):
        seed.set_path(path)
        seed.set_fixture_files(fixture_file)

        if flag_str == "create":
            seed.create_table_all()
        elif flag_str == "drop":
            seed.drop_table_all()
        elif flag_str == "seed":
            seed.create_table_all()
            seed.db_data_input()


def command_create(args):
    peewee_seeds_run("create")


def command_drop(args):
    peewee_seeds_run("drop")


def command_seed(args):
    peewee_seeds_run("seed")


def get_args():
    parser = ArgumentParser(prog='seeds_entry')
    subparsers = parser.add_subparsers()

    parent_create = subparsers.add_parser('create', help='db table create')
    parent_create.set_defaults(handler=command_create)

    parent_drop = subparsers.add_parser('drop', help='db table drop')
    parent_drop.set_defaults(handler=command_drop)

    parent_seed = subparsers.add_parser('seed', help='db table init data input')
    parent_seed.set_defaults(handler=command_seed)

    args = parser.parse_args()

    return args, parser


def main():
    args, parser = get_args()

    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

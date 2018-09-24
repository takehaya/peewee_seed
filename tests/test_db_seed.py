import os
from unittest import TestCase

from peewee import OperationalError

from peewee_seed import PeeweeSeed
from tests.test_db_model import Account
from tests.test_db_model import Picture
from tests.test_db_model import database


class TestFixtures(TestCase):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")

    # normal test
    def test_set_path(self):
        seed = PeeweeSeed()
        seed.set_path(self.path)

        self.assertEqual(seed.path, self.path)

    def test_set_file(self):
        seed = PeeweeSeed()
        seed.set_fixture_files(["accounts.yaml", "pictures.yaml"])

        self.assertEqual(seed.fixture_files, ["accounts.yaml", "pictures.yaml"])

    def test_load_fixture_file(self):
        seed = PeeweeSeed(database, self.path, ["accounts.yaml"])
        fixtures_row_data = seed.load_fixture_files()
        self.assertTrue(isinstance(fixtures_row_data[0], list))

    def test_load_fixture(self):
        seed = PeeweeSeed(database, self.path, ["accounts.yaml"])
        fixtures_row_data = seed.load_fixture_files()
        fields, modal_namelist = seed.load_fixture(fixtures_row_data[0])
        self.assertEqual(len(fields), 2)
        self.assertEqual(modal_namelist[0], "tests.test_db_model.Account")

    def test_load_fixtures(self):
        seed = PeeweeSeed(database, self.path, ["accounts.yaml", "pictures.yaml"])
        fixtures_row_data = seed.load_fixture_files()
        fields, modal_namelist = seed.load_fixtures(fixtures_row_data)
        self.assertEqual(len(fields), 2)
        self.assertEqual(modal_namelist[0], "tests.test_db_model.Account")
        self.assertEqual(modal_namelist[1], "tests.test_db_model.Picture")

    def test_create_table(self):
        seed = PeeweeSeed(database, self.path, ["accounts.yaml"])
        seed.create_table_all()
        accounts = Account.select()
        self.assertEqual(len(accounts), 0)

    def test_drop_table(self):
        seed = PeeweeSeed(database, self.path, ["accounts.yaml"])
        seed.drop_table_all()
        with self.assertRaises(OperationalError):
            accounts = Account.select()

            # Since it is not called until it refer to a variable....using len
            len(accounts)

    def test_load_input(self):
        seed = PeeweeSeed(database, self.path, ["accounts.yaml", "pictures.yaml"])
        seed.create_table_all()
        seed.db_data_input()
        accounts = Account.select()
        pictures = Picture.select()
        self.assertEqual(len(accounts), 2)
        self.assertEqual(len(pictures), 4)

    # # abnormal test
    # def test_load_fixture_by_wrong_order(self):
    #     pass

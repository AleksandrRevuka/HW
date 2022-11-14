import unittest
from unittest.mock import patch
from io import StringIO

from Homework.HW_19_Test_data.db import DataBase, DataBaseDTO


class TestDataBaseException(unittest.TestCase):
    def setUp(self) -> None:
        self.database_one_dto = DataBaseDTO('postgres', 'user', 'qwertyR1!', '127.0.0.1', '5001')
        self.database_one = DataBase(self.database_one_dto)
        self.table = 'table_12'
        self.data = 'Hello World'
        self.exc_type = 'str'
        self.exc_val = '200'
        self.exc_tb = 'table_1'

    def tearDown(self) -> None:
        del self.database_one

    def test__del__(self):
        self.database_one.__del__()
        self.assertEqual(self.database_one.instance(), None)

    def test__enter__(self):
        self.assertEqual(self.database_one.__enter__(), self.database_one)

    def test__exit__(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.database_one.__exit__(self.exc_type, self.exc_val, self.exc_tb)
            self.assertTrue(f'Close connect to DB: {self.database_one.db_name}' in fake_out.getvalue())

    def test_action_print(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.database_one.connect()
            self.assertTrue(f'Connect to DB: {self.database_one.db_name}' in fake_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.database_one.close()
            self.assertTrue(f'Close connect to DB: {self.database_one.db_name}' in fake_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.database_one.read(self.table)
            self.assertTrue(f'Read data from database: {self.database_one.db_name} from table: {self.table}'
                            in fake_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.database_one.write(self.table, self.data)
            self.assertTrue(f'Write {self.data} to DB: {self.database_one.db_name} table: {self.table}'
                            in fake_out.getvalue())

    def test_normal_data(self):
        self.assertEqual(self.database_one.db_name, self.database_one_dto.db_name)
        self.assertEqual(self.database_one.user, self.database_one_dto.user)
        self.assertEqual(self.database_one.password, self.database_one_dto.password)
        self.assertEqual(self.database_one.host, self.database_one_dto.host)
        self.assertEqual(self.database_one.port, self.database_one_dto.port)

    def test_set_values(self):
        self.database_one.db_name = 'mysql'
        self.database_one.user = 'user_1'
        self.database_one.password = 'Admin_#1'
        self.database_one.host = '8.8.8.8'
        self.database_one.port = '12111'

        self.assertEqual(self.database_one.db_name, 'mysql')
        self.assertEqual(self.database_one.user, 'user_1')
        self.assertEqual(self.database_one.password, 'Admin_#1')
        self.assertEqual(self.database_one.host, '8.8.8.8')
        self.assertEqual(self.database_one.port, '12111')

        self.reset_database()

    def test_with_wrong_database(self):

    def reset_database(self):
        self.person = DataBase(self.database_one_dto)

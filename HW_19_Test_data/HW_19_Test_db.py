import unittest
from unittest.mock import patch
import io

from Homework.HW_19_Test_data.db import DataBase, DataBaseDTO, DataBaseException


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

    def test_delete_database_instance(self):
        self.database_one.__del__()
        self.assertEqual(DataBase.instance(), None)

    def test_singleton_database_pattern(self):
        data_mysql = DataBaseDTO('mysql', 'user', 'qwertyR1!', '127.0.0.1', '5001')
        data_postgres = DataBaseDTO('postgres', 'user', 'qwertyR1!', '127.0.0.1', '5001')

        database_mysql = DataBase(data_mysql)
        database_postgres = DataBase(data_postgres)

        self.assertEqual(id(database_mysql), id(database_postgres))

    def test_connect(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.database_one.connect()
            self.assertTrue(f'Connect to DB: {self.database_one.db_name}' in fake_out.getvalue())

    def test_close_connect(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.database_one.close()
            self.assertTrue(f'Close connect to DB: {self.database_one.db_name}' in fake_out.getvalue())

    def test_read_data(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.database_one.read(self.table)
            self.assertTrue(f'Read data from database: {self.database_one.db_name} from table: {self.table}'
                            in fake_out.getvalue())

    def test_write(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
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

    def test_with_wrong_db_name(self):
        with self.assertRaises(TypeError) as context_not_string:
            self.database_one.db_name = 23456
        self.assertTrue(f'{23456} must be a string' in str(context_not_string.exception))

        with self.assertRaises(ValueError) as context_not_value:
            self.database_one.db_name = ' '
        self.assertTrue('Empty string in values' in str(context_not_value.exception))

        with self.assertRaises(DataBaseException) as context_wrong_value:
            self.database_one.db_name = 'wrong'
        self.assertTrue(f'Unsupported DB: {"wrong"}. Use these names: {self.database_one.databases}'
                        in str(context_wrong_value.exception))

    def test_with_wrong_user(self):
        with self.assertWarns(UserWarning) as context_user_root:
            self.database_one.user = 'root'
        self.assertTrue("Use root user is dangerous" in str(context_user_root.warning))

    def test_with_wrong_password(self):
        with self.assertRaises(DataBaseException) as context_wrong_password:
            passwords = ['Admin#1', 'Admin_#one', 'admin_#1', 'ADMIN_#1', 'Adminnuber1']
            for password in passwords:
                self.database_one.password = password
        self.assertTrue('Password must be at least 8 chars include Upper, Lower, Digit, Punctuation'
                        in str(context_wrong_password.exception))

    def test_with_wrong_host(self):
        with self.assertRaises(DataBaseException) as context_wrong_host:
            self.database_one.host = '127.0.0.876'
        self.assertTrue("\'127.0.0.876\' does not appear to be an IPv4 or IPv6 address"
                        in str(context_wrong_host.exception))

        with self.assertRaises(DataBaseException) as context_not_available_host:
            self.database_one.host = '192.168.88.99'
        self.assertTrue("192.168.88.99 is not available" in str(context_not_available_host.exception))

    def test_with_wrong_port(self):
        with self.assertRaises(DataBaseException) as context_wrong_port:
            self.database_one.port = 'number_port'
        self.assertEqual('Port must contains numbers not number_port', str(context_wrong_port.exception))

        with self.assertRaises(DataBaseException) as context_negative_port:
            self.database_one.port = '0'
        self.assertEqual(f'Port must be between 0-65000', str(context_negative_port.exception))

        with self.assertRaises(DataBaseException) as context_max_port:
            self.database_one.port = '66000'
        self.assertEqual(f'Port must be between 0-65000', str(context_max_port.exception))

    def test_database_context(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with DataBase(self.database_one_dto) as db:
                db.write('Owner', 'Some data')
            self.assertEqual(fake_out.getvalue(), 'Connect to DB: postgres\n'
                                                  'Write Some data to DB: postgres table: Owner\n'
                                                  'Close connect to DB: postgres\n')

    def reset_database(self):
        self.person = DataBase(self.database_one_dto)

import pytest
from unittest.mock import patch
import io

from Homework.HW_19_Test_data.db import DataBase, DataBaseDTO, DataBaseException


# def test_delete_database_instance():
#     database_one.__del__()
#     assert DataBase.instance is None


def test_singleton_database_pattern():
    data_mysql = DataBaseDTO('mysql', 'user', 'qwertyR1!', '127.0.0.1', '5001')
    data_postgres = DataBaseDTO('postgres', 'user', 'qwertyR1!', '127.0.0.1', '5001')
    database_mysql = DataBase(data_mysql)
    database_postgres = DataBase(data_postgres)
    assert id(database_mysql) == id(database_postgres)


def test_connect():
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        database_one.connect()
    assert f'Connect to DB: {database_one.db_name}' in fake_out.getvalue()


def test_close_connect():
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        database_one.close()
    assert f'Close connect to DB: {database_one.db_name}' in fake_out.getvalue()


def test_read_data():
    table = 'table_12'
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        database_one.read(table)
    assert f'Read data from database: {database_one.db_name} from table: {table}' in fake_out.getvalue()


def test_write():
    table = 'table_12'
    data = 'Hello World'
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        database_one.write(table, data)
    assert f'Write {data} to DB: {database_one.db_name} table: {table}' in fake_out.getvalue()


def test_normal_data():
    assert database_one.db_name == database_one_dto.db_name
    assert database_one.user == database_one_dto.user
    assert database_one.password == database_one_dto.password
    assert database_one.host == database_one_dto.host
    assert database_one.port == database_one_dto.port


def test_set_values():
    database_one.db_name = 'mysql'
    database_one.user = 'user_1'
    database_one.password = 'Admin_#1'
    database_one.host = '8.8.8.8'
    database_one.port = '12111'

    assert database_one.db_name == 'mysql'
    assert database_one.user == 'user_1'
    assert database_one.password == 'Admin_#1'
    assert database_one.host == '8.8.8.8'
    assert database_one.port == '12111'
    reset_database()


def test_with_wrong_db_name():
    with pytest.raises(TypeError) as context_not_string:
        database_one.db_name = 23456
    assert f'{23456} must be a string' in str(context_not_string.value)

    with pytest.raises(ValueError) as context_not_value:
        database_one.db_name = ' '
    assert 'Empty string in values' in str(context_not_value.value)

    with pytest.raises(DataBaseException) as context_wrong_value:
        database_one.db_name = 'wrong'
    assert f'Unsupported DB: {"wrong"}. Use these names: {database_one.databases}' \
           in str(context_wrong_value.value)


def test_with_wrong_user():
    with pytest.warns(Warning, match="Use root user is dangerous"):
        database_one.user = 'root'


def test_with_wrong_password():
    with pytest.raises(DataBaseException) as context_wrong_password:
        passwords = ['Admin#1', 'Admin_#one', 'admin_#1', 'ADMIN_#1', 'Adminnuber1']
        for password in passwords:
            database_one.password = password
    assert 'Password must be at least 8 chars include Upper, Lower, Digit, Punctuation' \
           in str(context_wrong_password.value)


def test_with_wrong_host():
    with pytest.raises(DataBaseException) as context_wrong_host:
        database_one.host = '127.0.0.876'
    assert "\'127.0.0.876\' does not appear to be an IPv4 or IPv6 address" in str(context_wrong_host.value)

    with pytest.raises(DataBaseException) as context_not_available_host:
        database_one.host = '192.168.88.99'
    assert "192.168.88.99 is not available" in str(context_not_available_host.value)


def test_with_wrong_port():
    with pytest.raises(DataBaseException) as context_wrong_port:
        database_one.port = 'number_port'
    assert 'Port must contains numbers not number_port' == str(context_wrong_port.value)

    with pytest.raises(DataBaseException) as context_negative_port:
        database_one.port = '0'
    assert f'Port must be between 0-65000' == str(context_negative_port.value)

    with pytest.raises(DataBaseException) as context_max_port:
        database_one.port = '66000'
    assert f'Port must be between 0-65000' == str(context_max_port.value)


def test_database_context():
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        with DataBase(database_one_dto) as db:
            db.write('Owner', 'Some data')
        assert fake_out.getvalue() in 'Connect to DB: postgres\n'\
                                      'Write Some data to DB: postgres table: Owner\n'\
                                      'Close connect to DB: postgres\n'


def reset_database():
    person = DataBase(database_one_dto)
    return person


if __name__ == '__main__':
    database_one_dto = DataBaseDTO('postgres', 'user', 'qwertyR1!', '127.0.0.1', '5001')
    database_one = DataBase(database_one_dto)
    pytest.main()

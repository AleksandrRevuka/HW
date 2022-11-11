"""Tests class Person"""
import unittest
from typing import NamedTuple
from Homework.HW_18_Test_person.person import Person


class PersonData(NamedTuple):
    full_name: str
    age: int
    id_card: str
    weight: float


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        person_data = PersonData('Иванов Иван Иванович', 30, 'AA-123456', 100.0)
        self.person = Person(person_data)

    def tearDown(self) -> None:
        del self.person

    def test_full_name(self):
        self.assertEqual(self.person.full_name, 'Иванов Иван Иванович')

    def test_set_full_name(self):
        self.person.full_name = 'Петров Петр Петрович'
        self.assertEqual(self.person.full_name, 'Петров Петр Петрович')

    def test_verify_full_name(self):
        with self.assertRaises(TypeError) as error:
            self.person.full_name = 12
        self.assertEqual('Full name must be a string', error.exception.args[0])

        with self.assertRaises(TypeError) as error:
            self.person.full_name = ' '
        self.assertEqual('Full name must contain at least one character', error.exception.args[0])

        with self.assertRaises(TypeError) as error:
            self.person.full_name = 'Юлия Сергеевна'
        self.assertEqual('Invalid name format', error.exception.args[0])

        with self.assertRaises(TypeError) as error:
            self.person.full_name = '_ Юлия Сергеевна'
        self.assertEqual('Full name can only contain letter', error.exception.args[0])

    def test_age(self):
        self.assertEqual(self.person.age, 30)

    def test_set_age(self):
        self.person.age = 40
        self.assertEqual(self.person.age, 40)

    def test_verify_age(self):
        with self.assertRaises(TypeError) as error:
            self.person.age = 99.0
        self.assertEqual('Age must be an integer', error.exception.args[0])

        with self.assertRaises(ValueError)as error:
            self.person.age = 10
        self.assertEqual('Age must be between 16 and 65', error.exception.args[0])

    def test_id_card(self):
        self.assertEqual(self.person.id_card, 'AA-123456')

    def test_set_id_card(self):
        self.person.id_card = 'ZZ-654321'
        self.assertEqual(self.person.id_card, 'ZZ-654321')

    def test_verify_id_card(self):
        with self.assertRaises(TypeError) as error:
            self.person.id_card = 12
        self.assertEqual('Invalid data type for card id', error.exception.args[0])

        with self.assertRaises(ValueError) as error:
            self.person.id_card = 'KK654321'
        self.assertEqual('Invalid card id data format XX-XXXXXX', error.exception.args[0])

    def test_weight(self):
        self.assertEqual(self.person.weight, 100.0)

    def test_set_weight(self):
        self.person.weight = 90.0
        self.assertEqual(self.person.weight, 90.0)

    def test_verify_weight(self):
        with self.assertRaises(TypeError)as error:
            self.person.weight = 65
        self.assertEqual('Weight must be an float number', error.exception.args[0])

        with self.assertRaises(ValueError) as error:
            self.person.weight = 150.0
        self.assertEqual('Weight should be between 50 and 119', error.exception.args[0])

    def test__str__(self):
        self.assertEqual(self.person.__str__(), 'Иванов Иван Иванович')


if __name__ == '__main__':
    unittest.main()

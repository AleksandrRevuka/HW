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
        self.assertEqual(self.person.full_name(), 'Иванов Иван Иванович')

    def test_set_full_name(self):
        self.assertEqual(self.person.full_name())

if __name__ == '__main__':
    unittest.main()
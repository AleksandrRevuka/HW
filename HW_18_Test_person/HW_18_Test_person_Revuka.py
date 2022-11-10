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
        self.assertEqual(self.person.full_name('Петров Петр Петрович'), 'Петров Петр Петрович')

    def test_age(self):
        self.assertEqual(self.person.age, 30)

    def test_set_age(self):
        self.assertEqual(self.person.age(40), 40)

    def test_id_card(self):
        self.assertEqual(self.person.id_card, 'AA-123456')

    def test_set_id_card(self):
        self.assertEqual(self.person.id_card('ZZ-654321'), '')
        self.assertEqual(self.person.id_card, 'ZZ-65432')

    def test_weight(self):
        self.assertEqual(self.person.weight, 100.00)

    def test_set_weight(self):
        self.assertEqual(self.person.weight(90.00), 90.00)


if __name__ == '__main__':
    unittest.main()

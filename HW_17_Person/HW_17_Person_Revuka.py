"""Processing of customer data"""
from typing import NamedTuple
from prettytable import PrettyTable


class Person(NamedTuple):
    """Type class for person"""
    number_person: int
    first_name: str
    last_name: str
    patronymic_name: str
    age: int
    id: str
    weight: float


class PrintPersons:
    def __init__(self, persons):
        self.persons = persons
        self.persons_table = PrettyTable()
        self.persons_table.field_names = ["Humber person", "First name", "Last name",
                                          "Patronymic Name", "Age", "ID", "Weight"]

    def print(self):
        for person in self.persons:
            self.persons_table.add_row([person.number_person, person.first_name, person.last_name,
                                        person.patronymic_name, person.age, person.id, person.weight])
        print(self.persons_table)


def main():
    persons = []
    person_0 = Person(0, "Aleksandr", "Revuka", "Nikolaevich", 37, "GA-123456", 79.3)
    person_1 = Person(1, "Aleksandr", "Revuka", "Nikolaevich", 35, "GA-123456", 89.3)
    persons.append(person_0)
    persons.append(person_1)
    print_table = PrintPersons(persons)
    PrintPersons.print(print_table)


if __name__ == '__main__':
    main()

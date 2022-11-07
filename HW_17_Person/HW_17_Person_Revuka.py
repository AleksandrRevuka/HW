"""Processing of customer data"""
from typing import NamedTuple
from prettytable import PrettyTable
import os


class PersonTable(NamedTuple):
    """Type class for person"""
    number_person: int
    first_name: str
    last_name: str
    patronymic_name: str
    age: int
    id: str
    weight: float


class PrintPersons:
    """Print persons"""
    def __init__(self, persons, person):
        self.person = person
        self.persons = persons
        self.persons_table = PrettyTable()
        self.persons_table.field_names = ["Humber person", "First name", "Last name",
                                          "Patronymic Name", "Age", "ID", "Weight"]

    def print_persons(self):
        for person in self.persons:
            self.persons_table.add_row([person.number_person, person.first_name, person.last_name,
                                        person.patronymic_name, person.age, person.id, person.weight])
        print(self.persons_table)

    def print_person(self):
        self.persons_table.add_row([self.persons[self.person].number_person, self.persons[self.person].first_name,
                                    self.persons[self.person].last_name, self.persons[self.person].patronymic_name,
                                    self.persons[self.person].age, self.persons[self.person].id,
                                    self.persons[self.person].weight])
        print(self.persons_table)


def check_exist_type_file(filename: str):
    """Check FileNotFoundError, UnicodeDecodeError exceptions"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text format'
    return False


def read_and_make_data_persons(data_file):
    """Read and make data persons"""
    with open(data_file, encoding="utf-8") as file:
        data_persons = []
        for line in file:
            parameters = line.split(' ')
            number_person, first_name, last_name, patronymic_name, age, id_pas, weight = \
                int(parameters[0]), parameters[1], parameters[2], parameters[3], int(parameters[4]), \
                parameters[5], float(parameters[6])
            person = PersonTable(number_person, first_name, last_name, patronymic_name, age, id_pas, weight)
            data_persons.append(person)
    return data_persons


def main(data_persons_file):
    """Main controller"""
    check_exist_type_file(data_persons_file)
    data_persons = read_and_make_data_persons(data_persons_file)
    e = PrintPersons(data_persons, 0)
    PrintPersons.print_persons(e)


if __name__ == '__main__':
    current_dir = os.getcwd()
    data = os.path.join(current_dir, 'data_persons.txt')
    main(data)

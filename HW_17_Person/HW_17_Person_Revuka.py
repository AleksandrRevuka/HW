"""Processing of customer data"""
from typing import NamedTuple
from prettytable import PrettyTable
import os
import re


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


class Person:
    def __init__(self, number_person, first_name, last_name, patronymic_name, age, id_pas, weight):
        self._number_person = number_person
        self._first_name = first_name
        self._last_name = last_name
        self._patronymic_name = patronymic_name
        self._age = age
        self._id_pas = id_pas
        self._weight = weight

    @property
    def number_person(self):
        return self._number_person

    @number_person.setter
    def number_person(self, number_person):
        if int:
            self._number_person = number_person
            print(f'Successfully changed to: {number_person}')
        else:
            print(f'{number_person} Invalid number, try again!')

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if re.findall(r'()', first_name):
            self._first_name = first_name
            print(f'Successfully changed to: {first_name}')
        else:
            print(f'{first_name} Invalid first name, try again!')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 16 < age < 66:
            self._age = age
            print(f'Successfully changed to: {age}')
        else:
            print(f'{age} Invalid age, try again!')

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if 40 < float(weight) < 130:
            self._weight = weight
            print(f'Successfully changed to: {weight}')
        else:
            print(f'{weight} Invalid weight, try again!')


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

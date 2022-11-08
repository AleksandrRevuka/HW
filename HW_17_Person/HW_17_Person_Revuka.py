"""Processing of customer data"""
from typing import NamedTuple
from prettytable import PrettyTable
import os
import re


class PersonTable(NamedTuple):
    """Type class for person"""
    full_name: str
    age: int | str
    id: str
    weight: float | str


class PrintPersons:
    """Print persons"""
    def __init__(self, persons, person):
        self.person = person
        self.persons = persons
        self.persons_table = PrettyTable()
        self.persons_table.field_names = ["Full name", "Age", "ID", "Weight"]

    def print_persons(self):
        for person in self.persons:
            self.persons_table.add_row([person.full_name, person.age, person.id, person.weight])
        print(self.persons_table)

    def print_person(self):
        self.persons_table.add_row([self.persons[self.person].full_name,
                                    self.persons[self.person].age, self.persons[self.person].id,
                                    self.persons[self.person].weight])
        print(self.persons_table)


class Person:
    def __init__(self, full_name, age, id_pas, weight):
        self.__full_name = full_name
        self.__age = age
        self.__id_pas = id_pas
        self.__weight = weight

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        if re.findall(r'(^[аА-яЯ]{2,15})\s([аА-яЯ]{2,15})\s([аА-яЯ]{2,15})$', full_name):
            self.__full_name = full_name
            print(f'Successfully changed full name to: {full_name}')
        else:
            print(f'Invalid full name: {full_name}, try again!')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age.isdigit() and 16 < int(age) < 66:
            self.__age = age
            print(f'Successfully changed age to: {age}')
        else:
            print(f'Invalid age: {age}, try again!')

    @property
    def id_pass(self):
        return self.__id_pas

    @id_pass.setter
    def id_pass(self, id_pas):
        if re.findall(r'^[A-Z-]{2}[0-9]{6}$', id_pas):
            self.__id_pas = id_pas
            print(f'Successfully changed ID to: {id_pas}')
        else:
            print(f'Invalid ID: {id_pas}, try again!')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight.isdigit() and 40 < float(weight) < 130:
            self.__weight = weight
            print(f'Successfully changed weight to: {weight}')
        else:
            print(f'Invalid weight: {weight}, try again!')

    def print_info(self):
        print(f'ФИО: {self.__full_name} Возраст: {self.__age} '
              f'Паспорт: {self.__id_pas} Вес: {self.__weight}')
        person = PersonTable(self.__full_name, self.__age, self.__id_pas, self.__weight)
        return person


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
            full_name = re.findall(r'^([аА-яЯ]{2,15})\s([аА-яЯ]{2,15})\s([аА-яЯ]{2,15})', line)
            age = re.findall(r'[0-9]{2}', line)
            id_pas = re.findall(r'[A-Z]{2}-[0-9]{6}', line)
            weight = re.findall(r'[0-9]{2}.[0-9]{1,2}$', line)
            if not all((full_name, age, id_pas, weight)):
                raise ValueError('Wrong data in data_persons.txt')
            full_name = full_name.pop()
            age = age.pop()
            id_pas = id_pas.pop()
            weight = weight.pop()
            person = PersonTable(full_name, age, id_pas, weight)
            data_persons.append(person)
    return data_persons


def main(data_persons_file):
    """Main controller"""
    check_exist_type_file(data_persons_file)
    data_persons = read_and_make_data_persons(data_persons_file)
    e = PrintPersons(data_persons, 0)
    PrintPersons.print_persons(e)
    full_name = 'Иванов Иван Ивановичь'
    age = '100'
    id_pas = 'AA-111111'
    weight = '99.99'
    person_1 = Person(full_name, age, id_pas, weight)
    person_1.print_info()
    person_1.full_name = 'Белюга Татьяна Сергеевна'
    person_1.age = '44'
    person_1.id_pass = "FF-999999"
    person_1.weight = '111'
    person_1.print_info()


if __name__ == '__main__':
    current_dir = os.getcwd()
    data = os.path.join(current_dir, 'data_persons.txt')
    main(data)

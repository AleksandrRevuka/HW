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
        if re.findall(r'^[A-Z]{2}-[0-9]{6}$', id_pas):
            self.__id_pas = id_pas
            print(f'Successfully changed ID to: {id_pas}')
        else:
            print(f'Invalid ID: {id_pas}, try again!')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight.replace('.', '', 1).isdigit() and 40 <= float(weight) <= 130:
            self.__weight = weight
            print(f'Successfully changed weight to: {weight}')
        else:
            print(f'Invalid weight: {weight}, try again!')

    def print_info(self):
        print(f'ФИО: {self.__full_name} Возраст: {self.__age} '
              f'Паспорт: {self.__id_pas} Вес: {self.__weight}')

    def data_person(self):
        person = self.__full_name + ' ' + self.__age + ' ' + self.__id_pas + ' ' + self.__weight
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
            f_name = ''
            for name in full_name:
                f_name += name + ' '
            age = age.pop()
            id_pas = id_pas.pop()
            weight = weight.pop()
            person = PersonTable(f_name, age, id_pas, weight)
            data_persons.append(person)
    return data_persons


def add_person_to_datafile(data_persons_file, person):
    with open(data_persons_file, 'a', encoding="utf-8") as file:
        file.write('\n')
        file.write(person)


def main_menu(data_persons_file):
    """Main controller"""
    while True:
        user_choice = input('What do you want? add new person (a) or print all person (p), exit (e):')
        if user_choice == 'a':
            person = Person("", "", "", "")
            person.full_name = input('Full name, for example "Иванов Иван Ивановичь": ')
            person.age = input('Age person, for example "45": ')
            person.id_pass = input('ID passport, for example "AA-111111": ')
            person.weight = input('Weight person (kg), for example "99.99": ')
            person.print_info()
            while True:
                user_choice = input("Add new person to datafile? or change (y/c) or go to up (enter): ")
                if user_choice == 'y':
                    add_person_to_datafile(data_persons_file, person.data_person())
                    print('New person added successfully')
                if user_choice == 'c':
                    while True:
                        user_choice = input('Change Full name (f), Age (a), ID (i), Weigh (w), '
                                            'Print (p), Add to datafile (s), exit (e): ')
                        if user_choice == 'f':
                            print(f'Now full name: {person.full_name}\n')
                            person.full_name = input('Full name, for example "Иванов Иван Ивановичь": ')
                            continue
                        if user_choice == 'a':
                            print(f'Now age: {person.age}\n')
                            person.age = input('Age person, for example "45": ')
                            continue
                        if user_choice == 'i':
                            print(f'Now ID passport: {person.id_pass}\n')
                            person.id_pass = input('ID passport, for example "AA-111111": ')
                            continue
                        if user_choice == 'w':
                            print(f'Now weight: {person.weight}\n')
                            person.weight = input('Weight person (kg), for example "99.99": ')
                            continue
                        if user_choice == 'p':
                            person.print_info()
                            continue
                        if user_choice == 's':
                            add_person_to_datafile(data_persons_file, person.data_person())
                            print('New person added successfully')
                        if user_choice == 'e':
                            exit(print('Goodbye'))
                        else:
                            break
                if user_choice == '':
                    main_menu(data_persons_file)
                else:
                    break
        if user_choice == 'p':
            check_exist_type_file(data_persons_file)
            data_persons = read_and_make_data_persons(data_persons_file)
            person_table = PrintPersons(data_persons, 0)
            PrintPersons.print_persons(person_table)
            continue
        if user_choice == 'e':
            exit(print('Goodbye my friend'))
        else:
            continue


if __name__ == '__main__':
    current_dir = os.getcwd()
    data = os.path.join(current_dir, 'data_persons.txt')
    main_menu(data)

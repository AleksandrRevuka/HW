# Написати функцію, яка сортує список із оцінками на основі англійської системи.
# Усього 5 символів, у порядку спадання: A, B, C, D, F.
#
# Приклади:
#
# sort_grades(['A', 'B', 'C', 'C', 'F', 'A')) -> ['F', 'C', 'C', 'B', 'A' , 'A']
# sort_grades(['b', 'c', 'C', 'f', 'A')) -> ['F', 'C', 'C', 'B', 'A']
# sort_grades([]) -> []


def make_upper_grades(data):
    for grade in enter_grades:
        sort_grades.append(grade.upper())


def normal_sort_grades(data):
    sort_grades.sort()


def reverse_sort_grades(data):
    sort_grades.reverse()


def chek_grades(data):
    i = 0
    while i < number_of_inputs:
        enter_grades.append(input())
        if enter_grades[i] not in GRADES:
            print('It is not grade, try again')
            del enter_grades[-1]
        else:
            i += 1


GRADES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
sort_grades = []
enter_grades = []


while True:
    number_of_inputs = input('How many grades do you want to enter:')
    if number_of_inputs.isnumeric():
        number_of_inputs = int(number_of_inputs)
        break
    else:
        print('It is not number, try again')

chek_grades(number_of_inputs)

make_upper_grades(enter_grades)

normal_sort_grades(sort_grades)
print(sort_grades)

reverse_sort_grades(sort_grades)
print(sort_grades)

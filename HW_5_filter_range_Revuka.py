# Число 89 є першим цілим числом з більш ніж однією цифрою, яке відповідає властивості
# Тому що ця сума дає те саме число.
# Фактично: 89 = 8^1 + 9^2
#
# Наступним числом, що володіє цією властивістю, є 135.
#
# Перегляньте цю властивість ще раз: 135 = 1^1 + 3^2 + 5^3
#
# Нам потрібна функція для збору цих чисел, яка може отримати два цілих числа a, b, які визначають діапазон [a, b]
# (включно) і виводять список відсортованих чисел у діапазоні, який відповідає властивості, описаній вище.
#
# Давайте розглянемо деякі випадки (введення -> вихід):
#
# 1, 10 -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# 1, 100 -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
#
# Якщо в діапазоні [a, b] таких чисел немає, функція має вивести порожній список.
#
# 90, 100 --> []


def exponentiation_and_summation(data, powers: list[int]) -> int:
    """Data and powers type must be list[int]"""
    numbers_powers = list(map(pow, data, powers))
    return sum(numbers_powers)


def converts_number_to_string(number: int) -> list[int]:
    """Convert  234 -> [2, 3, 4]"""
    numbers = []
    while number > 0:
        numbers.append(number % 10)
        number //= 10
    numbers.reverse()
    return numbers


def power(index: int) -> list[int]:
    """Convert  234 -> [1, 2, 3]"""
    index_number = list(range(1, len(str(index)) + 1))
    return index_number


if __name__ == '__main__':
    #   Enter a range of numbers

    while True:
        number_first_of_name = input('Please put a first number your range: ')
        if number_first_of_name.isnumeric():
            number_first_of_name = int(number_first_of_name)
            break
        else:
            print('It si not number, please try again')

    while True:
        number_second_of_name = input('Please put a second number your range: ')
        if number_second_of_name.isnumeric() and int(number_second_of_name) >= number_first_of_name:
            number_second_of_name = int(number_second_of_name)
            print('Your range: (', number_first_of_name, ',', number_second_of_name, ')')
            break
        else:
            print('It is not number or your second number > first number, please try again')

    range_numbers = list(range(number_first_of_name, number_second_of_name + 1))
    number_exp_sum_list = []

    for number in range_numbers:
        number_exp_sum = exponentiation_and_summation(converts_number_to_string(number), power(number))
        if number == number_exp_sum:
            number_exp_sum_list.append(number_exp_sum)
    print(number_exp_sum_list)

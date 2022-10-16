# Написати функцію, яка сортує список, але всі парні числа мають залишитись на своєму місці.
#
# Приклади:
#
# sort_array([3, 1]) -> [1, 3]
# sort_array([3, 2, -1, 4]) -> [-1, 2, 3, 4]
# sort_array([5, 3, 2, 8, 1, 4]) -> [1, 3, 2, 8, 5, 4]


def sort_without_even_numbers(numbers):
    numbers_odd = []
    numbers_temp = []
    numbers_even = []
    numbers_sort = []
    for number in numbers:
        if number % 2 == 0:
            numbers_even.append(number)
            numbers_temp.append(number)
        else:
            numbers_temp.append(1)
            numbers_odd.append(number)

    numbers_odd.sort()

    for number in numbers_temp:
        if number == 1:
            numbers_sort.append(numbers_odd[0])
            del numbers_odd[0]
        else:
            numbers_sort.append(numbers_even[0])
            del numbers_even[0]
    return numbers_sort


if __name__ == '__main__':
    CASES = (
        ([3, 1], [1, 3]),
        ([3, 2, -1, 4], [-1, 2, 3, 4]),
        ([5, 3, 2, 8, 1, 4], [1, 3, 2, 8, 5, 4])
    )
    for case, answer in CASES:
        assert sort_without_even_numbers(case) == answer

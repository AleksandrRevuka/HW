"""A thousand rolls of dice"""
from random import randint
from collections import Counter
from prettytable import PrettyTable
from datetime import datetime


def calc_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        data = func(*args, **kwargs)
        end = datetime.now()
        print(f'Time executed {func.__name__}(): {end - start}')
        print(f'Args positional {args}, kwargs: {kwargs}')
        return data
    return wrapper


def tossing_two_dice():
    sum_two_dice = randint(1, 6) + randint(1, 6)
    return sum_two_dice


def sort_and_count(data: list):
    count_box = Counter(data)
    sort_count_box = sorted(count_box.items(), key=lambda x: x[0])
    return sort_count_box


def thousand_rolls():
    counter = 0
    box_thousand_rolls = []
    while counter < number_of_rolls:
        counter += 1
        box_thousand_rolls.append(tossing_two_dice())
    return box_thousand_rolls


def math_chance_drop_dice():
    math_chance = []
    counter = 1
    while counter <= 6:
        probability = round(counter / 36 * 100, 2)
        math_chance.append(probability)
        counter += 1
    counter = 5
    while counter > 0:
        probability = round(counter / 36 * 100, 2)
        math_chance.append(probability)
        counter -= 1
    return math_chance


def chance_drop_dice(data, math_chance: list):
    box_drop_chance = []
    counter = 0
    for value in data:
        value = list(value)
        chance = round(100 / number_of_rolls * value[1], 2)
        value.append(chance)
        value.append(math_chance[counter])
        box_drop_chance.append(value)
        counter += 1
    return box_drop_chance


def print_result_table(data: list):
    element_table = PrettyTable()
    value_dice = []
    number_of_drops = []
    chance = []
    math_chance = []
    for value_0, value_1, value_2, value_3 in data:
        value_dice.append(value_0)
        number_of_drops.append(value_1)
        chance.append(value_2)
        math_chance.append(value_3)
    element_table.add_column('Dice', value_dice)
    element_table.add_column('Number of dice rolled', number_of_drops)
    element_table.add_column('Chance', chance)
    element_table.add_column('Expected value', math_chance)
    print(element_table)


@calc_time
def main():
    box_thousand_rolls = thousand_rolls()
    sort_and_count_rolls = sort_and_count(box_thousand_rolls)
    math_chance = math_chance_drop_dice()
    sort_and_count_rolls_plus_chance = chance_drop_dice(sort_and_count_rolls, math_chance)
    print_result_table(sort_and_count_rolls_plus_chance)


if __name__ == '__main__':
    number_of_rolls = 1000000
    main()

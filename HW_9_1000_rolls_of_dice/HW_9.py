"""A thousand rolls of dice"""
from random import randint
from collections import Counter
from prettytable import PrettyTable
from typing import NamedTuple


class SumDice(NamedTuple):
    """Type class for element"""
    dice: str
    number_of_dice_rolled: str
    chance: str
    expected_value: str


def tossing_two_dice():
    sum_two_dice = randint(1, 6) + randint(1, 6)
    return sum_two_dice


def sort_and_count(data: list):
    count_box = Counter(data)
    sort_count_box = sorted(count_box.items())
    return sort_count_box


def thousand_rolls(number_rolls):
    box_thousand_rolls = [tossing_two_dice() for _ in range(number_rolls)]
    return box_thousand_rolls


def chance_drop_dice(data, math_chance, number_rolls):
    box_drop_chance = []
    for counter, value in enumerate(data):
        dice = value[0]
        number_of_dice_rolled = value[1]
        chance = round(100 / number_rolls * value[1], 2)
        expected_value = math_chance[counter]
        box_chance = SumDice(dice, number_of_dice_rolled, chance, expected_value)
        box_drop_chance.append(box_chance)
    return box_drop_chance


def print_result_table(sum_dice: list[SumDice]):
    element_table = PrettyTable()
    element_table.field_names = ['Sum dice', 'Number of dice rolled', 'Chance', 'Expected value']
    for dice in sum_dice:
        element_table.add_row([dice.dice, dice.number_of_dice_rolled, dice.chance, dice.expected_value])
    print(element_table)


def main(number_rolls):
    box_thousand_rolls = thousand_rolls(number_rolls)
    sort_and_count_rolls = sort_and_count(box_thousand_rolls)
    math_chance = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
    sort_and_count_rolls_plus_chance = chance_drop_dice(sort_and_count_rolls, math_chance, number_rolls)
    print_result_table(sort_and_count_rolls_plus_chance)


if __name__ == '__main__':
    number_of_rolls = 10000
    main(number_of_rolls)

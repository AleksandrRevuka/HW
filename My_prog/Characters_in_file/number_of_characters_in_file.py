import os
from string import ascii_letters
from collections import Counter

from Homework.My_prog.Characters_in_file.diagram import make_diagram


def check_exist_type_file(filename: str):
    """Check FileNotFoundError, UnicodeDecodeError exceptions"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text format'
    return False


def make_string(text: str):
    """Make string from txt file"""
    with open(text) as file:
        text_file = file
        text_symbols = ''
        for word in text_file:
            for symbol in word:
                if symbol in LETTERS:
                    text_symbols += symbol.lower()
    return text_symbols


def counter_symbols(all_symbols: str):
    """Counter symbols in string"""
    symbols = Counter(all_symbols)
    sorted_symbols = sorted(symbols.items())
    return dict(sorted_symbols)


def count_percent(data: dict):
    """Count percentage of each symbols"""
    sum_value = 0
    for value in data.values():
        sum_value += value
    percent_all = []
    for value in data.values():
        percent = round((100 / sum_value) * value, 2)
        percent_all.append(percent)
    return percent_all


def make_data_diagram(data: dict):
    """Make data for diagram"""
    percents = count_percent(data)
    symbols = []
    values = []
    counter = 0
    for key, value in data.items():
        symbols.append(f"'{key}' ({percents[counter]}%)")
        values.append(value)
        counter += 1
    return symbols, values


def main(text_book: str):
    check_exist_type_file(text_book)
    only_symbols = make_string(text_book)
    data = counter_symbols(only_symbols)
    data_symbol, data_value = make_data_diagram(data)
    print(data_symbol)
    print(data_value)
    make_diagram(data_symbol, data_value)


if __name__ == '__main__':
    LETTERS = ascii_letters

    current_dir = os.getcwd()
    all_text = os.path.join(current_dir, 'english_text.txt')
    main(all_text)

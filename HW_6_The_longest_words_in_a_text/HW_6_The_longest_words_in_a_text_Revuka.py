""" The program searches for the longest word in a text file"""
import os


def filter_line(data):
    elements = [word.strip() for word in data]
    elements = [word.strip('.,:()/') for word in elements]
    return elements


def number_of_largest_words(data):
    max_len_word = 0
    for word in data:
        if len(word) > max_len_word:
            max_len_word = len(word)
    longest_word = [word for word in data if len(word) == max_len_word]
    return longest_word


def check_exist_type_file(filename: str):
    """Check FileNotFoundError, UnicodeDecodeError exceptions"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text format'
    return False


if __name__ == '__main__':
    current_dir = os.getcwd()
    user_file = os.path.join(current_dir, 'example.txt')
    check_exist_type_file(user_file)

    with open(user_file) as file:
        biggest_words = []
        for line in file:
            biggest_words = biggest_words + number_of_largest_words(filter_line(line.split(' ')))
    print(f"The biggest words: {number_of_largest_words(biggest_words)}")

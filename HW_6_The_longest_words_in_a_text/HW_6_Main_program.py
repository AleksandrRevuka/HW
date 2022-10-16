""" The program searches for the longest word in a text file"""
import os

from package.hw_6_functions import check_file, number_of_largest_words, filter_line


if __name__ == '__main__':
    current_dir = os.getcwd()
    user_file = os.path.join(current_dir, 'example.txt')
    check_file(user_file)

    with open(user_file) as file:
        biggest_words = []
        for line in file:
            biggest_words = biggest_words + number_of_largest_words(filter_line(line.split(' ')))
    print(f"The biggest words: {number_of_largest_words(biggest_words)}")

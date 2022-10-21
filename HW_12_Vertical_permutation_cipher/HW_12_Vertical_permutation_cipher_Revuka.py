"""Vertical permutation cipher"""
import os
from random import shuffle


def check_type_exist(filename: str):
    """Check if file exist and has text type"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text type'
    return False


def check_input_int(data: str):
    """Check input has int type"""
    try:
        numbers = list(data.split(', '))
        for number in numbers:
            int(number)
    except ValueError as error:
        return exit(print(error))
    return True


def generate_key(length_key):
    """Generate key"""
    key = [number for number in range(1, length_key + 1)]
    shuffle(key)
    return key


def encode_text(text_encode, keys, length_key):
    """Encode text"""
    data_text = {}
    for counter, key in enumerate(keys):
        encode_line = text_encode[counter::length_key]
        normalize_encode_line = [symbol.strip('\n') for symbol in encode_line]
        data_text[key] = normalize_encode_line
    return data_text


def decode_text(key_decode, text_decode, length_key_decode):
    """Decode text"""
    length_text = len(text_decode)
    number_long_lines = length_text % length_key_decode
    characters = length_text // length_key_decode
    data_text = {}
    for key in key_decode:
        data_text[key] = []
    long_str = key_decode[0:number_long_lines]
    counter = 1
    while counter <= length_key_decode:
        if counter in long_str:
            data_text[counter] = text_decode[:characters + 1]
            text_decode = text_decode[characters + 1:]
            counter += 1
        else:
            data_text[counter] = text_decode[:characters]
            text_decode = text_decode[characters:]
            counter += 1
    return data_text


def read_txt_file(user_file):
    """Read file and make data structure"""
    text = ''
    with open(user_file) as file:
        for line in file:
            text += line
    return text


def normalize_key_user(user_key):
    """Make key in int type"""
    keys = list(user_key.split(', '))
    key_decode = [int(key) for key in keys]
    length_key_decode = len(key_decode)
    return key_decode, length_key_decode


def print_result(encoded_text, key):
    """Print result encode text and key"""
    sort_encoded_text = dict(sorted(encoded_text.items()))
    encode_result = ''
    for text in sort_encoded_text.values():
        for symbol in text:
            encode_result += symbol
    print(f'Key for decode: {key}')
    print(f'Encode text:"{encode_result}"')


def print_result_table(encoded_text):
    """"Print result to table"""
    for key, element in encoded_text.items():
        print(f'{key:3}  ', end='')
        for col in element:
            print(f'{col:3}', end='')
        print()


def main(encode_file, decode_file):
    """Main controller"""
    check_encode_file = check_type_exist(encode_file)
    if check_encode_file:
        exit(print(check_encode_file))
    check_decode_file = check_type_exist(decode_file)
    if check_decode_file:
        exit(print(check_decode_file))
    user_choice = input("What do you want? encode or decode file 'encode.txt' e/d ('' - exit): ")
    if user_choice == 'e':
        length_key = input("How long should the key be? : ")
        check_input = check_input_int(length_key)
        if check_input:
            text_encode = read_txt_file(encode_file)
            key = generate_key(int(length_key))
            encoded_text = encode_text(text_encode, key, int(length_key))
            print_result(encoded_text, key)
    elif user_choice == 'd':
        key_user = input("Enter the decode key (example: '1, 3, 5, 7'): ")
        check_input = check_input_int(key_user)
        if check_input:
            key_decode, length_key_decode = normalize_key_user(key_user)
            text_decode = read_txt_file(decode_file)
            decoded_text = decode_text(key_decode, text_decode, length_key_decode)
            print_result_table(decoded_text)
    elif user_choice == '':
        exit('Good bye')
    else:
        print(ValueError)
        main(file_encode, file_decode)


if __name__ == '__main__':
    current_dir = os.getcwd()
    file_encode = os.path.join(current_dir, 'encode.txt')
    file_decode = os.path.join(current_dir, 'decode.txt')
    main(file_encode, file_decode)

"""Caesar cipher, a module that encode and decode a message with a given shift"""
import os


def check_type_exist(filename: str):
    """Check if file exist and has text type"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text type'
    return False


def check_symbol(data: str):
    """Check symbol"""
    symbol = data.isalpha()
    if symbol:
        return symbol
    return exit(print('Alphabet is not correct'))


def make_alphabet(alphabet_file):
    """Make alphabet"""
    temp_alphabet = ''
    with open(alphabet_file) as symbols_file:
        for line in symbols_file:
            temp_alphabet += line
    for symbol in temp_alphabet:
        check_symbol(symbol)
    alphabet = list(set(temp_alphabet))
    alphabet.sort()
    return alphabet


def encode_alphabet(alphabet: list, shift):
    """Make alphabet with shift"""
    slice_alphabet = alphabet[:shift]
    shift_alphabet = alphabet.copy()
    for symbol in slice_alphabet:
        shift_alphabet.append(symbol)
        shift_alphabet.remove(symbol)
    return shift_alphabet


def encode_line(line: str, alphabet: list, shift_alphabet):
    """Encode line"""
    code_line = ''
    for symbol in line:
        symbol = symbol.lower()
        if symbol in alphabet:
            index = alphabet.index(symbol)
            encode_symbol = shift_alphabet[index]
            code_line += encode_symbol
        else:
            code_line += symbol
    return code_line


def encode_txt_file(encode_file, alphabet: list, shift_alphabet: list):
    file_encoded = open('encoded_file.txt', 'w')
    with open(encode_file) as file:
        for line in file:
            code_line = encode_line(line, alphabet, shift_alphabet)
            file_encoded.write(code_line)


def main(encode_file, alphabet_file, shift: int):
    check_encode_file = check_type_exist(encode_file)
    if check_encode_file:
        exit(print(check_encode_file))
    check_alphabet_file = check_type_exist(alphabet_file)
    if check_alphabet_file:
        exit(print(check_alphabet_file))
    alphabet = make_alphabet(alphabet_file)
    shift_alphabet = encode_alphabet(alphabet, shift)
    encode_txt_file(encode_file, alphabet, shift_alphabet)


if __name__ == '__main__':
    SHIFT = 3
    current_dir = os.getcwd()
    file_alphabet = os.path.join(current_dir, 'alphabet.txt')
    file_encode = os.path.join(current_dir, 'encode.txt')
    main(file_encode, file_alphabet, SHIFT)

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


def check_symbol(symbol: str):
    """Check symbol"""
    symbol.isalpha()
    if symbol:
        return symbol
    return exit(print('Alphabet is not correct'))


def make_alphabet(alphabet_file):
    """Make alphabet"""
    temp_alphabet = ''
    with open(alphabet_file) as symbols_file:
        for line in symbols_file:
            temp_alphabet += line
    temp_alphabet = temp_alphabet.lower()
    for symbol in temp_alphabet:
        check_symbol(symbol)
    alphabet = list(set(temp_alphabet))
    alphabet.sort()
    return alphabet


def encode_alphabet(alphabet: list, shift: int):
    """Make alphabet with shift"""
    slice_alphabet = alphabet[:shift]
    shift_alphabet = alphabet.copy()
    for symbol in slice_alphabet:
        shift_alphabet.append(symbol)
        shift_alphabet.remove(symbol)
    return shift_alphabet


def encode_line(line: str, alphabet: list, shift_alphabet: list):
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
    """Encode file and writ result to file"""
    file_encoded = open('encoded_file.txt', 'w')
    with open(encode_file) as file:
        for line in file:
            code_line = encode_line(line, alphabet, shift_alphabet)
            file_encoded.write(code_line)
    print('Encode file "encoded_file.txt" successful')


def decode_line(line: str, alphabet: list, shift_alphabet: list):
    """Decode line"""
    code_line = ''
    for symbol in line:
        symbol = symbol.lower()
        if symbol in shift_alphabet:
            index = shift_alphabet.index(symbol)
            encode_symbol = alphabet[index]
            code_line += encode_symbol
        else:
            code_line += symbol
    return code_line


def decode_txt_file(decode_file, alphabet: list, shift_alphabet: list):
    """Decode file and writ result to file"""
    file_decoded = open('decoded_file.txt', 'w')
    with open(decode_file) as file:
        for line in file:
            code_line = decode_line(line, alphabet, shift_alphabet)
            file_decoded.write(code_line)
    print('Decode file "decoded_file.txt" successful')


def main(encode_file, alphabet_file, decode_file):
    """Main controller"""
    check_encode_file = check_type_exist(encode_file)
    if check_encode_file:
        exit(print(check_encode_file))
    check_alphabet_file = check_type_exist(alphabet_file)
    if check_alphabet_file:
        exit(print(check_alphabet_file))
    alphabet = make_alphabet(alphabet_file)
    user_choice = input("What do you want? encode or decode e/d ('' - exit): ")
    if user_choice == 'e':
        shift = int(input('With what shift do we encode the text in the file? :'))
        shift_alphabet = encode_alphabet(alphabet, shift)
        encode_txt_file(encode_file, alphabet, shift_alphabet)
    elif user_choice == 'd':
        shift = int(input('With what shift do we decode the text in the file? :'))
        shift_alphabet = encode_alphabet(alphabet, shift)
        decode_txt_file(decode_file, alphabet, shift_alphabet)
    elif user_choice == '':
        exit('Good bye')
    else:
        print(ValueError)


if __name__ == '__main__':
    current_dir = os.getcwd()
    file_alphabet = os.path.join(current_dir, 'alphabet.txt')
    file_encode = os.path.join(current_dir, 'encode.txt')
    file_decode = os.path.join(current_dir, 'decode.txt')
    main(file_encode, file_alphabet, file_decode)

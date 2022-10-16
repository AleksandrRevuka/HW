"""Program that displays the sequence of buttons that must be pressed
in order for text to appear on the screen of a push-button phone"""


def make_phone_map_keys(keys_table: dict[str, tuple[str]]):
    phone_map_keys = {}
    for key, chars in keys_table.items():
        char_codes = {char: key * index + '_' for index, char in enumerate(chars, 1)}
        phone_map_keys.update(char_codes)
    return phone_map_keys


def filter_text_message(text_message: str,  keys_table: dict[str, tuple[str]]):
    filtered_message = ''
    for symbol in text_message:
        symbol = symbol.lower()
        if symbol in keys_table:
            filtered_message += symbol
    return filtered_message


def encode_message(filtered_message: str, keys_table: dict[str, tuple[str]]):
    encoded_message = ''
    for symbol in filtered_message:
        if symbol in keys_table:
            encoded_message += keys_table[symbol]
    print(encoded_message)
    return encoded_message


def filter_message_for_decode(message_for_decode: str, valid_characters: list):
    filtered_message_for_decode = ''
    for symbol in message_for_decode:
        if symbol in valid_characters:
            filtered_message_for_decode += symbol
    return filtered_message_for_decode


def get_key(keys_table: dict[str, tuple[str]], symbol: str):
    for key, value in keys_table.items():
        if value == symbol:
            return key


def decode_message(message_decode: str, keys_table: dict[str, tuple[str]]):
    message_decode = message_decode.split('_')
    decoded_message = ''
    for symbol in message_decode:
        symbol += '_'
        if symbol in keys_table.values():
            key = get_key(keys_table, symbol)
            decoded_message += key
    return decoded_message


def main(keys_table: dict[str, tuple[str]], valid_characters: list):
    user_choice = input('Would you like to encode or decode? e/d: ')
    if user_choice == 'e':
        user_message = input('Enter your message for encode, '
                             'for example "Hello, world!": ')
        filtered_message = filter_text_message(user_message, keys_table)
        encoded_message = encode_message(filtered_message, keys_table)
        print(encoded_message)
        main(keys_table, valid_characters)
    elif user_choice == 'd':
        print('You need to enter each character of the word through "_", '
              'for example "44_33_555_555_666_11_0_9_666_777_555_3_1111": ')
        user_message = input('Enter you message for decode: ')
        filtered_message_decode = filter_message_for_decode(user_message, valid_characters)
        decoded_message = decode_message(filtered_message_decode, keys_table)
        print(decoded_message)
        main(keys_table, valid_characters)
    elif user_choice == '':
        exit('Good bye, my friend')
    else:
        print("If you want exit enter '', try again!")
        main(keys_table, valid_characters)


if __name__ == '__main__':
    phone_keys_table = {
        '1': ('.', ',', '!', ':'),
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z'),
        '0': (' ',)
    }
    box_valid_characters = ['_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    phone_mapping_keys = make_phone_map_keys(phone_keys_table)
    print(phone_mapping_keys)
    main(phone_mapping_keys, box_valid_characters)

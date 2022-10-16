"""Program that displays the sequence of buttons that must be pressed
in order for text to appear on the screen of a push-button phone"""


def filter_text_message(text_message: str,  keys_table: dict):
    filtered_message = ''
    for symbol in text_message:
        symbol = symbol.lower()
        if symbol in keys_table:
            filtered_message += symbol
    return filtered_message


def encode_message(filtered_message: str, keys_table: dict):
    encoded_message = ''
    for symbol in filtered_message:
        if symbol in keys_table:
            encoded_message += str(keys_table[symbol])
    return encoded_message


def filter_message_for_decode(message_for_decode: str):
    valid_characters = ['_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    filtered_message_for_decode = ''
    for symbol in message_for_decode:
        if symbol in valid_characters:
            filtered_message_for_decode += symbol
    return filtered_message_for_decode


def get_key(keys_table: dict, symbol: int):
    for key, value in keys_table.items():
        if value == symbol:
            return key


def decode_message(message_decode: str, keys_table: dict):
    message_decode = message_decode.split('_')
    message_decode = list(map(int, message_decode))
    decoded_message = ''
    for symbol in message_decode:
        if symbol in keys_table.values():
            key = get_key(keys_table, symbol)
            decoded_message += key
    return decoded_message


def main(keys_table: dict):
    user_choice = input('Would you like to encode or decode? e/d: ')
    if user_choice == 'e':
        user_message = input('Enter your message for encode, '
                             'for example "Hello, world!": ')
        filtered_message = filter_text_message(user_message, keys_table)
        encoded_message = encode_message(filtered_message, keys_table)
        print(encoded_message)
        main(keys_table)
    elif user_choice == 'd':
        print('You need to enter each character of the word through "_", '
              'for example "44_33_555_555_666_11_0_9_666_777_555_3_1111": ')
        user_message = input('Enter you message for decode: ')
        filtered_message_decode = filter_message_for_decode(user_message)
        decoded_message = decode_message(filtered_message_decode, keys_table)
        print(decoded_message)
        main(keys_table)
    elif user_choice == '':
        exit('Good bye, my friend')
    else:
        print("If you want exit enter '', try again!")
        main(keys_table)


if __name__ == '__main__':
    phone_keys_table = {
        '.': 1, ',': 11, '?': 111, '!': 1111, ':': 11111,
        'a': 2, 'b': 22, 'c': 222,
        'd': 3, 'e': 33, 'f': 333,
        'g': 4, 'h': 44, 'i': 444,
        'j': 5, 'k': 55, 'l': 555,
        'm': 6, 'n': 66, 'o': 666,
        'p': 7, 'q': 77, 'r': 777, 's': 7777,
        't': 8, 'u': 88, 'v': 888,
        'w': 9, 'x': 99, 'y': 999, 'z': 9999,
        ' ': 0
    }
    main(phone_keys_table)
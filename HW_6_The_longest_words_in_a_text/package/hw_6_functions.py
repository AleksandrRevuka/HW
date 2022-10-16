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


def check_file(file_check):
    try:
        open(file_check, mode='rt').readline()
    except UnicodeDecodeError:
        print('App can use only text files')
        exit()
    except FileNotFoundError as error:
        print(error)
        exit()

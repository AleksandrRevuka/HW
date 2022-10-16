"""Find all emails from a file and display statistics on the number of emails for all domains"""
import os
import re
from collections import Counter
from prettytable import PrettyTable
from datetime import datetime


def calc_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        data = func(*args, **kwargs)
        end = datetime.now()
        print(f'Time executed {func.__name__}(): {end - start}')
        print(f'Args positional {args}, kwargs: {kwargs}')
        return data
    return wrapper


def check_type_exist(filename: str):
    """Check if file exist and has text type"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text type'
    return False


def check_host_format(data: str):
    """Check emails format like 'jzaremba@unicon.net' and 'ian@caret.cam.ac.uk'"""
    host = re.findall(r'(@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', data)
    if not host:
        host = False
    return host


def read_file_and_make_host_box(filename: str):
    """Read data from txt file"""
    hosts = []
    with open(filename) as box_file:
        for line in box_file:
            host = check_host_format(line)
            if host:
                host = [i[1:] for i in host]
                hosts += host
            else:
                pass
    return hosts


def counter_and_sort_unique_hosts(data: list):
    counter_host = Counter(data)
    sorted_hosts = sorted(counter_host.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_hosts)


def print_result_table(hosts: dict):
    """Print unique hosts"""
    print(hosts)
    element_table = PrettyTable()
    name_host = []
    amount = []
    for key, value in hosts.items():
        name_host.append(key)
        amount.append(value)
    element_table.add_column('Name domain', name_host)
    element_table.add_column('Emails quantity', amount)
    print(element_table)


@calc_time
def main(filename: str):
    check = check_type_exist(filename)
    if check:
        exit(print(check))

    box_hosts = read_file_and_make_host_box(filename)
    counter_hosts = counter_and_sort_unique_hosts(box_hosts)
    print(counter_hosts)
    print_result_table(counter_hosts)


if __name__ == '__main__':
    current_dir = os.getcwd()
    file = os.path.join(current_dir, 'mbox.txt')
    main(file)

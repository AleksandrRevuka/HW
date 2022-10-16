"""Search in the file for chemical elements and display their characteristics"""
import os


def check_exist_type_file(filename: str):
    """Check FileNotFoundError, UnicodeDecodeError exceptions"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text format'
    return False


def filter_line(data):
    """Clean the line from garbage"""
    elements = [word.strip() for word in data]
    return elements


def make_chemistry_table(file):
    """Create a list of elements"""
    with open(chemistry_elements_file) as file:
        elements = []
        for line in file:
            data = filter_line(line.split(','))
            data_elements = {'protons': data[0], 'designation': data[1], 'name of a chemical element': data[2]}
            elements.append(data_elements)
    return elements


def check_errors_print_results(searched_element: str):
    check_error = True
    for chemistry_element in chemistry_elements:
        if searched_element == chemistry_element['protons']:
            designation = chemistry_element['designation']
            name_element = chemistry_element['name of a chemical element']
            print(f"You enter {searched_element}, this chemistry element: {name_element}, "
                  f"it's short name: {designation}, it has {searched_element} protons.\n {'= '*45}")
            main()
        elif searched_element == chemistry_element['designation']:
            protons = chemistry_element['protons']
            name_element = chemistry_element['name of a chemical element']
            print(f"You enter short name: {searched_element}, this chemistry element: {name_element}, "
                  f"it has {protons} protons.\n {'= '*45}")
            main()
        elif searched_element == chemistry_element['name of a chemical element']:
            protons = chemistry_element['protons']
            designation = chemistry_element['designation']
            print(f"You enter chemistry element: {searched_element}, it's short name: {designation}, "
                  f"it has {protons} protons.\n {'= '*45}")
            main()
    return check_error


def main():
    searched_element = input('Please put a chemistry element: ')
    if searched_element == '':
        exit("Good luck my junior chemist")

    check_error = check_errors_print_results(searched_element)

    if check_error:
        print(f"This '{searched_element}' chemical element does not exist, please try again.\n {'* '*45}")
        main()


if __name__ == '__main__':
    current_dir = os.getcwd()
    chemistry_elements_file = os.path.join(current_dir, 'elements.txt')
    check_exist_type_file(chemistry_elements_file)

    chemistry_elements = make_chemistry_table(chemistry_elements_file)
    main()

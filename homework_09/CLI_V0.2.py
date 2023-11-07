import sys
import re


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError, TypeError) as e:
            return f'An error occurred: {e}'
    return wrapper


def exit_program_f(*args):
    return sys.exit(f'Exiting the program.\nHave a nice day.')



def show_all_f(contact_list):
    result = []
    if not contact_list:
        return 'Contact list is empty.'
    for name, phone in contact_list.items():
        result += f'Name: {name.capitalize()}, Phone number: {phone}',
    return '\n'.join(result)


@input_error
def add_f(contact_list, *args):
    name, phone = args
    try:
        int(phone)
        contact_list[name] = phone
        return f'Contact {name.capitalize()} with phone number {phone} added to the list.'
    except ValueError:
        return f'Wrong value. The phone number must consist of digits.'


@input_error
def change_f(contact_list, *args):
    name, phone = args
    if name in contact_list:
        try:
            int(phone)
            contact_list[name] = phone
            return f'Contact {name.capitalize()} with phone number {phone} added to the list.'
        except ValueError:
            return f'Wrong value. The phone number must consist of digits.'
    else:
        return f'Contact {name.capitalize()} not found.'


@input_error
def phone_f(contact_list, name):
    if name in contact_list:
        return f'The phone number for {name.capitalize()} is {contact_list[name]}.'
    else:
        return f"Contact {name.capitalize()} not found."


def help_f(*args):
    return f'Available commands:\n' \
           f'-hello => Greetings\n' \
           f'-add [name] [phone number] => Adds a contact to the book\n' \
           f'-change [name] [phone number] => Changes a contact in a book\n' \
           f'-phone [name] => Shows contact number\n' \
           f'-show all => Shows all contacts numbers\n' \
           f'-good bye, close, exit, quit => Exiting the program'

def hello_f(*args):
    return f'Hello. How can I help you?'

COMMAND_LIST = {
    'help': help_f,
    'hello': hello_f,
    'add': add_f,
    'change': change_f,
    'phone': phone_f,
    'show all': show_all_f,
    'good bye': exit_program_f,
    'close': exit_program_f,
    'exit': exit_program_f,
    'quit': exit_program_f,
    'qqq': exit_program_f,
    '.': exit_program_f,
}

contact_list = {}


def main():
    help_massage = help_f()
    print(help_massage)
    print(f'Expecting commend.')
    while True:
        user_input = input('>>> ').lower()
        if re.findall(r'\.', user_input):
            exit_massage = exit_program_f()
            print(exit_massage)
        else:
            for key in COMMAND_LIST.keys():
                if user_input.startswith(key):
                    user_input = user_input.replace(key, '')
                    print(COMMAND_LIST[key](contact_list, *user_input.split()))
                    break
            else:
                print(f'Unknown command. Try again.')


if __name__ == '__main__':
    main()

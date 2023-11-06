import sys


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError, TypeError) as e:
            return print(f'An error occurred: {e}\n')
    return wrapper


def exit_program_f(*args):
    print(f'Exiting the program.\n'
          f'Have a nice day.')
    sys.exit()


def show_all_f(contact_list):
    if not contact_list:
        return print('Contact list is empty.\n')
    for name, phone in contact_list.items():
        print(f'Name: {name.capitalize()}, Phone number: {phone}')
    print('')

@input_error
def add_f(contact_list, *args):
    name, phone = args
    try:
        int(phone)
        contact_list[name] = phone
        print(f'Contact {name.capitalize()} with phone number {phone} added to the list.\n')
        return contact_list
    except ValueError:
        print(f'Wrong value. The phone number must consist of digits.\n')


@input_error
def change_f(contact_list, *args):
    name, phone = args
    if name in contact_list:
        try:
            int(phone)
            contact_list[name] = phone
            print(f'Contact {name.capitalize()} with phone number {phone} added to the list.\n')
            return contact_list
        except ValueError:
            print(f'Wrong value. The phone number must consist of digits.\n')
    else:
        return print(f'Contact {name.capitalize()} not found.\n')

@input_error
def phone_f(contact_list, name):
    if name in contact_list:
        return print(f'The phone number for {name.capitalize()} is {contact_list[name]}.\n')
    else:
        return print(f"Contact {name.capitalize()} not found.\n")

def help_f():
    print(f'Available commands:\n'
          f'-hello => Greetings\n'
          f'-add [name] [phone number] => Adds a contact to the book\n'
          f'-change [name] [phone number] => Changes a contact in a book\n'
          f'-phone [name] => Shows contact number\n'
          f'-show all => Shows all contacts numbers\n'
          f'-good bye, close, exit, quit => Exiting the program\n')

COMMAND_LIST = {
    'help': help_f,
    'hello': lambda contact_list, *args: print("Hello. How can I help you?\n"),
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
    help_f()
    print(f'Expecting commend.\n')
    while True:
        user_input = input('>>> ').lower()
        for key in COMMAND_LIST.keys():
            if user_input.startswith(key):
                user_input = user_input.replace(key, '')
                COMMAND_LIST[key](contact_list, *user_input.split())
                break
        else:
            print(f'Unknown command. Try again.\n')


if __name__ == '__main__':
    main()
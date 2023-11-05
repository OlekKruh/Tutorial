import sys
import re


# Error decorator
def input_error(func):
    def wrapper(contact_list, *args):

    return wrapper


# Exit program function
def exit_program():
    print(f'Exiting the program.\n'
          f'Have a nice day.')
    sys.exit()


# Adding contacts
@input_error
def add(contact_list, *args):
    name = args[0]
    phone = args[1]
    contact_list[name] = phone
    print(f'Contact "{name}" with phone number "{phone}" added to the list.\n')
    return contact_list


# Changing phone in contacts
@input_error
def change(contact_list, *args):
    name = args[0]
    if name in contact_list:
        contact_list[name] = phone
        print(f"Contact '{name}' updated with phone number '{phone}'.")
        return contact_list
    else:
        return print(f"Contact '{name}' not found.")


# Shoving content of Contact list
def show_all(contact_list):
    if not contact_list:
        return 'Contact list is empty.'
    for key, value in contact_list.items():
        print(f'Name: {key}, Phone number: {value}')
    print(f'')


# Shoving contact phone number
def phone(contact_list, *args):
    name = args[0]
    if name in contact_list:
        return print(f'The phone number for {name} is {contact_list[name]}.\n')
    else:
        return print(f"Contact '{name}' not found.\n")


COMMAND_LIST = {
    'hello': lambda contact_list, *args: print("Hello. How can I help you?\n"),
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'good bye': exit_program,
    'close': exit_program,
    'exit': exit_program,
    'quit': exit_program,
    'qqq': exit_program,
    '.': exit_program,
}

contact_list = {}


def main():
    print(f'Expecting commend.\n')
    while True:
        print(f'Available commands:\n'
              f'-hello => Greetings\n'
              f'-add [name] [phone number] => Adds a contact to the book\n'
              f'-change [name] [phone number] => Changes a contact in a book\n'
              f'-phone [name] => Shows contact number\n'
              f'-show all => Shows all contacts numbers\n'
              f'-good bye, close, exit, quit => Exiting the program\n')

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

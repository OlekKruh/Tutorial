import sys
import re


#Error decorator
def input_error(func):
    def wrapper(contact_list, *args):
        try:
            if func.__name__ == 'phone_f' and len(args) == 1:
                name = args[0]
                try:
                    if contact_list[name]:
                        return func(contact_list, name)
                except KeyError:
                    print('This name does not exist in the contact list.\n')

            elif func.__name__ == 'change_f' and len(args) == 2:
                name, phone = args
                if not contact_list:
                    print(f'Yours contact list is empty\n')
                else:
                    try:
                        contact_list[name]
                    except KeyError:
                        print('This name does not exist in the contact list.\n')
                    try:
                        if phone.isdigit():
                            return func(contact_list, name, phone)
                    except ValueError:
                        print('The phone number must consist only of digits.\n')

            elif func.__name__ == 'add_f' and len(args) == 2:
                name, phone = args
                try:
                    phone.isdigit()
                    return func(contact_list, name, phone)
                except ValueError:
                    print('The phone number must consist only of digits.\n')

            else:
                print(f'Enter the command according to the pattern\n')
        except IndexError:
            print('You have entered too many/few values. Try again according to the template.\n')

    return wrapper


# Exit program function
def exit_program_f(*args):
    print(f'Exiting the program.\n'
          f'Have a nice day.')
    sys.exit()


# Adding contacts
@input_error
def add_f(contact_list, name, phone):
    contact_list[name] = phone
    print(f'Contact {name.capitalize()} with phone number {phone} added to the list.\n')
    return contact_list


# Changing phone in contacts
@input_error
def change_f(contact_list, name, phone):
    if name in contact_list:
        contact_list[name] = phone
        print(f'Contact {name.capitalize()} updated with phone number {phone}.\n')
        return contact_list
    else:
        return print(f'Contact {name.capitalize()} not found.\n')


# Shoving content of Contact list
def show_all_f(contact_list):
    if not contact_list:
        return print('Contact list is empty.\n')
    for name, phone in contact_list.items():
        print(f'Name: {name.capitalize()}, Phone number: {phone}\n')


# Shoving contact phone number
@input_error
def phone_f(contact_list, name):
    if name in contact_list:
        return print(f'The phone number for {name.capitalize()} is {contact_list[name]}.\n')
    else:
        return print(f"Contact {name.capitalize()} not found.\n")


COMMAND_LIST = {
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

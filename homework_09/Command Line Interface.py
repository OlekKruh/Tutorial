import sys
import re

# Error decorator
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Wrong contact name.'
        except ValueError:
            return 'Cannot convert data.'
        except IndexError:
            return 'No such contact in your contact list.'
    return wrapper


# Exit program function
def exit_program():
    print(f'Exiting the program.\n'
          f'Have a nice day.')
    sys.exit()


# All available commands output
def help():
    print("Available commands:")
    print("1. hello - Replies on the console 'How can I help you?'")
    print("2. add - Add a new name and phone number to your Notebook")
    print("3. change - Changes the name and phone number of an existing contact")
    print("4. phone - Display the phone number for a specific contact in the console.")
    print("5. show all - Display all saved contacts with phone numbers in the console.")
    print("6. good bye, close, exit, quit - Use any of these commands to exit the program.")
    print("7. Do not use '.' in sentences; this will close the program immediately.")


def add(contact_list):
    print(f'Please enter the data according to the specified sample after >>>\n'
          f'Sample: John 123456789')
    data = input(f'>>> ')
    if re.match(r'^[A-Za-z]+\s\d{9}$', data):
        name, phone = data.split()
        contact_list[name] = phone
        print(f'Contact "{name}" with phone number "{phone}" added to the list.')
    else:

    return contact_list


def show_all(contact_list):
    if not contact_list
        return 'Contact list is empty.'
    for key, value in contact_list.items():
        print(f'Name: {key}, Phone number: {value}')


COMMAND_LIST = {
    'help': help,
    'hello': lambda: "How can I help you?",
    'add': add,
    # 'change': change,
    # 'phone': phone,
    'show all': show_all,
    'good bye': exit_program,
    'close': exit_program,
    'exit': exit_program,
    'quit': exit_program,
    'qqq': exit_program,
    '.': exit_program,
}


def main():
    contact_list = {}
    print_message = False
    while True:
        if not print_message:
            print(f'Expecting commend.')
            print_message = True

        command = input(f'>>> ').lower()

        if command in COMMAND_LIST:
            if command in ['add', 'change', 'phone', 'show all']:
                contact_list = COMMAND_LIST[command](contact_list)
            else:
                COMMAND_LIST[command]()
        else:
            print('Command not recognized. Type "help" for a list of available commands.')


if __name__ == '__main__':
    main()

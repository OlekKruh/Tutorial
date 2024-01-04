from abc import ABC, abstractmethod


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


class UI(ABC):
    def __init__(self):
        self.content = ""

    @abstractmethod
    def display_content(self):
        pass


class UserInput(ABC):
    def __init__(self):
        self.input = ""

    @abstractmethod
    def user_input(self, input_str):
        pass

    @abstractmethod
    def echo(self, input_str):
        pass


class MenuUI(UI, UserInput):
    def display_content(self):
        separator = '='
        quantity = 20
        print(f'{separator * quantity}'
              f'Maine Menu\n'
              f'{separator * quantity}'
              f'1. AddressBook\n'
              f'2. NoteBook\n'
              f'3. Exit\n'
              f'{separator * quantity}')

    def user_input(self, input_str):
        for key in COMMAND_LIST.keys():
            if input_str.startswith(key):
                input_str = input_str.replace(key, '')
                COMMAND_LIST[key](contact_list, *input_str.split())
                break
            else:
                print(f'Unknown command. Try again.\n')

    def echo(self, input_str):
        print(input_str)
from abc import ABC, abstractmethod


class UI(ABC):
    def __init__(self):
        self.content = ""

    @abstractmethod
    def display_content(self, content):
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


class DisplayContact(UI):
    def display_content(self, content):
        return (f'Name: {self._name}\n'
                f'Phone: {", ".join(map(str, self._phone))}\n'
                f'Birthday: {birthday_str}\n'
                f'Days to next Birthday left: {self.days_to_birthday()}\n')


class DisplayNote(UI)
    def display_content(self, content):
        return (f'Title: {self._title}'
                f'Tag: {", ".join(map(str, self._tag))}'
                f'Text: {self._text}')


class ConsoleUserInput(UserInput):
    def user_input(self, input_str):
        self.input = input_str

    def echo(self, input_str):
        print(f"Echo: {input_str}")

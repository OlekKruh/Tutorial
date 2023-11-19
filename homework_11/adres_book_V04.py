import re
from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if self.validate(new_value):
            self.__value = new_value
        else:
            raise ValueError(f"Invalid format for {self.__class__.__name__}.")

    def validate(self, value):
        return True

    def __str__(self):
        return str(self.value)


class Name(Field):
    def validate(self, value):
        return bool(re.match(r'^[A-Za-z]+\s[A-Za-z]+$', value))


class Phone(Field):
    def validate(self, value):
        return bool(re.match(r'\d{10}', value))


class BirthDay(Field):
    def validate(self, value):
        return bool(re.match(r'^(0[1-9]|[12][0-9]|3[01])\.'  # dzień
                             r'(0[1-9]|1[0-2])\.'  # miesiąц 
                             r'(19[4-9][0-9]|200[0-9]|201[0-9]|202[0-4])$',  # рік
                             value))


class Record:
    def __init__(self, name):
        try:
            if not Name(name).validate(name):
                raise ValueError(f'Error: Invalid Name format for {name}\n')
        except ValueError as e:
            print(e)
            self.name = None  # None jak nie zgadza się imię i nazwisko.
        else:
            self.name = Name(name)
        self.phone = []
        self.birthday = []
        self.days_left = None

    # Dodawania numeru telefonu.
    def add_phone(self, phone):
        try:
            if not Phone(phone).validate(phone):
                raise ValueError(f'Error: Invalid phone number format for {phone}\n')
        except ValueError as e:
            print(e)
        else:
            self.phone.append(Phone(phone))

    # Dodawania daty urodzenia.
    def add_birthday(self, birthday):
        try:
            if not BirthDay(birthday).validate(birthday):
                raise ValueError(f'Error: Invalid birthday format for {birthday}\n')
        except ValueError as e:
            print(e)
        else:
            self.birthday.append(BirthDay(birthday))

    # Usuwania numeru telefonu.
    def delete_phone(self, phone):
        self.phone = [i for i in self.phone if str(i) != phone]

    # Usuwania daty urodzin.
    def delete_birthday(self):
        self.birthday = []
        print(f'Birthday deleted successfully.')

    # Zamiana numeru telefonu.
    def edit_phone(self, old_phone, new_phone):
        try:
            if not Phone(new_phone).validate(new_phone):
                raise ValueError(f'Error: Invalid phone number format for {new_phone}\n')
        except ValueError as e:
            print(e)
        else:
            for key, elem in enumerate(self.phone):
                if str(elem) == old_phone:
                    self.phone[key] = Phone(new_phone)
                    break

    # Zamiana daty urodzenia.
    def edit_birthday(self, new_birthday):
        try:
            if not BirthDay(new_birthday).validate(new_birthday):
                raise ValueError(f'Error: Invalid birthday format for {new_birthday}\n')
        except ValueError as e:
            print(e)
        else:
            self.birthday = [BirthDay(new_birthday)]

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now().date()
            day, month, year = map(int, re.findall(r'\d+', self.birthday[0].value))
            next_birthday = datetime(today.year, month, day).date()

            if today > next_birthday:
                next_birthday = datetime(today.year + 1, month, day).date()

            self.days_left = (next_birthday - today).days
            return self.days_left
        else:
            return ''

    # Czytelne wyświetlanie.
    def __str__(self):
        result = (f'Name: {self.name}\n'
                  f'Phone: {", ".join(map(str, self.phone))}\n'
                  f'Birthday: {", ".join(map(str, self.birthday))}\n'
                  f'Days to next Birthday left: {self.days_to_birthday()}\n')
        return result


class AddressBook(UserDict):
    # Zapis do księgi.
    def add_record(self, record: Record):
        if record.name is None:
            raise ValueError(f'Error: The contact cannot be created.\n'
                             f'First and last name entered incorrectly.\n')
        else:
            self.data[record.name.value] = record  # Dodać sprawdzenie. Jak None to wywalić bląd.

    # EXTERMINATUS.
    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact {name} deleted successfully.\n")
        else:
            print(f"Contact {name} not found in the address book.\n")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

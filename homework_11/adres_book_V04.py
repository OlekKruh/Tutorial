import re
from collections import UserDict


class Field:
    def __init__(self, user_data):
        self.user_data = user_data

    def __str__(self):
        return str(self.user_data)


class Name(Field):
    # Sprawdza Imię i Nazwisko.
    def validate(self):
        try:
            first_last_name = re.match(
                r'^[A-Za-z]+\s[A-Za-z]+$',
                self.user_data)
            if not first_last_name:
                return False
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False


class Phone(Field):
    # Sprawdza numer telefonu.
    def validate(self):
        try:
            phone_numbers = re.findall(
                r'\d{10}',
                self.user_data)
            if not phone_numbers:
                return False
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False


class BirthDay(Field):
    # Sprawdza date urodzenia.
    def validate(self):
        try:
            birth_day = re.findall(
                r'^(0[1-9]|[12][0-9]|3[01])\.'  # dzień
                r'(0[1-9]|1[0-2])\.'  # miesiąc 
                r'(19[4-9][0-9]|200[0-9]|201[0-9]|202[0-4])$',  # rok
                self.user_data
            )
            if not birth_day:
                return False
            return True
        except ValueError as e:
            print(f'Error: {e}')
            return False


class Record:
    def __init__(self, name):
        try:
            if not Name(name).validate():
                raise ValueError(f'Error: Invalid Name format for {name}')
        except ValueError as e:
            print(e)
            self.name = None  # None jak nie zgadza się imię i nazwisko.
        else:
            self.name = Name(name)
        self.phone = []

    # Dodawania opcjonalnej informacji.
    def add_phone(self, phone):
        try:
            if not Phone(phone).validate():
                raise ValueError(f'Error: Invalid phone number format for {phone}')
        except ValueError as e:
            print(e)
        else:
            self.phone.append(Phone(phone))

    # Usuwania opcjonalnej informacji.
    def delete_phone(self, phone):
        self.phone = [i for i in self.phone if str(i) != phone]

    # Zamiana opcjonalnego informacji.
    def edit_phone(self, old_phone, new_phone):
        try:
            if not Phone(new_phone).validate():
                raise ValueError(f'Error: Invalid phone number format for {new_phone}')
        except ValueError as e:
            print(e)
        else:
            for key, elem in enumerate(self.phone):
                if str(elem) == old_phone:
                    self.phone[key] = Phone(new_phone)
                    break

    # Czytelne wyświetlanie.
    def __str__(self):
        result = (f'Name: {self.name}\n'
                  f'Phone: {", ".join(map(str, self.phone))}\n')
        return result


class AddressBook(UserDict):
    # Zapis do księgi.
    def add_record(self, record: Record):
        if record.name is None:
            raise ValueError(f'Error: The contact cannot be created.\n'
                             f'First and last name entered incorrectly.\n')
        else:
            self.data[record.name.user_data] = record  # Dodać sprawdzenie. Jak None to wywalić bląd.

    # EXTERMINATUS.
    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found in the address book.")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

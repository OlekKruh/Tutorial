import re
from collections import UserDict


class Field:
    def __init__(self, user_data):
        self.user_data = user_data

    def __str__(self):
        return str(self.user_data)


class Name(Field):
    # Sprawdza Imie i Nazwisko.
    def validate(self):
        try:
            first_last_name = re.match(r'^[A-Za-z]+\s[A-Za-z]+$', self.user_data)
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
            phone_numbers = re.findall(r'\d{10}', self.user_data)
            if not phone_numbers:
                return False
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False


class Email(Field):
    # Sprawdza Maila.
    def validate(self):
        try:
            email = re.findall(r'[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[A-Za-z]'
                               r'|[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[A-Za-z]+\.[A-Za-z]',
                               self.user_data)
            if not email:
                return False
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False


class BirthDay(Field):
    # Sprawdza urodziny.
    def validate(self):
        try:
            birthday = re.findall(r'\d{2}.\d{2}.\d{4}', self.user_data)
            if not birthday:
                return False
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False


class Record:
    def __init__(self, user_data):
        self.user_data = user_data
        self.name = None
        self.phone = []
        self.email = None
        self.birthday = None

        # Sprawdzamy, czy User wprowadził poprawnie Imie z Nazwiskiem.
        try:
            if len(self.user_data) < 2:
                raise ValueError('Insufficient data.\n'
                                 'At least first name and last name are required.\n'
                                 'Other data is optional\n')
            else:
                name_candidate = Name(' '.join(self.user_data[:2]))
                if not name_candidate.validate():
                    raise ValueError('Invalid Name format.\n'
                                     'First of all enter firstname then lastname.\n'
                                     'Then other data.\n')
                else:
                    self.name = name_candidate
                    self.add_optional_data(user_data[2:])
        except ValueError as e:
            print(f"Error: {e}")

    # Logika dodawania opcjonalnej informacji.
    def add_optional_data(self, optional_data):
        field_classes = {
            'Phone': Phone,
            'Email': Email,
            'BirthDay': BirthDay,
        }

        for field_key, field_class in field_classes.items():
            for i in optional_data:
                data = field_class(i)
                if data.validate():
                    if field_key == 'Phone':
                        self.phone.append(data)
                    elif field_key == 'Email':
                        self.email = data
                    elif field_key == 'BirthDay':
                        self.birthday = data

    # Czytelne wyświetlanie.
    def __str__(self):
        result = (f'Name: {self.name}\n'
                  f'Phone: {", ".join(map(str, self.phone))}\n')
        if self.email:
            result += f'Email: {self.email}\n'
        if self.birthday:
            result += f'BirthDay: {self.birthday}\n'
        return result

    # Usuwania opcjonalnej informacji.
    def delete_optional_data(self, field_key):
        if field_key == 'Phone':
            print(f"Phone {self.phone} deleted successfully.\n")
            self.phone = []
        elif field_key == 'Email':
            print(f"Email {self.email} deleted successfully.\n")
            self.email = None
        elif field_key == 'BirthDay':
            print(f"BirthDay {self.birthday} deleted successfully.\n")
            self.birthday = None
        else:
            print(f"{field_key} not found in the contact.\n")

    # Zamiana opcjonalnego informacji.
    def edit_optional_data(self, field_key, new_data):
        if field_key == 'Phone':
            self.phone = [new_data]
        elif field_key == 'Email':
            self.email = new_data
        elif field_key == 'BirthDay':
            self.birthday = new_data
        else:
            print(f"Invalid field key: {field_key}")


class AddressBook(UserDict):
    # Zapis do ksiegi.
    def add_record(self, record):
        if record.name:
            self.data[record.name.user_data] = record
        else:
            print('Error: Cannot add record without a valid Name.')

    # EXTERMINATUS.
    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found in the address book.")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


# Test
data1 = ["John", "Doe", "1234567890", "john.doe@example.com", "02-20-1988"]
data2 = ["John", "john.doe@example.com", "01-05-1988"]
data3 = ["Alice", "Johnson", "555-1234", "alice.johnson@example.com", "06-15-1990"]
data4 = ["Bob", "Smith", "7890123456", "bob.smith@example.com"]
data5 = ["Eve", "Evans", "eve.evans@example.com", "12-25-2000"]

record1 = Record(data1)
record2 = Record(data2)
record3 = Record(data3)
record4 = Record(data4)
record5 = Record(data5)

address_book = AddressBook()
address_book.add_record(record1)
address_book.add_record(record2)
address_book.add_record(record3)
address_book.add_record(record4)
address_book.add_record(record5)

print(address_book)

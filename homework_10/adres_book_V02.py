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
        self.contact = {
            'Name': None,
            'Phone': None,
            'Email': None,
            'BirthDay': None,
        }
        # Sprawdzamy, czy User wprowadził poprawnie Imie z Nazwiskiem.
        try:
            if len(self.user_data) < 2:
                raise ValueError('Insufficient data.\n'
                                 'At least first name and last name are required.\n'
                                 'Ather data is optional\n')
            else:
                self.name = Name(' '.join(self.user_data[:2]))
                if not self.name.validate():
                    raise ValueError('Invalid Name format.\n'
                                     'First of all enter firstname then lastname.\n'
                                     'Then other data.\n')
                else:
                    self.contact['Name'] = self.name
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
                    self.contact[field_key] = data

    # Czytelne wyświetlanie.
    def __str__(self):
        result = ""
        for key, value in self.contact.items():
            result += f'{key}: {value}\n'
        return result


# logika dodawania
# def add_phone(self, phone):
#     phone_field = Phone(phone)
#     phone_field.validate()
#     self.phones.append(phone_field)

# logika usuwania
# def del_phone(self, phone):
#     for i in self.phones:
#         if i.value == phone:
#             self.phones.remove(i)
#             return

# logika edycji
# def edit_value(self, new_value, old_value):
#     self.del_valu(old_valu)
#     self.add_valu(new_valu)

# def find_phone(self, phone):
#     for i in self.phones:
#         if i.value == phone:
#             return i.value

# def __str__(self):
#     return f'Contact: {self.name}, phones: {",".join(str(i) for i in self.phones)}'


# class AddressBook(UserDict):
#     def add_record(self, record):
#         self.data[record.name.value] = record
#
#     def delete(self, name):
#         del self.data[name]
#
#     def find(self, name):
#         return self.data.get(name)
#
#     def __str__(self):
#         return "\n".join(str(record) for record in self.data.values())

# Przykład użycia
data1 = ["John", "Doe", "john.doe@example.com", "02-20-1988"]
record1 = Record(data1)
print(record1)

data2 = ["John", "1234567890", "01-05-1988"]
record2 = Record(data2)
print(record2)

data3 = ["Hanna", "Smith", "1234567890", "12-10-1988"]
record3 = Record(data3)
print(record3)

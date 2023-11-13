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

    # Usuwania opcjonalnej informacji.
    def delete_optional_data(self, field_key):
        if field_key in self.contact:
            self.contact[field_key] = None
            print(f"{field_key} deleted successfully.")
        else:
            print(f"{field_key} not found in the contact.")

    # Zamiana opcjonalnego informacji.
    def edit_optional_data(self, field_key, new_data):
        if field_key in self.contact:
            self.contact[field_key] = new_data
            print(f"{field_key} replaced successfully with {new_data}.")
        else:
            print(f"{field_key} not found in the contact.")


class AddressBook(UserDict):
    # Zapis do ksiegi.
    def add_record(self, record):
        self.data[record.contact['Name'].user_data] = record

    # EXTERMINATUS.
    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found in the address book.")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


# Tworzenie różnych danych testowych
data1 = ["John", "Doe", "john.doe@example.com", "02-20-1988"]
data2 = ["Jane", "Smith", "555-1234", "jane.smith@example.com"]
data3 = ["Alice", "Johnson", "alice.j@example.com", "01-15-1995"]
data4 = ["Bob", "Brown", "1234567890", "bob.b@example.com", "07-07-1980"]
data5 = ["Charlie", "Chaplin", "charlie.c@example.com", "03-16-1975"]
data6 = ["David", "Davis", "555-9876", "david.d@example.com", "11-30-1990"]
data7 = ["Eva", "Evans", "eva.e@example.com", "09-22-1985"]
data8 = ["Frank", "Fisher", "9876543210", "frank.f@example.com", "05-12-2000"]
data9 = ["Grace", "Green", "grace.g@example.com", "04-03-1992"]
data10 = ["Henry", "Hill", "555-5432", "henry.h@example.com", "08-18-1982"]

# Tworzenie rekordów i dodawanie do książki adresowej
record1 = Record(data1)
record2 = Record(data2)
record3 = Record(data3)
record4 = Record(data4)
record5 = Record(data5)
record6 = Record(data6)
record7 = Record(data7)
record8 = Record(data8)
record9 = Record(data9)
record10 = Record(data10)

# Wyświetlanie informacji o rekordach przed modyfikacjami
print("Before modifications:")
print(record1)
print(record2)
print(record3)
print(record4)
print(record5)
print(record6)
print(record7)
print(record8)
print(record9)
print(record10)

# Usuwanie opcjonalnych informacji
record1.delete_optional_data('Phone')
record2.delete_optional_data('Email')
record3.delete_optional_data('BirthDay')
record4.delete_optional_data('Phone')
record5.delete_optional_data('Email')
record6.delete_optional_data('BirthDay')
record7.delete_optional_data('Phone')
record8.delete_optional_data('Email')
record9.delete_optional_data('BirthDay')
record10.delete_optional_data('Phone')

# Wyświetlanie informacji o rekordach po usunięciu opcjonalnych informacji
print("\nAfter deleting optional data:")
print(record1)
print(record2)
print(record3)
print(record4)
print(record5)
print(record6)
print(record7)
print(record8)
print(record9)
print(record10)

# Edytowanie opcjonalnych informacji
record1.edit_optional_data('Phone', '555-9999')
record2.edit_optional_data('BirthDay', '12-31-2000')
record3.edit_optional_data('Email', 'new.email@example.com')
record4.edit_optional_data('BirthDay', '01-01-1990')
record5.edit_optional_data('Phone', '1234567890')
record6.edit_optional_data('Email', 'updated.email@example.com')
record7.edit_optional_data('Phone', '9876543210')
record8.edit_optional_data('BirthDay', '06-15-1988')
record9.edit_optional_data('Email', 'modified.email@example.com')
record10.edit_optional_data('Phone', '999-8888')

# Wyświetlanie informacji o rekordach po edycji opcjonalnych informacji
print("\nAfter editing optional data:")
print(record1)
print(record2)
print(record3)
print(record4)
print(record5)
print(record6)
print(record7)
print(record8)
print(record9)
print(record10)
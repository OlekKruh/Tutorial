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


class Record:
    def __init__(self, name):
        try:
            if not Name(name).validate():
                raise ValueError(f'Error: Invalid Name format for {name}')
        except ValueError as e:
            print(e)
            self.name = Name('Mr Smith')
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

    # Czytelne wyświetlanie.
    def __str__(self):
        result = (f'Name: {self.name}\n'
                  f'Phone: {", ".join(map(str, self.phone))}\n')
        return result

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


class AddressBook(UserDict):
    # Zapis do ksiegi.
    def add_record(self, record: Record):
        self.data[record.name.user_data] = record

    # EXTERMINATUS.
    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found in the address book.")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


# Tworzenie książki adresowej
address_book = AddressBook()

# Dodawanie rekordu do książki adresowej
record1 = Record("John")
record1.add_phone("1234567890")
record1.add_phone("9876543210")
address_book.add_record(record1)

# Wyświetlanie książki adresowej
print(address_book)

# Usuwanie kontaktu z książki adresowej
address_book.delete_contact("John Doe")

# Wyświetlanie książki adresowej po usunięciu kontaktu
print(address_book)

# Dodawanie kolejnego rekordu
record2 = Record("Alice Johnson")
record2.add_phone("5551234567")
record2.add_phone("9876543")
address_book.add_record(record2)

# Wyświetlanie zaktualizowanej książki adresowej
print(address_book)

# Edycja numeru telefonu w rekordzie
record2.edit_phone("5551234567", "5559876543")
print(address_book)

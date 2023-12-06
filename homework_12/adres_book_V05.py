import re
from collections import UserDict
from datetime import datetime
import json


class Field:
    def __init__(self, value):
        self.__value = value

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

    def __str__(self):
        if self.value:
            if "+48" not in self.value:
                formatted_phone = f"+48 {self.value[:3]}-{self.value[3:6]}-{self.value[6:]}"
            else:
                formatted_phone = self.value
            return formatted_phone


class BirthDay(Field):
    def validate(self, value):
        return bool(re.match(r'^(0[1-9]|[12][0-9]|3[01])\.'  # dzień
                             r'(0[1-9]|1[0-2])\.'  # miesiąc 
                             r'(19[4-9][0-9]|200[0-9]|201[0-9]|202[0-4])$',  # rok
                             value))


class Record:
    def __init__(self, name, phone=None, birthday=None):
        try:
            if not Name(str(name)).validate(name):
                raise ValueError(f'Error: Invalid Name format for {name}\n')
        except ValueError as e:
            print(e)
            self.name = None  # None jak nie zgadza się imię i nazwisko.
        else:
            self.name = Name(name)
        self.phone = [Phone(str(phone))] if phone else []
        self.birthday = BirthDay(str(birthday)) if birthday else None

    # Dodawania numeru telefonu.
    def add_phone(self, phone):
        try:
            if not Phone(str(phone)).validate(phone):
                raise ValueError(f'Error: Invalid phone number format for {phone}\n')
        except ValueError as e:
            print(e)
        else:
            self.phone.append(Phone(phone))

    # Dodawania daty urodzenia.
    def add_birthday(self, birthday):
        try:
            if not BirthDay(str(birthday)).validate(birthday):
                raise ValueError(f'Error: Invalid birthday format for {birthday}\n')
        except ValueError as e:
            print(e)
        else:
            self.birthday = BirthDay(birthday)

    # Usuwania numeru telefonu.
    def delete_phone(self, phone):
        self.phone = [i for i in self.phone if str(i) != phone]

    # Usuwania daty urodzin.
    def delete_birthday(self):
        self.birthday = None
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
            self.birthday = BirthDay(str(new_birthday))

    # Obliczamy dni do urodzin.
    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now().date()
            day, month, year = map(int, re.findall(r'\d+', str(self.birthday.value)))
            next_birthday = datetime(today.year, month, day).date()

            if today > next_birthday:
                next_birthday = datetime(today.year + 1, month, day).date()

            return (next_birthday - today).days
        else:
            return ''

    # Czytelne wyświetlanie.
    def __str__(self):
        birthday_str = str(self.birthday) if self.birthday else ''
        return (f'Name: {self.name}\n'
                f'Phone: {", ".join(map(str, self.phone))}\n'
                f'Birthday: {birthday_str}\n'
                f'Days to next Birthday left: {self.days_to_birthday()}\n')


# Kule dla wyciągania numerów z listy [...] w string.
def extract_phone(phone_list):
    return ', '.join(str(Phone(number)) for number in phone_list)


class AddressBook(UserDict):
    def __init__(self, records={}):
        super().__init__(records)
        self.page_size = 1
        self.page_index = 0

    def __iter__(self):
        self.page_index = 0
        return self

    def __next__(self):
        start_index = self.page_index * self.page_size
        end_index = start_index + self.page_size
        page_keys = list(self.data.keys())[start_index:end_index]
        if page_keys:
            self.page_index += 1
            return [self.data[key] for key in page_keys]
        else:
            raise StopIteration()

    # Przewijamy.
    def display_next_page(self):
        try:
            page = next(self)
            for record in page:
                print(record)
        except StopIteration:
            print("No more pages.\n")

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
            print(f"Contact {name} exterminated successfully ;)\n")
        else:
            print(f"Contact {name} not found in the address book.\n")

    def __str__(self, records=None):
        records_to_display = records or self.data.values()
        if records_to_display is not None:
            return "\n".join(str(record) for record in records_to_display)
        else:
            return "No records to display."

    def to_json(self, filename):
        # Robimy strukture slownika z kluczem 'records'
        # w którym każdej user to oddzielny słownik gdzie kluch to imie usera.
        data_to_write = {
            name: {
                'name': str(record.name),
                'phone': list(map(str, record.phone)),
                'birthday': str(record.birthday) if record.birthday else None
            } for name, record in self.data.items()
        }
        with open(filename, 'w') as data_file:
            json.dump(data_to_write, data_file, indent=2)  # Dalem indent zeby bylo czytelne w pliku.

    @classmethod
    def from_json(cls, filename):
        with open(filename, 'r') as data_file:  # Wgrywamy plik.
            data = json.load(data_file)  # Wyciągamy słowniki.
            records = {}

            for name, record_data in data.items():
                phone_list = record_data.get('phone', [])  # Wyciągamy liste z numerami.
                phone_string = extract_phone(phone_list)  # Naszymi kulami robimy string.
                # Stwarzamy objekt i pakujemy do rekordów w AddressBook.
                record = Record(
                    name,
                    phone_string,
                    record_data.get('birthday')
                )
                records[name] = record
        return cls(records)

    # Wyszukiwarka.
    def search(self, pattern):
        matching_record = []

        for record in self.data.values():
            if (
                    re.search(pattern, record.name.value, re.IGNORECASE) or
                    any(re.search(pattern, str(phone), re.IGNORECASE) for phone in record.phone) or
                    (record.birthday and re.search(pattern, record.birthday.value, re.IGNORECASE))
            ):
                matching_record.append(record)

        return self.__str__(matching_record)


# Odczyt z pliku JSON.
address_book = AddressBook.from_json("address_book.json")
print(address_book)

# Wyszukaj i wyświetl rekordy pasujące do wzorca 'al'.
matching_records = address_book.search('A')
print(matching_records)

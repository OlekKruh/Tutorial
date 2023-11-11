from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value


class Name(Field):
    # sprawdza Imie i Nazwisko
    def validate(self):
        if not (
                isinstance(self.value, str) and
                len(self.value.split()) == 2 and
                all(len(part) >= 3 for part in self.value.split())
        ):
            return ValueError('Invalid name format.')


class Phone(Field):
    # sprawdza numer telefonu
    def validate(self):
        if not (
                isinstance(self.value, str) and
                self.value.isdigit() and
                len(self.value) == 10
        ):
            return ValueError('Invalid phone number format')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # logika dodawania
    def add_phone(self, phone):
        phone_fild = Phone(phone)
        self.phones.append(phone_fild)

    # logika usuwania
    def del_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
            return

    # logika edycji
    def edit_phone(self, new_phon, old_phone):
        self.del_phone(old_phone)
        self.add_phone(new_phon)

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i.value

    def __str__(self):
        return f'Contact: {self.name}, phones: {",".join(str(i) for i in self.phones)}'

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        del self.data[name]

    def find(self, name):
        return self.data.get(name)

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

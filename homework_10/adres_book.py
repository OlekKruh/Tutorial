from collections import UserDict


class Field:
    def __init__(self, value):
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

    def __str__(self):
        return str(self.value)


class Phone(Field):
    # sprawdza numer telefonu
    def validate(self):
        if not (
                isinstance(self.value, str) and
                self.value.isdigit() and
                len(self.value) == 10
        ):
            return ValueError('Invalid phone number format')

    def __str__(self):
        return str(self.value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # logika dodawania
    def add_phone(self, phone):
        phone_field = Phone(phone)
        phone_field.validate()
        self.phones.append(phone_field)

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

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
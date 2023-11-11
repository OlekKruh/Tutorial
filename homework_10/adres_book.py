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
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = Phone(phone)
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

# Створення запису для Bob
bob_record = Record("Bob", "5551236780")
# Додавання запису Bob до адресної книги
book.add_record(bob_record)

# Пошук та виведення запису для Bob
print(book.find("Bob"))

# Створення запису для Marly
marly_record = Record("Marly", "5559876543")
# Додавання запису Marly до адресної книги
book.add_record(marly_record)

# Перевірка всіх записів у книзі
print(book)

# Редагування номеру телефону для Bob
bob_record.edit_phone("5550001111", "5551236780")
print(book.find("Bob"))  # Виведення: Contact: Bob, phones: 5550001111

# Додавання нового номеру телефону для Bob
bob_record.add_phone("5552223333")
print(book.find("Bob"))  # Виведення: Contact: Bob, phones: 5550001111,5552223333

# Видалення запису Marly
book.delete("Marly")
print(book)

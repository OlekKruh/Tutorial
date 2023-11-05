import sys
def input_error(func):
    def wrapper(contact_list):
        while True:
            data = input(f'>>> ')
            if len(data.split()) != 2:
                print('Invalid input. Please enter both name and phone number.')
                continue

            name, phone = data.split()
            if not name.isalpha():
                print('Invalid input. Name should only contain letters.')
                continue
            if not phone.isdigit():
                print('Invalid input. Phone number should only contain digits.')
                continue

            contact_list[name] = phone
            print(f'Contact "{name}" with phone number "{phone}" added to the list.')
            break

        return contact_list

    return wrapper

@input_error
def add(contact_list):
    print(f'Please enter the data according to the specified sample after >>>\n'
          f'Sample: John 123456789')
    data = input(f'>>> ')
    name, phone = data.split()
    contact_list[name] = phone
    print(f'Contact "{name}" with phone number "{phone}" added to the list.')
    return contact_list


contact_list = {}

add(contact_list)
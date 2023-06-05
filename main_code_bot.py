import csv
from my_classes import AddressBook, Name, Phone, Birthday, Email, Address, NumberPhoneError, BirthdayError, EmailError, AddressError

# список для хранения имеющихся данных у контактов
contacts_data = []

# список  имен комманд для окончания работы бота:
finish = ['good bye', 'close', 'exit', '.']

# файл csv для сохранение данных адресной книги на диск
file_name = 'contacts_data.csv'

field_names = ['name', 'phones', 'birthday', 'email', 'address']


# функция декоратор для функций обработчиков команд:


def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return f'Name can not be empty, please repeat the command and enter correct user name, or enter next command'
        except ValueError:
            return f'You have entered an invalid command, please refine your query'
        except IndexError:
            return f'Give me name and phone please'
        except NumberPhoneError:
            return f'This number phone is not correct, please repeat the command and enter correct number phone, ' \
                   f'or enter next command'
        except FileNotFoundError:
            return f'Please first enter and save the data'
        except BirthdayError:
            return f'This date is not format, please repeat the command and enter correct date, or enter next command'
        except EmailError:
            return f'This email is not correct, please repeat the command and enter correct email, or enter next command'
        except AddressError:
            return f'This address is not format, please repeat the command and enter correct adress, or enter next ' \
                   f'command'

    return inner


# Парсер введеных команд:
def parcer(user_input):
    command, *data = user_input.strip().lower().split(' ', 1)
    if command in command_func:
        if data:
            data = data[0].split(' ', 1)
            return command_func[command], data
        else:
            return command_func[command], data
    else:
        return f'You have entered an invalid command, please refine your query'


# функции обработчки  вводимых команд:
@input_error
def hello():  # функция приветствия
    return f'How can I help you?'


# функция добавления контакта и его данных
@input_error
def add_data():
    new_contact = {}

    name = input('Name: ')
    phone = input("Phone (add data in format '+38 number phone' or 'number phone'): ")
    birthday = input('Birthday(enter data in the format dd-mm-year): ')
    email = input('Email: ')
    address = input('Address(enter data in the format "name street" "number building" "name town"): ')

    if name.title() != '':
        new_contact['name'] = Name(name.title())
    if phone != '':
        new_contact['phones'] = [Phone(phone)]
    if birthday != '':
        new_contact['birthday'] = Birthday(birthday)
    if email != '':
        new_contact['email'] = Email(email)
    if address != '':
        new_contact['address'] = Address(address)

    for key, value in new_contact.items():
        if key == 'name':
            for cont in contacts_data:
                if new_contact[key].value == cont['name'].value:
                    return f'This contact has already exist, please, try once again\nHow can I help you?'

            contacts_data.append(new_contact)
            return f'Contact added successfully\nHow can I help you?'

    raise KeyError


@input_error
def change_phone(name, phone):  # функция для смены номера телефона
    name = Name(name.title())
    phone = Phone(phone)
    for cont in contacts_data:
        if name.value == cont['name']:
            entity = AddressBook(**cont)
            cont['phones'] = entity.edit_phone(cont['phones'], phone)
            return f'Contact updated successfully\nHow can I help you?'
    raise KeyError


@input_error
def add_name_phone(name, phone):  # функция добавления/сохранения номера телефона  контакта
    name = Name(name.title())
    new_phone = Phone(phone)
    for cont in contacts_data:
        if cont['name'] == name.value:
            entity = AddressBook(**cont)
            cont['phones'].append(entity.add_phone(new_phone))
            return f'Contact added successfully\n\nHow can I help you?'

    contacts_data.append({'name': name.value, 'phones': [new_phone]})
    return f'Contact added successfully\n\nHow can I help you?'


@input_error
def show_phone(name):  # функция для показа  номера телефона
    name = Name(name.title())
    for cont in contacts_data:
        if name.value in cont['name']:
            return f'{name.value} - {cont["phones"]}\nHow can I help you?'
    raise KeyError


@input_error
# функция для добавления дня рождения контакта
def add_birthday(name, birthday):
    name = Name(name.title())
    for cont in contacts_data:
        if cont['name'] == name.value:
            entity = AddressBook(**cont)
            cont['birthday'] = entity.add_birthday(birthday)
            return f'Contact birthday added successfully\nHow can I help you?'

    return f'Unfortunately, there is no such name here\nHow can I help you?'


@input_error
def add_email(name, email):  # функция для добавления email контакта
    name = Name(name.title())
    for cont in contacts_data:
        if cont['name'] == name.value:
            entity = AddressBook(**cont)
            cont['email'] = entity.add_email(email)
            return f'Contact email added successfully\nHow can I help you?'

    return f'Unfortunately, there is no such name here\nHow can I help you?'


@input_error
# функция для добавления адреса контакта
def add_address(name, address):
    name = Name(name.title())

    for cont in contacts_data:
        if cont['name'] == name.value:
            entity = AddressBook(**cont)
            cont['address'] = entity.add_address(address.title())
            return f'Contact address added successfully\nHow can I help you?'

    return f'Unfortunately, there is no such name here\nHow can I help you?'


@input_error
def show_contacts():  # функция для показа всех контактов
    return f'{contacts_data}\nHow can I help you?'


@input_error
def exit_program():  # функция  для окончания работы бота
    return f'Good bye!'


# функция  для сохранения данных в файл csv
def save_contacts(local_file_name, local_contacts_data):
    with open(local_file_name, 'w', newline='', encoding='utf-8') as fh:
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(local_contacts_data)
    return f'Data saved successfully\nHow can I help you?'


@input_error
# функция  для чтения  данных из  файла csv
def read_contacts(local_file_name, data):
    with open(local_file_name, 'r', newline='', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            data.append(row)
    print(contacts_data)
    return f'How can I help you?'


@input_error
# функция  для редактирования контакта
def edit_data(name):
    name = Name(name.title())

    for cont in contacts_data:
        if cont['name'] == name.value:
            entity = AddressBook(**cont)

            for field_name in field_names:
                user_input_new_value = input(f'{field_name}: ')
                if user_input_new_value:
                    cont[field_name] = entity.edit(**{field_name: user_input_new_value})

            return f'Contact {cont["name"]} edited successfully\nHow can I help you?'
    raise KeyError


@input_error
# функция  для удаления контакта
def remove_contact(name):
    name = Name(name.title())

    for cont in contacts_data:
        if cont['name'] == name.value:
            contacts_data.remove(cont)

            return f'Remove contact successfully\nHow can I help you?'
    raise KeyError


# функция  для поиска  данных в адресной книге
def search(value_search):
    found_contacts = list(filter(lambda item: value_search in item['name'].lower().strip(), contacts_data))

    if len(found_contacts) == 0:
        return f'No data in contacts\nHow can I help you?'
    else:
        return f'{found_contacts}\nHow can I help you?'


# словарь для хранения  имен функций обработчиков команд:
command_func = {'hello': hello, 'add': add_data, 'change-phone': change_phone,
                'show-phone': show_phone, 'show all': show_contacts, 'exit': exit_program,
                'save': save_contacts, 'search': search, 'birthday': add_birthday,
                'email': add_email, 'address': add_address, 'read': read_contacts, 'edit': edit_data,
                'remove-contact': remove_contact}


# главная функция:


def main():
    user_input = input(
        'Enter hello for start, or one of the commands for finish: ')

    if user_input.lower().strip() == 'hello':
        print(
            'Hi, I am a contact book helper bot!\n\nI understand these commands:\n"add name phone" - add a new contact '
            'to the book, instead of name and phone, enter the username and phone number, separated by a '
            'space.\n"change name phone" - change contact phone number, instead of name and phone, enter the username '
            'and phone number, separated by a space.\n"phone name" - show contact phone number, instead of name enter '
            'the username.\n"birthday name data" - add/change data birthday contact, instead of name and data, '
            'enter the username and birthday in format month-day-year,separated by a space.\n"email name data" - '
            'add/change email contact, instead of name and data, enter the username and email,separated by a '
            'space\n"address name data" - add/change address contact, instead of name and data, enter the username and '
            'address in format "name street" "number building" "name town",separated by a space.\n"show all" - show all'
            'contacts\n"save" - save data to file csv.\n"read" - read data from file csv.\n"search contact" - search '
            'for contacts,instead of a contact, enter a request (name / part of a name or phone number / part of a '
            'phone number).\n"hello" - for start bot.\n"good bye" or "close" or "exit" or "." - for finish '
            'bot.\n"edit" - change contact, instead of name, enter the name, phone, birthday, email and address '
            'separated by a space\n"remove-contact" - delete contact, enter the name for delete\n')

        while True:
            try:
                if user_input.lower().strip() in finish:
                    user_input_parser = parcer('exit')
                    command, arg = user_input_parser
                    print(command(*arg))
                    break
                elif user_input.lower().strip() == 'show all':
                    print(show_contacts())
                    user_input = input()
                else:
                    user_input_parser = parcer(user_input)
                    command, arg = user_input_parser
                    if command == save_contacts or command == read_contacts:
                        print(command(file_name, contacts_data))
                        user_input = input()
                    else:
                        print(command(*arg))
                        user_input = input()

            except (ValueError, TypeError):
                user_input = input(
                    f'You have entered an invalid command, please refine your query\nHow can I help you?\n')
    elif user_input.lower().strip() in finish:
        user_input_parser = parcer('exit')
        command, arg = user_input_parser
        print(command(*arg))
    else:
        main()


if __name__ == "__main__":
    main()

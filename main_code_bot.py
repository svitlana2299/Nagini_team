import csv
from my_classes import AddressBook, Name, Phone, Record, NumberPhoneError, BirthdayError, EmailError, AdressError


# список для хранения имеющихся данных у контактов
contacts_data = []

# список  имен комманд для окончания работы бота:
finish = ['good bye', 'close', 'exit', '.']

# файл csv для сохранение данных адресной книги на диск
file_name = 'contacts_data.csv'

# функция декоратор для функций обработчиков команд:


def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return f'Enter correct user name'
        except ValueError:
            return f'You have entered an invalid command, please refine your query'
        except IndexError:
            return f'Give me name and phone please'
        except NumberPhoneError:
            return f'Enter correct number phone'
        except FileNotFoundError:
            return f'Please first enter and save the data'
        except BirthdayError:
            return f'Enter correct date'
        except EmailError:
            return f'Enter correct email'
        except AdressError:
            return f'Enter correct adress'

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


@input_error
def add_phone(name, phone):  # функция добавления/сохранения номера телефона  контакта
    name = Name(name.title())
    phone = Phone(phone)
    record = Record(name.value)
    contact = AddressBook()
    record.add_phone(phone.value)
    contact.add_record(record)
    for cont in contacts_data:
        if name.value == cont['name']:
            cont['phone'].append(phone.value)
            return f'Contact added successfully\nHow can I help you?'

    contacts_data.append(contact)
    return f'Contact added successfully\nHow can I help you?'


@input_error
def change(name, phone):  # функция для смены номера телефона
    name = Name(name.title())
    phone = Phone(phone)
    for cont in contacts_data:
        if name.value == cont['name']:
            cont['phone'] = [phone.value]
            return f'Contact updated successfully\nHow can I help you?'
    raise KeyError


@input_error
def phone(name):  # функция для показа  номера телефона
    name = Name(name.title())
    for cont in contacts_data:
        if name.value in cont['name']:
            return f'{name.value} - {cont["phone"]}\nHow can I help you?'
    raise KeyError


@input_error
# функция для добавления дня рождения контакта
def add_birthday(name, birthday):
    name = Name(name.title())
    record = Record(name.value)
    record.add_birthday(birthday)
    contact = AddressBook()
    contact.add_record(record)
    for cont in contacts_data:
        if name.value == cont['name']:
            cont['birthday'] = birthday
            return f'Contact birthday added successfully\nHow can I help you?'

    contacts_data.append(contact)
    return f'Contact birthday added successfully\nHow can I help you?'


@input_error
def add_email(name, email):  # функция для добавления email контакта
    name = Name(name.title())
    record = Record(name.value)
    record.add_email(email)
    contact = AddressBook()
    contact.add_record(record)
    for cont in contacts_data:
        if name.value == cont['name']:
            cont['email'] = email
            return f'Contact email added successfully\nHow can I help you?'

    contacts_data.append(contact)
    return f'Contact email added successfully\nHow can I help you?'


@input_error
# функция для добавления адреса контакта
def add_adress(name, adress):
    name = Name(name.title())
    record = Record(name.value)
    record.add_adress(adress.title())
    contact = AddressBook()
    contact.add_record(record)
    for cont in contacts_data:
        if name.value == cont['name']:
            cont['adress'] = adress.title()
            return f'Contact adress added successfully\nHow can I help you?'

    contacts_data.append(contact)
    return f'Contact adress added successfully\nHow can I help you?'


@input_error
def show_all():  # функция для показа всех контактов
    return f'{contacts_data}\nHow can I help you?'


@input_error
def exit():  # функция  для окончания работы бота
    return f'Good bye!'


# функция  для сохранения данных в файл csv
def save_contacts(file_name, contacts_data):
    with open(file_name, 'w', newline='', encoding='utf-8') as fh:
        field_names = ['name', 'phone', 'birthday', 'email', 'adress']
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(contacts_data)
    return f'Data saved successfully\nHow can I help you?'


@input_error
# функция  для чтения  данных из  файла csv
def read_contacts(file_name, data):
    with open(file_name, 'r', newline='', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            data.append(row)
    print(contacts_data)
    return f'How can I help you?'


def search(search):  # функция  для поиска  данных в адресной книге
    found_contacts = []
    for cont in contacts_data:
        if cont.search_contacts(search) == 'No data in contacts\nHow can I help you?':
            continue
        elif cont.search_contacts(search) == 'Enter correct data':
            return f'Enter correct data'
        else:
            found_contacts.append(cont)
    if len(found_contacts) == 0:
        return f'No data in contacts\nHow can I help you?'
    else:
        return f'{found_contacts}\nHow can I help you?'


# словарь для хранения  имен функций обработчиков команд:
command_func = {'hello': hello, 'add': add_phone, 'change': change,
                'phone': phone, 'show all': show_all, 'exit': exit,
                'save': save_contacts, 'search': search, 'birthday': add_birthday,
                'email': add_email, 'adress': add_adress, 'read': read_contacts}

# главная функция:


def main():
    print('Hi, I am a contact book helper bot!\n\nI understand these commands:\n"add name phone" - add a new contact to the book, instead of name and phone, enter the username and phone number, separated by a space.\n"change name phone" - change contact phone number, instead of name and phone, enter the username and phone number, separated by a space.\n"phone name" - show contact phone number, instead of name enter the username.\n"birthday name data" - add/change data birthday contact, instead of name and data, enter the username and birthday in format month-day-year,separated by a space.\n"email name data" - add/change email contact, instead of name and data, enter the username and email,separated by a space\n"adress name data" - add/change adress contact, instead of name and data, enter the username and adress in format "name street" "number building" "name town",separated by a space.\n"show all" - show all contacts\n"save" - save data to file csv.\n"read" - read data from file csv.\n"search contact" - search for contacts,instead of a contact, enter a request (name / part of a name or phone number / part of a phone number).\n"hello" - for start bot.\n"good bye" or "close" or "exit" or "." - for finish bot.\n')

    user_input = input(
        'Enter hello for start, or one of the commands for finish: ')
    if user_input.lower().strip() == 'hello':
        while True:
            try:
                if user_input.lower() in finish:
                    user_input_parser = parcer('exit')
                    command, arg = user_input_parser
                    print(command(*arg))
                    break
                elif user_input.lower().strip() == 'show all':
                    print(show_all())
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

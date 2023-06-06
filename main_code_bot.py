import csv
from datetime import datetime, timedelta
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
            return f'There is no such name in contacts. Please, add the contact with this name first or enter correct ' \
                   f'name'
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
            return f'Invalid birthday date. Please, put the date in format dd-mm-yyyy'
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
def add_name_phone(name, phone):  # функция добавления/сохранения номера телефона  контакта
    name = Name(name.title())
    for cont in contacts_data:
        if cont['name'] == name.value:
            item = {}
            for key, data in cont.items():
                print(key, type(data) == list, data)
                item[key] = map(lambda x: str(x.value), data) if type(data) == list else data.value

            entity = AddressBook(**item)
            cont['phones'].append(entity.add_phone(phone))
            return f'Contact added successfully\n\nHow can I help you?'

    contacts_data.append({'name': name, 'phones': [Phone(str(phone))]})
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
            item = {}
            for key, data in cont.items():
                print(key, type(data) == list, data)
                item[key] = map(lambda x: str(x.value), data) if type(data) == list else data.value

            entity = AddressBook(**item)
            cont['birthday'] = entity.add_birthday(birthday)
            return f'Contact birthday added successfully\nHow can I help you?'

    return f'Unfortunately, there is no such name here\nHow can I help you?'


@input_error
def add_email(name, email):  # функция для добавления email контакта
    name = Name(name.title())
    for cont in contacts_data:
        if cont['name'] == name.value:
            item = {}
            for key, data in cont.items():
                print(key, type(data) == list, data)
                item[key] = map(lambda x: str(x.value), data) if type(data) == list else data.value

            entity = AddressBook(**item)
            cont['email'] = entity.add_email(email)
            return f'Contact email added successfully\nHow can I help you?'

    return f'Unfortunately, there is no such name here\nHow can I help you?'


@input_error
# функция для добавления адреса контакта
def add_address(name, address):
    name = Name(name.title())

    for cont in contacts_data:
        if cont['name'] == name.value:
            item = {}
            for key, data in cont.items():
                print(key, type(data) == list, data)
                item[key] = map(lambda x: str(x.value), data) if type(data) == list else data.value

            entity = AddressBook(**item)
            cont['address'] = entity.add_address(address.title())
            return f'Contact address added successfully\nHow can I help you?'

    return f'Unfortunately, there is no such name here\nHow can I help you?'


@input_error
def show_contacts():  # функция для показа всех контактов
    if len(contacts_data) > 0:
        print('-----------------------------------------------------------')
        for cont in contacts_data:
            for key, value in cont.items():
                print(f'{key}: {value}')
            print('-----------------------------------------------------------')
    else:
        print('There are no records')
    return f'How can I help you?\n'


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
    with open(local_file_name, 'r', newline='', encoding='utf-8') as file_obj:
        reader = csv.DictReader(file_obj)
        for row in list(reader):
            row['phones'] = [str(x) for x in eval(row['phones'].replace('[', "['").replace(', ', "','").replace(']', "']"))] if row['phones'] else []
            entity = AddressBook(**row)
            new_data = entity.get_contact()
            unique_identifier = new_data['name'].value

            if not any(contact['name'].value == unique_identifier for contact in data):
                data.append(new_data)

    print('-----------------------------------------------------------')
    for cont in data:
        for key, value in cont.items():
            print(f'{key}: {value}')
        print('-----------------------------------------------------------')
    return f'How can I help you?'

@input_error
# функция  для редактирования контакта
def edit_data(name):
    name = Name(name.title())

    for cont in contacts_data:
        if cont['name'].value == name.value:
            item = {}
            for key, data in cont.items():
                item[key] = map(lambda x: str(x.value), data) if type(data) == list else data.value

            entity = AddressBook(**item)

            for field_name in field_names:
                if 'phones' == field_name:
                    if 'phones' in cont.keys() and len(cont['phones']):
                        print('At the moment you have several phones.\n')
                        for phone in cont['phones']:
                            print(f'{phone}\n')
                        print('Choose which one you want to change.\n')
                        print('To change, specify the data in the format "[OldPhone] [NewPhone]".\n')
                        print('if you add a new phone the data in the format "[NewPhone]".\n')
                        print('If you do not want to change the phone then just press ENTER".\n')

                        user_input_new_value = input(f'{field_name}: ')

                        if user_input_new_value:
                            data_phone = user_input_new_value.strip().lower().split(' ', 1)

                            if len(data_phone) == 2:
                                cont[field_name] = entity.edit_phone(**{'old_phone': data_phone[0], 'new_phone': data_phone[1]})
                            else:
                                cont[field_name] = entity.add_phone(data_phone[0])
                    else:
                        user_input_new_value = input(f'{field_name}: ')
                        if user_input_new_value:
                            cont[field_name] = entity.edit(**{field_name: [user_input_new_value]})
                else:
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
        if cont['name'].value == name.value:
            contacts_data.remove(cont)

            return f'Remove contact successfully\nHow can I help you?'
    raise KeyError


# функция  для поиска  данных в адресной книге
def search(value_search):
    found_contacts = list(filter(lambda item: value_search.lower().strip() in item['name'].value.lower().strip(), contacts_data))

    if len(found_contacts) == 0:
        return f'No data in contacts\nHow can I help you?'
    else:
        print('-----------------------------------------------------------')
        for cont in found_contacts:
            for key, value in cont.items():
                print(f'{key}: {value}')
            print('-----------------------------------------------------------')

        return f'How can I help you?\n'

# Конвертация дат в datetime объекты
def convert_dates(contacts_data):
    new_contacts_data = []
    for contact in contacts_data:
        birthday = str(contact['birthday'])
        day,month, year = map(int, birthday.split('-'))
        date_object = datetime(year, month, day)
        new_contact = {'name': contact['name'], 'birthday': date_object}
        new_contacts_data.append(new_contact)
    return new_contacts_data

# Функция вывода списка дней рождений через заданное число дней
def upcoming_birthdays(days):
    # days = int(days)
    new_contacts_data = convert_dates(contacts_data)

    today = datetime.now().date()
    target_date = today + timedelta(days=int(days))
    upcoming_birthdays_list = [
        str(contact['name'])
        for contact in new_contacts_data
        if (contact['birthday'].month, contact['birthday'].day) == (target_date.month, target_date.day)
    ]
    if len(upcoming_birthdays_list) == 0:
        return 'There are no birthdays that day'
    else:
        return 'List of birthdays: ' + ', '.join(upcoming_birthdays_list)


# словарь для хранения  имен функций обработчиков команд:
command_func = {'hello': hello, 'add': add_data, 'show-phone': show_phone,
                'show all': show_contacts, 'exit': exit_program,
                'save': save_contacts, 'search': search, 'birthday': add_birthday,
                'email': add_email, 'address': add_address, 'read': read_contacts,
                'edit': edit_data, 'remove-contact': remove_contact, 'birthday-list': upcoming_birthdays}


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
            'separated by a space\n"remove-contact" - delete contact, enter the name for delete '
            '\n"birthday-list number" -  show a list of birthdays after a given number of days.\n')
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

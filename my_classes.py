from collections import UserDict
from datetime import datetime
import re


class NumberPhoneError(Exception):
    pass


class BirthdayError(Exception):
    pass


class EmailError(Exception):
    pass


class AdressError(Exception):
    pass


class Field:
    def __init__(self, value):
        self.value = value
        self.__private_value = None


class Name(Field):

    @property
    def value(self):
        return self.__private_value

    @value.setter
    def value(self, new_value):
        if new_value.isalpha():
            self.__private_value = new_value
        else:
            raise KeyError('Enter correct user name')

    def __repr__(self):
        return f'{self.value}'


class Phone(Field):

    @property
    def value(self):
        return self.__private_value

    @value.setter
    def value(self, new_value):
        if (''.join(new_value.split())).isdigit() or (new_value[0] == '+' and (''.join(new_value.split()))[1:].isdigit()):
            self.__private_value = (''.join(new_value.split()))
        else:
            raise NumberPhoneError('Enter correct number phone')

    def __repr__(self):
        return f'{self.value}'


class Birthday:
    def __init__(self, birthday=False):
        self.__private_birthday = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__private_birthday

    @birthday.setter
    def birthday(self, new_birthday):
        try:
            if datetime.strptime(str(new_birthday), '%d-%m-%Y'):
                self.__private_birthday = new_birthday
        except ValueError:
            raise BirthdayError('Enter correct date')

    def __repr__(self):
        return f'{self.birthday}'

    def __bool__(self):
        return self.birthday != False


class Email:
    def __init__(self, email=''):
        self.__private_email = None
        self.email = email

    @property
    def email(self):
        return self.__private_email

    @email.setter
    def email(self, new_email):
        try:
            mail = bool(
                re.search(r"[a-zA-Z]+[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", new_email))
            if mail:
                self.__private_email = new_email
            else:
                raise EmailError('Enter correct email')
        except ValueError:
            raise EmailError('Enter correct email')

    def __repr__(self):
        return f'{self.email}'


class Adress:
    def __init__(self, adress=''):
        self.__private_adress = None
        self.adress = adress

    @property
    def adress(self):
        return self.__private_adress

    @adress.setter
    def adress(self, new_adress):
        try:
            adr = bool(
                re.search(r'^[A-Za-z0-9\s.,-]+ \d+[A-Za-z]* [A-Za-z\s]+$', new_adress))
            if adr:
                self.__private_adress = new_adress
            else:
                raise AdressError('Enter correct adress')
        except ValueError:
            raise AdressError('Enter correct adress')

    def __repr__(self):
        return f'{self.adress}'


class Record:
    def __init__(self, name, birthday='', email='', adress=''):
        self.name = Name(name)
        self.phones = []
        self.birthday = birthday
        self.email = email
        self.adress = adress

    def __repr__(self):
        return f'{self.name}, {self.birthday}'

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def delete_phone(self, phone: Phone):
        for p in self.phones:
            if str(p) == phone:
                self.phones.remove(p)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        for p in self.phones:
            if str(p) == old_phone:
                self.phones[self.phones.index(p)] = new_phone

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_email(self, email):
        self.email = Email(email)

    def add_adress(self, adress):
        self.adress = Adress(adress)

    def days_to_birthday(self):
        if self.birthday:
            current_date = datetime.now()
            data_birthday = datetime.strptime(str(self.birthday), '%d-%m-%Y')
            current_data_birthday = data_birthday.replace(
                year=current_date.year)
            if current_data_birthday < current_date:
                next_birthday = data_birthday.replace(
                    year=(current_date.year + 1))
                result = next_birthday - current_date
            else:
                result = current_data_birthday - current_date

            return result.days


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data = {'name': record.name.value,
                     'phone': record.phones, 'birthday': record.birthday,
                     'email': record.email, 'adress': record.adress}

    def iterator(self, n=1):
        items = list(self.data.items())
        for i in range(0, len(items), n):
            yield items[i:i+n]

    def search_contacts(self, search):
        found_contacts = []
        for val in self.data.values():
            if type(val) is list:
                if search in (','.join(val)):
                    found_contacts.append(self.data)
                    break
            elif search in ('.,@!?+-;:='):
                return f'Enter correct data'
            else:
                if search.lower() in str(val).lower():
                    found_contacts.append(self.data)
                    break
        if len(found_contacts) == 0:
            return f'No data in contacts\nHow can I help you?'
        else:
            return f'{found_contacts}\nHow can I help you?'


        ddddddddcs
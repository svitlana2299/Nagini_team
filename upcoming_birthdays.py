#Код для виведення списків контактів, у яких день народження через задану кількість днів від поточної дати


#Для роботи модулю потрібно:
#Додати в main_code_bot.py в command_func: {'birthdaylist':upcoming_birthdays}
#Додати в main_code_bot.py  def main(): print(\n "birthdaylist number" -  show a list of birthdays after a given number of days.)


from datetime import datetime, timedelta

def convert_dates(contacts_data):
    new_contacts_data = []
    for contact in contacts_data:
        birthday = contact['birthday']
        month, day, year = map(int, birthday.split('-'))
        date_object = datetime(year, month, day)
        new_contact = {'name': contact['name'], 'birthday': date_object}
        new_contacts_data.append(new_contact)
    return new_contacts_data

def upcoming_birthdays(days):
    days = int(days)
    new_contacts_data = convert_dates(contacts_data)

    today = datetime.now().date()
    target_date = today + timedelta(days=days)

    upcoming_birthdays_list = [
        contact['name']
        for contact in new_contacts_data
        if (contact['birthday'].month, contact['birthday'].day) == (target_date.month, target_date.day)
    ]
    if len(upcoming_birthdays_list) == 0:
        return 'There are no birthdays that day'
    else:
        return 'List of birthdays: ' + ', '.join(upcoming_birthdays_list)


from main_code_bot import main, command_func

func_list = ['contact book', 'notebook', 'sort', 'help', 'exit']
windows = r"Windows: C:\Users\Username\Documents\My_Folder"
macOS = r"macOS: /Users/Username/Documents/My_folder"
Linux = r"Linux: /home/Username/Documents/My_folder"

def main_help():
    print(f"\nThe personal assistant console program can implement the following functionality:\n1) A contact book that can:\n- save contacts with names, addresses, phone numbers, email, and birthdays to the contacts book;\n- display a list of contacts whose birthday is a specified number of days from the current date;\n- check the correctness of the entered phone number and email when creating or editing a record and notify the user in case of incorrect entry;\n- search for contacts among book contacts;\n- edit and delete entries from the contact book;\nTo switch to the contact book functionality, please enter 'Сontact book'\n\n2) Notebook that can:\n- save notes with text information;\n- search for notes;\n- edit and delete notes;\n- add 'tags' to notes, keywords describing the subject and subject of the record;\nsearch and sort notes by keywords (tags);\nTo switch to the Notebook functionality, please enter 'Notes'\n\n3) Sort, which can sort files in the specified folder by categories (images, documents, videos, etc.).\nTo switch to the Sort function, please enter 'Sort'\n\nTo exit the Assistant bot, enter 'Exit'\n")

def contact_book():
    print(f"I am a contact book helper bot!\nI can:\n- Save contacts in Сontact book with names, addresses, phone numbers, email and birthdays (to access this function, please enter 'Add')\n- Display a list of contacts whose birthday is a specified number of days from the current date (to use this function, please enter '???')\n- Search for contacts among contacts in the book (to use this function, please enter 'Search'\n- Edit entries from the contact book (to use this function, please enter 'Edit');\n- Delete entries from the contact book (to use this function, please enter 'Delete')\n- Save contacts to a file (to use this function, please enter 'Save')\n- View contacts saved in the file (to use this function, please enter 'Read')\n\nI also check the correctness of the entered phone number and email when creating or editing a record and notify you in case of an incorrect entry\nFor more detailed information, enter 'Help' or 'Exit' to return to the main menu") 

def contact_book_help():
    print(f"\nThe contact book can implement the following functionality:\n\n'Add' - adds contact book with names, addresses, phone numbers, email, and birthdays. In order to save the contact, click Add and enter all the necessary information, the required field is Name - this is a unique property of the contact. Also, in the Add function, a check for the adds connput parameters such as Phone number and Email is implemented.\n\nThe contact book has the ability to save contacts' birthdays:\n\n'???' -  display a list of contacts whose birthday is a specified number of days from the current date\n\nWork with the list of contacts is implemented using advanced functions:\n\n'Search' - search for contacts among contacts in the book;\n'Edit'- edit entries from the contact book;\n'Delete' - delete entries from the contact book;\n'Save' - save contacts to a file (.csv file format).\n\nEnter the command you need from the list above.\nReturn to the main menu, enter 'Exit'")

def notebook():
    print(f"I am a notebook helper bot!\nI can:\n- Save notes with text information and keywords (tags) (to access this function, please enter'Add')\n- Search for notes (to use this function, please enter 'Search')\n- Edit notes (to use this function, please enter 'Edit')\n- Delete notes (to use this function, please enter 'Delete')\n- Search and sort notes by keywords (tags) (to use this function, please enter 'Search by tags')\n- Delete notes by keywords (tags) (to use this function, please enter 'Delete by tags')\nFor more detailed information, enter 'Help'")

def notebook_help():
    print(f"\nThe notebook has the following list of functions, it can store notes with text information, search for notes, edit and delete notes, it is also possible to add 'tags' to notes, keywords describing the topic and subject of the record, search and sort notes by keywords (tags).\n\nThe list of commands is as follows:\n'Add' - save notes with text information and keywords (tags);\n'Search' - search for notes;\n'Edit' - edit notes;\n'Delete' - delete notes;\n'Search by tags' - search and sort notes by keywords (tags);\n'Delete by tags' - delete notes by keywords (tags).\nEnter the command you need from the list above.\nReturn to the main menu, enter 'Exit'")

def sort():
    print(f'I am a sort of helper bot!\n\nI can:\n- Sort files in the specified folder by category (to use this function, please enter "Sort folder path")\n Folder path for different OS:\n{windows}\n{macOS}\n{Linux}')

def start_bot():
    user_input = input("Hello, I'm a personal assistant console bot, to get started, use, please enter 'Hello': ")
    if user_input.lower().strip() == 'hello':
        user_input = input("\nI can help with the following tasks\n\n- Maintain your personal contact book (to access this function, please enter 'Сontact book')\n\n- Enter any of your test notes (to access this function, please enter 'Notebook')\n\n- Sort files in the specified folder by category (to access this function, please enter 'Sort')\n\nFor more detailed information, enter 'Help'\nFor finish bot, enter 'Exit'\n\nPlease select a task: ")
        while True:
            if user_input.lower().strip() == 'help':
                main_help()
                user_input = input("Hi, this main menu bot, please enter your choice or 'help' to see my options: ")

            if user_input.lower().strip() == 'contact book':
                contact_book()
                while True:
                    user_input = input("This menu contact_ book, please enter your choice or 'help' to view a list of commands or 'exit' for return to the main menu: ")
                    if user_input.lower().strip() == 'help':
                        while user_input == 'help':
                            contact_book_help()
                            user_input = input("Please enter your choice or 'help' to view a list of commands: ")
                    if user_input.lower().strip() == 'exit':
                        break
                    if user_input in command_func:
                        main(user_input)
                    if user_input:
                        continue
                user_input = input("Hi, this main menu bot, please enter your choice or 'help' to see my options: ")
                   
            if user_input.lower().strip() == 'notebook':
                notebook()
                while True:
                    user_input = input("This menu notebook, please enter your choice or 'help' to view a list of commands or 'exit' for return to the main menu: ")
                    if user_input.lower().strip() == 'help':
                        while user_input == 'help':
                            notebook_help()
                            user_input = input("Please enter your choice or 'help' to view a list of commands: ")
                    if user_input.lower().strip() == 'exit':
                        break
                    if user_input in command_func:
                        main(user_input)
                    if user_input:
                        continue
                user_input = input("Hi, this main menu bot, please enter your choice or 'help' to see my options: ")

            if user_input.lower().strip() == 'sort':
                sort()
                while True:
                    user_input = input("This menu notebook, please enter commands 'sort' or 'exit' for return to the main menu: ")
                    if user_input.lower().strip() == 'exit':
                        break
                    if user_input in command_func:
                        main(user_input)
                    if user_input:
                        continue
                user_input = input("Hi, this main menu bot, please enter your choice or 'help' to see my options: ")
            
            if user_input.lower().strip() == 'exit':
                print(f'Good bye!')
                break
            if user_input.lower().strip() in func_list:
                continue
            else:
                user_input = input("Hi, this main menu bot, please enter your choice or 'help' to see my options: ")
    else:
        start_bot()

start_bot()
    
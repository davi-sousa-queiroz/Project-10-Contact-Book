#Contact Book

import time

import random

contacts = {}

def welcome():
    print('Welcome to Contact Book 📖')
    time.sleep(1)
    print('')

def main_menu():
    print('')
    print("1. Add to contacts ")
    print("2. Remove contact ")
    print("3. View contacts ")
    print("4. Search for contact ")
    print("5. Exit")
    print('6. Generate random phone number')

def add_contact(name, phone):
    contacts[name] = phone

    print('')

    print("Contact added!")

def view_contacts():
    if contacts:
        for name in contacts:
            print(f'{name}: {contacts[name]}')
    else:
        print('No contacts to show.')

def search_contact():
    name = input('Enter contact name: ')
    print('')
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print('Contact not found')

def remove_contact():

    view_contacts()
    print('')
    removal = input('Enter contact name: ')
    if removal in contacts:
        contacts.pop(removal)
        print('')
        print('Contact removed')

    else:
        print('Contact not found')

def random_contact():
    area = random.randint(200,999)
    prefix = random.randint(1,999)
    line = random.randint(1000,9999)
    random_num = f"{area}-{prefix}-{line}"
    print(random_num)

def main():
    welcome()
    while True:
        main_menu()
        print('')
        time.sleep(1)
        choice = input('Enter your choice: ')
        print('')
        if choice == '1':
            add_contact(input('Enter contact name: '), input('Enter contact phone number: '))
        elif choice == '2':
             remove_contact()
        elif choice == '3':
            view_contacts()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            print('Thank you for using Contact Book! 📕')
            break
        elif choice == '6':
            random_contact()
        else:
            print('Please enter a valid choice, 1-5.')

if __name__ == '__main__':
    main()
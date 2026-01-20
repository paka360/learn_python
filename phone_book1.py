# Contact Book
import json
import os


contacts = {
    'stephen':{
        'phone_number':'1',
        'email': 'st@gmail.com'
    },
    'john':{
        'phone_number': '2',
        'email': 'jh@gmail.com'
    },
    'ella':{
        'phone_number':'3',
        'email': 'el@gmail.com',
    },
}


def add_contact():
    """Allows users to add contacts"""

    name = input('Please enter a name: ')
    if not name.strip():
        print("Cannot be empty.")
        return


    phone_number = input("Please enter a contact number: ")
    if not phone_number.isdigit() or len(phone_number) < 9:
        print("Invalid phone number!")
        return

    email = input("Please enter an email: ")

    
    strnumber = {}
    strnumber['phone_number'] = phone_number 
    strnumber['email'] = email

    contacts[name] = strnumber
    
    print("COntact added successfully.")



def view_contacts():
    """Allows users to view contact."""

    for key, value in contacts.items():
        print('name: ' + key.title())
    
        print('phone number: ' + value['phone_number'])
        print('Email: ' + value['email'])
        

def search_contact():
    """Allows users to search for contacts"""
    prompt = input("Please enter the name you wish to search for: ")
    prompt = prompt.lower()

    if prompt in contacts:
        print( 'Contact Found!')
        print(prompt.title())
        print(contacts[prompt] )
    else:
        print("No results found.")


def delete_contact():
    """Allows users to delete contact"""

    prompt1 = input("Enter the name of tha contact you wish to delete. ")
    prompt1 = prompt1.lower()
    

    if prompt1 in contacts:
        confirm = input("Are you sure you wish to delete this contact? Enter Yes/No. ")
        confirm = confirm.lower()

        if confirm == 'yes':
            del contacts[prompt1]
            print("Contact deleted successfully.")
        else:
            print('Contact retained.')
    else:
        print("No results found.")
    


while True:
    print("Welcome to the Phonebook.")
    prompt2 = input("Which action would you like to perform?\n" 
    "1. Add a new contact.\n" 
    "2. View all contacts.\n" 
    "3. Search for a contact.\n" 
    "4. Delete a contact.\n" 
    "5. Quit the program.\n")

    if prompt2 == '1':
        add_contact()
    elif prompt2 == '2':
        view_contacts()
    elif prompt2 =='3':
        search_contact()
    elif prompt2 =='4':
        delete_contact()
    elif prompt2 == '5':
        break
    else:
        print("Invalid input! Try again.")
        continue

filename = "contacts.json"
try:
    with open(filename, "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)


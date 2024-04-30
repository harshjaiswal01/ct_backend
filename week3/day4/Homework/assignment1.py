# User Interface (UI):
# Create a user-friendly command-line interface (CLI) for the Contact Management System.
# Display a welcoming message and provide a menu with the following options:
# Welcome to the Contact Management System! 
# Menu:
# Add a new contact
# Edit an existing contact
# Delete a contact
# Search for a contact
# Display all contacts
# Export contacts to a text file
# Import contacts from a text file
# Quit 
# > 
import re
# contact = {email : {"Name":name, "Phone Number":phone, "Address":address, "Notes":notes, "Friends":friends, "Family":family, "work":work}}

contact = {}

def email_check_again(email, contacts):
    while True:
        try:
            email_check = re.search(r'[\w._-]+@[\w._-]+\.[a-z]{2,3}', email)
            # print(email_check)
            if str(email_check) == 'None':
                # print("Wrong Email")
                raise ValueError ("Wrong Email")
            else:
                # print("Correct Email")
                for contact in contacts:
                    if contact == email:
                        print("This email is already in the system. Please try again")
                        raise ValueError ("Already")
                else:
                    return email
                    break
        except ValueError as ve:
            if "Wrong Email" in str(ve):
                email = input("Please enter email again in correct format: ").lower()
            if "Already" in str(ve):
                email = input("Please enter email again which is not already in the system: ").lower()
            
def phone_check_again(phone):
    while True:
        try:
            phone_check = re.search(r'[(]?\d{3}[)]?[-|\s]?\d{3}[-|\s]?\d{4}', phone)
            if str(phone_check) == 'None':
                # print("Wrong Email")
                raise ValueError ("Wrong Phone")
            else:
                return phone
                break
        except ValueError as ve:
            if "Wrong Phone" in str(ve):
                phone = input("Please enter phone number again in correct format(XXX-XXX-XXXX or (XXX)XXX-XXXX or XXXXXXXXXX): ")

def name_check(name):
    while True:
        try:
            name_match = re.search(r"[A-Z]\w*\s[A-Z]*\w*\s*[A-Z]\w+", name)
            # [A-Z]*\w*\s*[A-Z]\w*
            # print(name_match)
            # print(name)
            if str(name_match) == 'None':
                # print("Wrong Name")
                raise ValueError ("Wrong Name")
            else:
                return name
                break
        except ValueError as ve:
            if "Wrong Name" in str(ve):
                name = input("Please enter name again in correct format(First(Required) Middle(optional) Last(Required)): ").title()

def friends_category_check(friend):
    while True:
        try:
            if friend == 'yes' or friend == 'no':
                return friend
            else:
                raise ValueError ("Wrong")
        except ValueError as ve:
            if "Wrong" in str(ve):
                print("\nPlease enter either a Yes or No!")
                friend = input("Does the contact belong to Friends Category? Yes or No?: ").lower()

def family_category_check(friend):
    while True:
        try:
            if friend == 'yes' or friend == 'no':
                return friend
            else:
                raise ValueError ("Wrong")
        except ValueError as ve:
            if "Wrong" in str(ve):
                print("\nPlease enter either a Yes or No!")
                friend = input("Does the contact belong to Family Category? Yes or No?: ").lower()

def work_category_check(friend):
    while True:
        try:
            if friend == 'yes' or friend == 'no':
                return friend
            else:
                raise ValueError ("Wrong")
        except ValueError as ve:
            if "Wrong" in str(ve):
                print("\nPlease enter either a Yes or No!")
                friend = input("Does the contact belong to Work Category? Yes or No?: ").lower()

def add_new_contact():
    print("\nPlease enter the following details:-")
    email = input("Email(Required): ").lower()
    correct_email = email_check_again(email, contact)     
    name = input("Name(Required): ").title()
    correct_name = name_check(name)
    phone = input("Phone Number(XXX-XXX-XXXX or (XXX)XXX-XXXX or XXXXXXXXXX)(Required): ")
    correct_phone = phone_check_again(phone)
    address = input("Address(Optional): ")
    notes = input("Notes(Optional): ")
    friends = input("Does the contact belong to Friends Category? Yes or No?: ").lower()
    friends_check = friends_category_check(friends)
    family = input("Does the contact belong to Family Category? Yes or No?: ").lower()
    family_check = family_category_check(family)
    work = input("Does the contact belong to work Category? Yes or No?: ").lower()
    work_check = work_category_check(work)
    contact_new = {correct_email : {"Name":correct_name, "Phone Number":correct_phone, "Address":address, "Notes":notes, "Friends":friends_check, "Family":family_check, "Work":work_check}}
    contact.update(contact_new)
    # print(contact)
    # update_file(contact)
    return contact


def update_file(contacts):
    with open('contacts.txt', 'w') as file:
        for email, info in contacts.items():
            file.write(f'{email}-:-{info['Name']}-:-{info['Phone Number']}-:-{info['Address']}-:-{info['Notes']}-:-{info['Friends']}-:-{info['Family']}-:-{info['Work']}\n')

def open_file():
    contact = {}
    with open('contacts.txt', 'r') as file:
        contact_new = {}
        for line in file:
            email, name, phone, address, notes, friends, family, work = line.strip().split('-:-')
            contact_new[email] = {"Name":name, "Phone Number":phone, "Address":address, "Notes":notes, "Friends":friends, "Family":family, "Work":work}
            contact.update(contact_new)
    return contact



def edit_contact(contacts):
    # print(contacts)
    email = input("Please enter the email address of the contact: ").lower()
    c = 0
    for contact1 in contacts:
        if email == contact1:
            print("Email Found")
            print(f'''
                  What would you like to change for this contact? Please see the details below:-
                    1. Name : {contacts[contact1]['Name']}
                    2. Phone Number: {contacts[contact1]['Phone Number']}
                    3. Address: {contacts[contact1]['Address']}
                    4. Notes: {contacts[contact1]['Notes']}
                    5. Friend Category: {contacts[contact1]['Friends']}
                    6. Family Category: {contacts[contact1]['Family']}
                    7. Work Category: {contacts[contact1]['Work']}
                  ''')
            c = 1
    if c == 1:
        selection = int(input("Please enter your selection 1-7 or 8 to change everything or 9 to cancel: "))
        if selection == 9:
            pass
        elif selection == 1:
            new_name = input("Please enter new Name: ").title()
            correct_name = name_check(new_name)
            contacts[email]['Name'] = correct_name
            return contacts
        elif selection == 2:
            new_number = input("Please enter new Phone Number: ")
            correct_phone = phone_check_again(new_number)
            contacts[email]['Phone Number'] = correct_phone
            return contacts
        elif selection == 3:
            new_address = input("Please enter new Address: ")
            contacts[email]['Address'] = new_address
            return contacts
        elif selection == 4:
            new_notes = input("Please enter new Notes: ")
            contacts[email]['Notes'] = new_notes
            return contacts
        elif selection == 5:
            friend = input("Does this contact belong to the Friends Category? Yes or No?: ")
            new_friend = friends_category_check(friend)
            contacts[email]['Friends'] = new_friend
            return contacts
        elif selection == 6:
            family = input("Does this contact belong to the Family Category? Yes or No?: ")
            new_family = family_category_check(family)
            contacts[email]['Family'] = new_family
            return contacts
        elif selection == 7:
            work = input("Does this contact belong to the Work Category? Yes or No?: ")
            new_work = work_category_check(work)
            contacts[email]['Work'] = new_work
            return contacts
        elif selection == 8:
            new_name = input("Please enter new Name: ").capitalize()
            correct_name = name_check(new_name)
            contacts[email]['Name'] = correct_name
            new_number = input("Please enter new Phone Number: ")
            correct_phone = phone_check_again(new_number)
            contacts[email]['Phone Number'] = correct_phone
            new_address = input("Please enter new Address: ")
            contacts[email]['Address'] = new_address
            new_notes = input("Please enter new Notes: ")
            contacts[email]['Notes'] = new_notes
            friend = input("Does this contact belong to the Friends Category? Yes or No?: ")
            new_friend = friends_category_check(friend)
            contacts[email]['Friends'] = new_friend
            family = input("Does this contact belong to the Family Category? Yes or No?: ")
            new_family = family_category_check(family)
            contacts[email]['Family'] = new_family
            work = input("Does this contact belong to the Work Category? Yes or No?: ")
            new_work = work_category_check(work)
            contacts[email]['Work'] = new_work
            return contacts
    else:
        print("Contact not found in the System. Please try Again!")
        return contacts
    
def email_check_again_2(email, contacts):
    while True:
        try:
            email_check = re.search(r'[\w._-]+@[\w._-]+\.[a-z]{2,3}', email)
            # print(email_check)
            if str(email_check) == 'None':
                raise ValueError ("Wrong Email")
            else:
                return email
                break
        except ValueError as ve:
            if "Wrong Email" in str(ve):
                email = input("Please enter email again in correct format: ").lower()


def delete_contact(contacts):
    email = input("Please enter the email address of the contact to delete: ").lower()
    new_email = email_check_again_2(email, contacts)
    print(new_email)
    try:
        if contacts[new_email]:
            contacts.pop(new_email)
            print('Email Found. Deleting...Done')
            return contacts
        else:
            raise KeyError ("Not found")
            print('Email not found. Please try again!!!')
            return contacts
    except KeyError:
        print("Email not found")
        return contacts

def search_contact(contacts):
    c = 0
    email = input("Please enter the email address of the contact you want to search for: ").lower()
    for contact1 in contacts:
        if email == contact1:
            print("Email Found")
            print(f'''
                  Please find the contact's details below:-
                    1. Name : {contacts[contact1]['Name']}
                    2. Phone Number: {contacts[contact1]['Phone Number']}
                    3. Address: {contacts[contact1]['Address']}
                    4. Notes: {contacts[contact1]['Notes']}
                    5. Friend Category: {contacts[contact1]['Friends']}
                    6. Family Category: {contacts[contact1]['Family']}
                    7. Work Category: {contacts[contact1]['Work']}
                  ''')
            c = 1
    if c == 1:
        pass
    else:
        print("Contact not found!!! Please try again!")

def display_contact(contacts):
    i = 1
    for contact in contacts:
        print(f'{i}. Email: {contact}, Name: {contacts[contact]['Name']}, Phone Number: {contacts[contact]['Phone Number']}, Address: {contacts[contact]['Address']}, Notes: {contacts[contact]['Notes']}, Friends: {contacts[contact]['Friends']}, Family: {contacts[contact]['Family']}, Work: {contacts[contact]['Work']}')
        i += 1

def display_contact_category(contacts):
    i = 1
    print("\nFriends Category Contacts:-")
    for contact in contacts:
        if contacts[contact]['Friends'] == 'yes':
            print(f'{i}. Email: {contact}, Name: {contacts[contact]['Name']}, Phone Number: {contacts[contact]['Phone Number']}, Address: {contacts[contact]['Address']}, Notes: {contacts[contact]['Notes']}')
            i += 1
    i = 1
    print("\nFamily Category Contacts:-")
    for contact in contacts:
        if contacts[contact]['Family'] == 'yes':
            print(f'{i}. Email: {contact}, Name: {contacts[contact]['Name']}, Phone Number: {contacts[contact]['Phone Number']}, Address: {contacts[contact]['Address']}, Notes: {contacts[contact]['Notes']}')
            i += 1
    i = 1
    print("\nWork Category Contacts:-")
    for contact in contacts:
        if contacts[contact]['Work'] == 'yes':
            print(f'{i}. Email: {contact}, Name: {contacts[contact]['Name']}, Phone Number: {contacts[contact]['Phone Number']}, Address: {contacts[contact]['Address']}, Notes: {contacts[contact]['Notes']}')
            i += 1

def export_contact():
    pass

def import_contact():
    pass

contact = open_file()

# user_selection = 0
while True:
    try:
        # print("Contacts currently in the system: ", contact)
        print('''
            Welcome to the Contact Management System! 
              
            Menu:
            1. Add a new contact
            2. Edit an existing contact
            3. Delete a contact
            4. Search for a contact
            5. Display all contacts
            6. Display Contacts by Categories
            7. Export contacts to a text file
            8. Import contacts from a text file
            9. Quit 
              ''')
        user_selection = int(input("Please enter your choice (1-9): "))
        if int(user_selection) < 1:
            raise ValueError ("Less than One")
        elif int(user_selection) > 9:
            raise ValueError ("Greater than 8")
        elif int(user_selection) >= 1 and int(user_selection) <= 9:
            pass
        else:
            raise ValueError ("Wrong")
    except ValueError as ve:
        if "Less than One" in str(ve):
            pass
        elif "Greater than 8" in str(ve):
            pass
        elif "Wrong" in str(ve):
            pass
    else:
        if user_selection == 1:
            contact = add_new_contact()
        elif user_selection == 2:
            # print(contact)
            edit_contact(contact)
        elif user_selection == 3:
            new_contact = delete_contact(contact)
            contact = new_contact
        elif user_selection == 4:
            search_contact(contact)
        elif user_selection == 5:
            display_contact(contact)
        elif user_selection == 6:
            display_contact_category(contact)
        elif user_selection == 7:
            update_file(contact)
            print("\nContacts have been saved in file called contacts.txt")
        elif user_selection == 8:
            print("\nLoading data from contacts.txt")
            contact = open_file()
        elif user_selection == 9:
            print("\nThank you for using the Contact Management System. Goodbye!!!")
            break

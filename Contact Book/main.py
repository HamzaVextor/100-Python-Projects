TASK_FILE = 'contact.txt'

def show_menu():
    print("Welcome to your contact book")
    print('1. View Contacts')
    print('2. Add contacts')
    print('3. Delete Contacts')
    print('4. Search Contacts')
    print('5. Exit')

def view_contacts():
    try:
        with open(TASK_FILE, 'r') as file:
            contacts = file.readlines()
            for index, contact in enumerate(contacts, start=1):
                print(f"{index}. {contact.strip()}")
    except FileNotFoundError:
        print("The contact file does not exist.")

    

def add_contacts():
    add_contact_num, add_contact_name = input('Enter the contact number: '), input('Enter contact name: ')
    contact_Entry = f"{add_contact_num}, {add_contact_name}"
    with open(TASK_FILE, 'a') as file:
         file.write(contact_Entry)
    with open(TASK_FILE, 'r') as file:
         for index, contact in enumerate(file, start=1):
             print(f"{index}. {contact.strip()}")
             print('Contact added successfully')

def delete_contact():
    view_contacts()
    contact_num = int(input('Enter task number: '))
    with open(TASK_FILE, 'r') as file:
        lines = file.readlines()
    if contact_num <= len(lines):
        delete_contact = lines.pop(contact_num - 1).strip()
    with open(TASK_FILE, "w") as file:
            file.writelines(lines)
            print(f"Task '{delete_contact}' deleted successfully!")

def search_contacts():
    search_criteria = input('Enter the contact number or name to search: ')
    matching_contacts = []
    with open(TASK_FILE, 'r') as file:
        for contact in file:
            contact_num, contact_name = contact.strip().split(', ')
            if search_criteria.lower() in contact_name.lower() or search_criteria.lower() in contact_num.lower():
                    matching_contacts.append(contact.strip())

            if matching_contacts:
                 print("Matching contacts found")

            for index, contact in enumerate(matching_contacts, start=1):
                 print(f"{index}. {contact}")
            else:
                 print("NO matching contacts found")

def main():
    while True:
        show_menu()
        service = int(input('Choose a number from 1-5: '))
        if service == 1:
         view_contacts()
        if service == 2:
            add_contacts()
        if service == 3:
            delete_contact()
        if service == 4:
            search_contacts()
        if service == 5:
            break
    
if __name__ == "__main__":
    main()
import contacts
# Salmaan Rauf
# 2-08-2024
# Creating menu for user interaction allowing modification and viewing of list

contact_dict = {}

while True:
    print("*** EMPLOYEE CONTACT MAIN MENU")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Find contact")
    print("6. Exit the program")


    choice= input("Enter menu choice: ")



    if choice == '1':
        try:
            id = int(input("Enter phone number: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contacts.add_contact(contact_dict, id = id, first_name=first_name, last_name=last_name)

            if result == "error":
                print("Phone number already exists. ")
            else:
                print("Contact added successfully: ", result)
        except ValueError:
            print("Please only input integers for the phone number. ")


    elif choice == '2':
        try:
            mod_id = int(input("Enter phone number: "))
            mod_first_name = input("Enter first name: ")
            mod_last_name = input("Enter last name: ")

            result = contacts.modify_contact(contact_dict, mod_id= mod_id, mod_first_name=mod_first_name, mod_last_name=mod_last_name)

            if result == "error":
                print("Phone number does not exist. ")
            else: 
                print("Modified: ", mod_first_name, mod_last_name)

            # if not contacts.modify_contact(contact_list, id=id, mod_first_name=mod_first_name, mod_last_name=mod_last_name):
            #     print("Invalid index number.")
        except ValueError:
            print("Please only input integers for the phone number. ")

    elif choice == '3':

        try:
            id_del = int(input("Enter phone number: "))
            result = contacts.delete_contact(contact_dict, id_del=id_del)

            if result == "error":
                print("Invalid phone number. ")
            else:
                print("Deleted: ", first_name, last_name)
        except ValueError:
            print("Invalid  phone number. Please enter integers only.")
    

    elif choice == '4':
        contacts.print_list(contact_dict)
    
    elif choice == '5':
        find = input("Enter search string: ")
        print(f"Search String: {find}")
        print(f"Contact Dictionary: {contact_dict}")
        resulting_dict = contacts.find_contact(contact_dict, find=find)

        if resulting_dict:
            print("==================== FOUND CONTACT(S) ====================")
            print(f'{"Last name":<0}{"            First name":<22}{"           Phone":<40}')
            print("==================== ==================== ======")

            for key, value in resulting_dict.items():
                print(f'{value[1]:<21}{value[0]:<20} {key:<10}')
        else:
            print("No contacts found. ")

    elif choice == '6':
        break
    
    else: 
        print("Invalid menu choice.")
        







# Salmaan Rauf
# 2-08-2024
# Creating all the actions that allow the user to modify and view the list

def print_list(contact_dict, /):
    """ This function formats and prints out the index, first name, and last name of each contact"""

    # Need to print out the labels for index, first name, last name based off the example spacing
    print("================== CONTACT LIST ==================")
    print(f'{"Last name":0}{"            First name":22}{"           Phone":40}')
    print("==================== ==================== ======")

    #iterate through the whole length of the contact list and print the corresponding values
    for i, values in contact_dict.items():
        # Given for formatting convention
        print(f'{contact_dict[i][1]:21}{contact_dict[i][0]:20} {str(i):10}')
        #        |Index    | index 0 of contact  | index 1 of contactlist 
                        #    list is first name    is last name



def add_contact(contact_dict, /, *, id, first_name, last_name):
    """This function will allow users to add a new contact to the contact list"""

    if id in contact_dict:
        return "error"
    else:
        contact_dict[id] = [first_name, last_name]
        return contact_dict[id]





def modify_contact(contact_dict, /, *, mod_id,  mod_first_name, mod_last_name):
    """The purpose of this function is to modify a contact based off the index. This could be used for misspellings etc..."""

    if mod_id not in contact_dict:
        return "error"
    else:
        contact_dict.update({mod_id: [mod_first_name, mod_last_name]})
        return contact_dict[mod_id]






def delete_contact(contact_dict, /, *, id_del):
    """This function deletes existing contacts"""

    if id_del not in contact_dict:
        return "error"
    else:
        del contact_dict[id_del]


    



def sort_contacts(contact_dict, /):
    """This function allows you to sort the contacts based on first or last name"""
    sorted_dict = dict(sorted(contact_dict.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
    return sorted_dict

def find_contact(contact_dict, /, *, find):
    """This function allows you to find a specific contact"""
    resulting_dict = {}

    print("Search String:", find)
    print("Contact Dictionary:", contact_dict)
    

    if find.isdigit():
        find_int = int(find)
        if find_int in contact_dict:

            resulting_dict[find_int] = contact_dict[find_int]
   
    else:
        for key, value in contact_dict.items():
            if find.isdigit() and find == key:
                resulting_dict[key] = value
            elif find.lower() in value[0].lower() or find.lower() in value[1].lower():
                resulting_dict[key] = value


    sorted_resulting_dict = sort_contacts(resulting_dict)
    return sorted_resulting_dict

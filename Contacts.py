#Moktadir Shourav fa9444 CSC 1100 Sec 002/003
#Project 1 Completed 04/06/2013
#Work Completed: 100%

def add_contact(): #Add Contact function. May also be considered the 'mother'
                    #of the coding tree because all functions can trace back to
                    #this function if there is a problem.
    print("\nAdd Contact\n")
    import pickle #Pickle module
    try: #Attempts to open binary file. Carries out commands for existing dict.
        contact_file = open("Contacts.dat","rb") #Load binary
        contact_set = pickle.load(contact_file) #Load dictionary
        contact_file.close() #Securing file closure
        new_contact = input("Enter contact name or 'Cancel': ") #Contact name
        if new_contact.lower() == 'cancel': #Easy exit option
            return
        else:
            contact_email = input("Enter contact e-mail: ") #Contact e-mail
            contact_set.update({new_contact : contact_email})
            contact_file = open("Contacts.dat","wb") #Load binary for update.
            pickle.dump(contact_set,contact_file) #Updated binary.
            contact_file.close() #Closure.
    except: #Response if no binary file exists
        print("You have no contacts!")
        new_contact = input("Enter contact name or 'Cancel': ")
        if new_contact.lower() == 'cancel':
            return
        else:
            contact_email = input("Enter contact e-mail: ")
            contact_set = {}
            contact_set.update({new_contact : contact_email})
            contact_file = open("Contacts.dat","wb") #Writes updated dictionary                                               
            pickle.dump(contact_set,contact_file)     #to binary file.
            contact_file.close()
            return


def check_list(): #Call it a 'background function'. Acts like a skeleton for the
    import pickle  #coding tree. Checks for existing file/dictionary.
    try:
        contact_file = open("Contacts.dat","rb")
        contact_set = pickle.load(contact_file)
        contact_file.close()
        if contact_set == {}: #Response if no dictionary exists
                print("You have no contacts!")
                add = input("Would you like to add a contact? ")
                if 'yes' in add.lower():
                    add_contact() #Return to 'mother'.
                else:
                    return
        else:
            return contact_set
    except EOFError: #Response to empty binary or reading error.
        print("You have no contacts!")
        add = input("Would you like to add a contact? ")
        if 'yes' in add.lower():
            add_contact()
        else:
            return
    except FileNotFoundError: #Response if no binary exists.
        print("You have no contacts!")
        add = input("Would you like to add a contact? ")
        if 'yes' in add.lower():
            add_contact()
        else:
            return

    
def search_contact(): #Function for searching contacts.
    print("\nSearch Contact\n")
    import pickle
    contact_set = check_list() #File/dictionary check
    if contact_set == None: #Function break condition
        return
    else:
        try:
            search_entry = input("Enter contact name, 'All', or 'Cancel': ")
            if search_entry.lower() == 'cancel':
                return
            elif search_entry.lower() == 'all':
                for key, value in sorted(contact_set.items()): #Attempts to
                    print("Name: ", key, "\nEmail:", \
                          value,"\n")                           #print an
                return                                          #organized list.
            else:
                print("Name: ", search_entry, "\nEmail:", \
                      contact_set[search_entry])
                return
        except KeyError: #Response for invalid entry.
            print("Entry does not exist!")
            show_list = input("Would you like to check your list? ")
            if 'yes' in show_list.lower():
                for key, value in sorted(contact_set.items()):
                    print("Name: ", key, "\nEmail:", \
                          value,"\n")
            else:
                return

    
def edit_contact(): #Edit Contact function.
    print("\nEdit Contact\n")
    import pickle
    contact_set = check_list() #Check
    if contact_set == None:
        return
    else:
        edit = input("Enter contact name or 'Cancel': ") #User-specified name
        if edit.lower() == 'cancel':
            return
        else:
            if edit not in contact_set: #Options for non-existing contact.
                create = input("Contact not in list. Create new contact? ")
                if 'yes' in create.lower():
                    new_email = input("Enter e-mail: ")
                    contact_set[edit] = new_email #creates new key and value.
                    print("Name:     ", edit, "\nEmail:", \
                      contact_set[edit])
                    contact_file = open("Contacts.dat","wb")
                    pickle.dump(contact_set,contact_file) #Update binary.
                    contact_file.close()
                    return
                else:
                    return
            else: #Options for existing contact.
                new_email = input("Enter new e-mail or 'Cancel': ")
                if new_email.lower() == 'cancel':
                    return
                else:
                    contact_set[edit] = new_email #Updates key with new value.
                    print("Name:     ", edit, "\nNew Email:", \
                      contact_set[edit])
                    contact_file = open("Contacts.dat","wb")
                    pickle.dump(contact_set,contact_file)
                    contact_file.close()
                    return
                

def delete_contact(): #Delete Contact function.
    print("\nDelete Contact\n")
    import pickle
    contact_set = check_list() #Check
    if contact_set == None:
        return
    else:
        try:
            delete = input("Enter contact name or 'Cancel': ")
            if delete.lower() == 'cancel':
                return
            else:
                contact_set.pop(delete) #Deletion of key/value from dictionary.
                print(delete,"has been deleted from your list.")
                contact_file = open("Contacts.dat","wb")
                pickle.dump(contact_set,contact_file) #Update binary
                contact_file.close()
                if contact_set == None: #Quick break from function.
                    print("You have no contacts.")
                else:
                    return
        except KeyError: #Options for invalid input.
            print("Entry does not exist!")
            show_list = input("Would you like to check your list? ")
            if 'yes' in show_list.lower():
                for key, value in sorted(contact_set.items()):
                    print("Name: ", key, "\nEmail:", \
                          value,"\n")
            else:
                return


def main_menu(): #Main Menu function, the 'father' because it keeps all the         
    selection = ""   #functions connected consistently.
    while selection.lower() != "quit": #Sets up a continuous function for                            
        print("\nMain Menu\n")            #quick-access convenience.
        selection = input("Choose an option (Number or Name):\n"
                          "1. Add Contact\n"
                          "2. Search Contact\n"
                          "3. Edit Contact\n"
                          "4. Delete Contact\n"
                          "5. Quit\n\n")
        if selection.lower() in "1. add contact": #From here the conditions             
            add_contact()                          #are made user-friendly.
        elif selection.lower() in "2. search contact":
            search_contact()
        elif selection.lower() in "3. edit contact":
            edit_contact()
        elif selection.lower() in "4. delete contact":
            delete_contact()
        elif selection.lower() in "5. quit":
            break
        else:
            print("Your input is invalid.")
        
        
main_menu()

''''''


def main_menu():        # Main menu function
    try:        # Try except to handle value error
        print("\n                                                 Menu                                    ")
        while True:
            # Prints menu and choices
            print("\nWelcome! You can create new entries, change email addresses, delete entries, or display entries")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry.")
            print("4. Remove an entry")
            print("5. Quit")

            choice = int(                                       # Gathers user's choice
                input("Please enter the number of your selection:      "))
            if 1 <= choice <= 5:            # makes sure choice is 1-5
                return choice
            else:
                print("That number is not valid. Please try again.")
    except ValueError:
        print("That is not a valid entry, try again")
    except Exception as e:
        print(f"There was an error: {e}")


def check():        # Check function that opens customer list in read mode
    try:
        with open("customer_list.txt", 'r') as file:            # stores lines
            lines = file.readlines()
        return lines                # returns lines
    except FileNotFoundError:               # handles file not found error
        print("Customer list does not exist. Creating new customer database...")
        return []


def create():       # Create function to create entries
    customers = check()             # opens file and reads lines
    # prompts entries for name, phone number and email
    fname = input("Please enter the customer\'s first name: ").strip().lower()
    lname = input("Please enter the customer\'s last name: ").strip().lower()
    phone = input("Please enter the customer\'s phone number: ")
    email = input("Please enter the customer\'s email: ").strip().lower()
    # Creates entry variable that formats the entries in the file
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customers.append(entry)         # Appends entries
    save(customers)     # Saves file


def read():     # Read function
    customers = check()
    # Prompts user to figure out what they would like to find an entry based on
    print("Would you like to search by:")
    print("Email (1), Phone number (2), or Last name (3)?")
    search_param = int(
        input("Input 1 for email, 2 for phone number, or 3 for last name: "))

    if search_param == 1:           # gathers user input and stores as query, along with setting the index variable to 1, 2, or 3
        query = input(
            "Enter the email of the customer you would like to search for: ").strip().lower()
        # Email is at index 3
        index = 3
    elif search_param == 2:
        query = input(
            "Enter the phone number of the customer you would like to search for (format: XXXYYYZZZZ): ").strip()
        # Phone number is at index 2
        index = 2
    elif search_param == 3:
        query = input(
            "Enter the last name of the customer you would like to search for: ").strip().lower()
        # Last name is at index 1
        index = 1
    else:
        print("Invalid Option")
        return

    found = False           # Sets found to false
    try:
        # searches lines individually for matches
        with open("customer_list.txt", "r") as file:
            for line in file:
                # strips and splits entries
                parts = line.strip().split(", ")
                # if statement to check if the length of the parts is equal to 4 along with checking if the parts index is equal to what the user inputted
                if len(parts) >= 4 and parts[index].strip().lower() == query:
                    print(
                        # If customer found, prints out details and sets found to true
                        f"\nCustomer found: {parts[0]} {parts[1]}, Phone: {parts[2]}, Email: {parts[3]}")
                    found = True
                    break
            if found == False:           # If not found, lets the user know
                print("Customer not found")
    except FileNotFoundError:                       # Standard error handling to make sure list is there
        print("Customer list does not exist")


def update():       # Update function to update entries
    customers = check()
    # Asks similar prompt to read function to determine what entry needs to be updated
    print("What are the credentials of the entry you would like to update")
    print("Email (1), Phone number (2), first name (3), or last name (4)?")
    search_param = int(                                                                             # Search parameter variable to take users search parameter and get a value
        input("Input 1 for email, 2 for phone number, 3 for first name, or 4 for last name: "))

    # Query variables that set index based on search parameter
    if search_param == 1:
        query = input(
            "Enter the email of the customer you would like to update for: ").strip().lower()
        # Email is at index 3
        index = 3
    elif search_param == 2:
        query = input(
            "Enter the phone number of the customer you would like to update for (format: XXXYYYZZZZ): ").strip()
        # Phone number is at index 2
        index = 2
    elif search_param == 3:
        query = input(
            "Enter the first name of the customer you would like to update for: ").strip().lower()
        # First name is at index 0
        index = 0
    elif search_param == 4:
        query = input(
            "Enter the last name of the customer you would like to update for: ").strip().lower()
        # Last name is at index 1
        index = 1
    else:
        print("Invalid Option")
        return

    found = False           # Sets found to false
    for line in customers:              # for statement using same logic as above
        # Strips and splits entries into a readable format for the code
        parts = line.strip().split(", ")
        if len(parts) >= 4 and parts[index].strip().lower() == query:
            print(
                f"\nCustomer found: {parts[0]} {parts[1]}, Phone: {parts[2]}, Email: {parts[3]}")
            confirm = input(
                # NOW prompts user to see if this is the correct entry to update
                "Is this the customer you'd like to update? (y/n): ").strip().lower()
            if confirm == 'y':
                new_fname = input(                                                                  # Prompt user for new values (blank to skip)
                    f"Enter new first name (leave blank to keep '{parts[0]}'): ").strip()
                new_lname = input(
                    f"Enter new last name (leave blank to keep '{parts[1]}'): ").strip()
                new_phone = input(
                    f"Enter new phone number (leave blank to keep '{parts[2]}'): ").strip()
                new_email = input(
                    f"Enter new email (leave blank to keep '{parts[3]}'): ").strip()

                # Keep old value if new one is blank
                if new_fname == '':
                    # if new value is blank, it keeps old value
                    parts[0] = parts[0]
                # if it is not blank, it overrides the previous entry with the new one
                else:
                    parts[0] = new_fname

                if new_lname == '':
                    parts[1] = parts[1]
                else:
                    parts[1] = new_lname

                if new_phone == '':
                    parts[2] = parts[2]
                else:
                    parts[2] = new_phone

                if new_email == '':
                    parts[3] = parts[3]
                else:
                    parts[3] = new_email

                # Finds the index of the line and update it in the list
                line_index = customers.index(line)
                customers[line_index] = f"{parts[0]}, {parts[1]}, {parts[2]}, {parts[3]}\n"
                # Sets found to true and breaks
                found = True
                break
            else:
                print("Canceled update.")
                return

    # If found is true, saves customer list and informs user it has been updated
    if found == True:
        save(customers)
        print("Customer updated successfully.")
    else:
        print("Customer not found.")


def delete():       # Delete function to delete an entry
    customers = check()
    # Asks user what credentials they would like to search for (same as above)
    print("What are the credentials of the entry you would like to delete")
    print("Email (1), Phone number (2), first name (3), or last name (4)?")
    search_param = int(
        input("Input 1 for email, 2 for phone number, 3 for first name, or 4 for last name: "))

    if search_param == 1:
        query = input(
            "Enter the email of the customer you would like to delete for: ").strip().lower()
        index = 3                               # Email is at index 3
    elif search_param == 2:
        query = input(
            "Enter the phone number of the customer you would like to delete for (format: XXXYYYZZZZ): ").strip()
        index = 2                               # Phone number is at index 2
    elif search_param == 3:
        query = input(
            "Enter the first name of the customer you would like to delete for: ").strip().lower()
        index = 0                               # First name is at index 0
    elif search_param == 4:
        query = input(
            "Enter the last name of the customer you would like to delete for: ").strip().lower()
        index = 1                               # Last name is at index 1
    else:
        print("Invalid Option")
        return

    # Sets found to false
    found = False
    # Sets line_to_delete to None
    line_to_delete = None

    # cycles though with same logic to find the customer to delete
    for line in customers:
        parts = line.strip().split(", ")
        if len(parts) >= 4 and parts[index].strip().lower() == query:
            print(f"\nIs this the customer you would like to delete?")
            print(
                # Shows user the entry of the customer to make sure it is the correct entry
                f"{parts[0]} {parts[1]}, Phone: {parts[2]}, Email: {parts[3]}")
            # Y or N to confirm
            confirm = input("Confirm deletion(y/n): ").strip().lower()
            # finds line and sets it to line to delete
            if confirm == 'y':
                # Deletes and sets found to true
                line_to_delete = line
                found = True
                break
            else:
                print("Deletion cancelled.")
                return

    # If found is true and line to delete is not None...
    if found == True and line_to_delete != None:
        # Removes that line
        customers.remove(line_to_delete)
        save(customers)                                         # Saves
        # informs user that entry has been deleted
        print("Customer successfully deleted.")
    elif found != True:
        print("Customer not found.")


# Save function to save file
def save(customers):
    with open("customer_list.txt", 'w') as file:
        for line in customers:
            file.write(line)
    print("Customer database updated")


def main():                                         # Main function
    customers = check()                                 # Starts by checking
    choice = main_menu()                                # Shows main menu
    while choice != 5:                              # While statement to start a loop
        if choice is None:                          # user selects option and runs that function based on input
            choice = main_menu()
        elif choice == 1:
            create()
            choice = main_menu()
        elif choice == 2:
            read()
            choice = main_menu()
        elif choice == 3:
            update()
            choice = main_menu()
        elif choice == 4:
            delete()
            choice = main_menu()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            break


main()

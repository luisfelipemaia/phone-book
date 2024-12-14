# Initialize an empty list to store contacts
phonebook = []

# Start an infinite loop to display the menu and perform actions
while True:
    # Display the menu options
    print("\n--- Phonebook ---")
    print("1. Add contact")
    print("2. Remove contact")
    print("3. Search contact")
    print("4. Show all contacts")
    print("5. Exit")

    # Prompt the user to select an option
    option = input("Choose an option (1-5): ")

    # Validate the input: exit the program if the option is invalid
    if option > "5" or option < "0":
        print("Invalid option")
        break

    # Option 1: Add a new contact
    elif option == "1":
        name = input("Enter the contact's name: ")  # Get the contact's name
        phone = input("Enter the phone number: ")  # Get the contact's phone number

        # Check if the contact already exists
        exists = False
        for contact in phonebook:
            if contact[0] == name:  # If a contact with the same name exists
                exists = True
                break

        if exists:
            print("This contact already exists in the phonebook.")  # Notify the user
        else:
            phonebook.append([name, phone])  # Add the new contact to the phonebook
            print(f"Contact '{name}' added successfully!")  # Confirm the addition

    # Option 2: Remove an existing contact
    elif option == "2":
        name = input("Enter the name of the contact to be removed: ")  # Get the contact's name
        found = False

        # Search for the contact in the phonebook
        for contact in phonebook:
            if contact[0] == name:  # If the contact is found
                phonebook.remove(contact)  # Remove the contact
                print(f"Contact '{name}' removed successfully!")  # Confirm the removal
                found = True
                break

        if not found:
            print("Contact not found.")  # Notify the user if the contact doesn't exist

    # Option 3: Search for a contact by name
    elif option == "3":
        name = input("Enter the name of the contact to search: ")  # Get the contact's name
        found = False

        # Search for the contact in the phonebook
        for contact in phonebook:
            if contact[0] == name:  # If the contact is found
                print(f"Name: {contact[0]}, Phone: {contact[1]}")  # Display contact details
                found = True
                break

        if not found:
            print("Contact not found.")  # Notify the user if the contact doesn't exist

    # Option 4: Display all contacts
    elif option == "4":
        if len(phonebook) > 0:  # Check if the phonebook has any contacts
            print("\n--- All Contacts ---")
            for contact in phonebook:  # Iterate over the phonebook and display each contact
                print(f"Name: {contact[0]}, Phone: {contact[1]}")
        else:
            print("The phonebook is empty.")  # Notify the user if the phonebook is empty

    # Option 5: Exit the program
    elif option == "5":
        print("Exiting the phonebook. See you later!")  # Display exit message
        break  # Exit the loop

    # Handle any other invalid inputs
    else:
        print("Invalid option. Please try again.")

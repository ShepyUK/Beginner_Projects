# Add new contact (name, phone, email) Y
# view all saved contacts
# search contacts by name or phone number
# update existing contact information
# delete a contact by name
# save and load contacts from a JSON file Y

import json
contacts = []
# Load tasks from file if it exists, otherwise create an empty file
try:
    with open("address_book.json", "r") as f:
        contacts = json.load(f)
        print("Address Book Loaded:", contacts)
except FileNotFoundError:
    print("No existing addresses found. Starting fresh.")
    with open("address_book.json", "w") as f:
        json.dump(contacts, f)


def save_tasks_to_file():  # saves tasks to file
    with open("address_cook.json", "w") as f:
        json.dump(contacts, f)
    print("Address saved successfully!")


def show_menu():  # start menu
    print("\nWelcome to the Address Book App!")
    print("1. Add Address")
    print("2. View Addresses")
    print("3. Update an Address")
    print("4. Delete an Address")
    print("5. Exit")


def add_address():  # adds address to the book (1)
    address = input("Enter the Contacts name: ")
    phone = input("Enter Phone number: ")
    email = input("Enter Email Address: ")
    contacts.append({"Name": address, "Phone": phone, "Email": email})
    save_tasks_to_file()
    print(f"Contact '{address}' added successfully!")


def view_addresses():  # views tasks (2)
    if not contacts:
        print("No Contacts avaliable.")
        return

    print("\nYour Contacts:")


def delete_address():  # delete contacts (4)
    if not contacts:
        print("No tasks available to delete.")
        return

    view_addresses()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(contacts):
            removed_contact = contacts.pop(task_number - 1)
            save_tasks_to_file()
            print(f"contact '{removed_contact['name']}' has been deleted.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    while True:
        show_menu()
        choice = input("Choose an options: ")

        if choice == "1":
            add_address()
            print("You chose to add a task.")
        elif choice == "2":
            view_addresses()
            print("you chose to view tasks.")
        elif choice == "3":
            update_address()
            print("you chose to mark a task as complete.")
        elif choice == "4":
            delete_address()
            print("you chose to delete a task.")
        elif choice == "5":
            print("Existing the app. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


main()

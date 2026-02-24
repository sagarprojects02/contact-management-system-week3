import json
import os
import csv

contacts = {}

# ---------------- VALIDATION FUNCTIONS ---------------- #

def validate_name(name):
    return name.replace(" ", "").isalpha()

def validate_phone(phone):
    phone = phone.replace(" ", "").replace("-", "")
    return phone.isdigit() and len(phone) == 10

def validate_email(email):
    return "@" in email and "." in email


# ---------------- CRUD FUNCTIONS ---------------- #

def add_contact():
    name = input("Enter Name: ").strip().title()
    if not validate_name(name):
        print("Invalid name!")
        return

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter Phone (10 digits): ").strip()
    if not validate_phone(phone):
        print("Invalid phone number!")
        return

    email = input("Enter Email: ").strip().lower()
    if not validate_email(email):
        print("Invalid email!")
        return

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully!")


def search_contact():
    search = input("Enter name to search: ").strip().lower()
    found = False

    for name, details in contacts.items():
        if search in name.lower():
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print("-" * 30)
            found = True

    if not found:
        print("No matching contact found.")


def update_contact():
    name = input("Enter name to update: ").strip().title()

    if name not in contacts:
        print("Contact not found!")
        return

    phone = input("Enter new phone: ").strip()
    if validate_phone(phone):
        contacts[name]["phone"] = phone

    email = input("Enter new email: ").strip()
    if validate_email(email):
        contacts[name]["email"] = email

    print("Contact updated successfully!")


def delete_contact():
    name = input("Enter name to delete: ").strip().title()

    if name not in contacts:
        print("Contact not found!")
        return

    confirm = input("Are you sure? (yes/no): ").lower()
    if confirm == "yes":
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Deletion cancelled.")


def display_all():
    if not contacts:
        print("No contacts available.")
        return

    for name, details in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print("-" * 30)


# ---------------- FILE OPERATIONS ---------------- #

def save_to_file():
    with open("contacts_data.json", "w") as file:
        json.dump(contacts, file, indent=4)


def load_from_file():
    global contacts
    if os.path.exists("contacts_data.json"):
        with open("contacts_data.json", "r") as file:
            contacts = json.load(file)


def export_to_csv():
    with open("contacts_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])
        for name, details in contacts.items():
            writer.writerow([name, details["phone"], details["email"]])
    print("Contacts exported to contacts_export.csv")


def show_statistics():
    print(f"Total Contacts: {len(contacts)}")


# ---------------- MENU ---------------- #

def main_menu():
    load_from_file()

    while True:
        print("\nCONTACT MANAGEMENT SYSTEM")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Export to CSV")
        print("7. Show Statistics")
        print("8. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            display_all()
        elif choice == "6":
            export_to_csv()
        elif choice == "7":
            show_statistics()
        elif choice == "8":
            save_to_file()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main_menu()

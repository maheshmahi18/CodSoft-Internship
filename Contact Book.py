class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("Contact list is empty.")

    def search_contact(self, query):
        found = False
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self, name, attribute, new_value):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if attribute.lower() == "phone":
                    contact.phone_number = new_value
                elif attribute.lower() == "email":
                    contact.email = new_value
                elif attribute.lower() == "address":
                    contact.address = new_value
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

# Main program loop
contact_book = ContactBook()

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        name = input("Enter contact's name: ")
        phone = input("Enter contact's phone number: ")
        email = input("Enter contact's email: ")
        address = input("Enter contact's address: ")
        contact_book.add_contact(Contact(name, phone, email, address))

    elif choice == '2':
        contact_book.view_contacts()

    elif choice == '3':
        query = input("Enter name or phone number to search: ")
        contact_book.search_contact(query)

    elif choice == '4':
        name = input("Enter name of contact to update: ")
        attribute = input("Enter attribute to update (phone/email/address): ")
        new_value = input("Enter new value: ")
        contact_book.update_contact(name, attribute, new_value)

    elif choice == '5':
        name = input("Enter name of contact to delete: ")
        contact_book.delete_contact(name)

    elif choice == '6':
        print("Thank you for using the Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")

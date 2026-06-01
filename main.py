import json

def show_menu():
    print("\n Contact Book App")
    print("===================")
    print("1. View contacts")
    print("2. Add contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

def save_file(contacts):
    if not contacts:
        print("No contacts to save.")
    else:
        with open("records.txt", "w") as file:
            for name, number in contacts.items():
                file.write(f"{name} : {number}\n")
    
def load_file():
    try:
        final_dict = {}
        with open("records.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    name, number = line.split(" : ", 1)
                    final_dict[name] = number
    except FileNotFoundError:
        return {}
    return final_dict

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def load_contacts():
    print("This is the JSON")
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No contacts found!")

def main():
    contacts = load_contacts()

    while True:
        show_menu()
        print("===============")
        user_choice = input("Enter a choice: ")

        if user_choice == "5":
            print("Good Bye!!")
            break
        elif user_choice == "1":
            if not contacts:
                print("No contacts found!")
            else:    
                print(contacts)
        elif user_choice == "2":
            print("You have chosen to add a contact.")
            print("------------------")
            contact_name = input("Enter the contact name: ")
            phone_num = input("Enter the phone number: ")

            contacts[contact_name] = phone_num
            print("\ncontact added.")
            print("=============")
            print(contacts)
            save_file(contacts)
            save_contacts(contacts)
        elif user_choice == "3":
            name = input("Enter the name of the contact that you want to search for: ")
            if name.lower() in contacts:
                print("Here is the contact you were looking for:")
                print(f"{name} : {contacts[name]}")
            else:
                print("\n No such contact found!")
        elif user_choice == "4":
            del_item = input("Enter the name to be deleted: ")
            if del_item.lower() in contacts:
                del contacts[del_item.lower()]
                print("\n Contact deleted successfully!")
                save_file(contacts)
                save_contacts(contacts)
            else:
                print("No such contact exists!")

        else:
            print("More features to be added shortly.")


if __name__ == "__main__":
    main()
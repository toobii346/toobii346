# Day 15: Simple Contact Book

print("=" * 35)
print("     CONTACT BOOK")
print("=" * 35)

contacts = {}  # A Dictionary to store contacts

while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Exit")
    
    choice = input("\nChoose (1-4): ")
    
    if choice == "1":
        # To add contacts
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        
        # We store multiple details in a dictionary
        contacts[name] = {"phone": phone, "email": email}
        print(f"Added {name}")
    
    elif choice == "2":
        # To view all contacts
        if not contacts:
            print("\nNo contacts yet!")
        else:
            print("\n" + "=" * 30)
            for name, info in contacts.items():
                print(f"\n📱 {name}")
                print(f"   Phone: {info['phone']}")
                print(f"   Email: {info['email']}")
    
    elif choice == "3":
        # To search a contact
        name = input("\nSearch name: ")
        if name in contacts:
            print(f"\nFound!")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
        else:
            print("Not found!")
    
    elif choice == "4":
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choice!")
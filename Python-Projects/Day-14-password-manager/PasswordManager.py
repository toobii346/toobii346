# Day 14: Simple Password Manager

print("=" * 40)
print("     SIMPLE PASSWORD MANAGER")
print("=" * 40)

# Dictionary to store website and passwords
passwords = {}

def show_passwords():
    """Display all saved passwords"""
    if not passwords:
        print("\nNo passwords saved yet!")
    else:
        print("\n" + "-" * 30)
        print("   SAVED PASSWORDS")
        print("-" * 30)
        for website, password in passwords.items():
            print(f"{website}: {password}")

while True:
    print("\n" + "-" * 30)
    print("1. Add password")
    print("2. View passwords")
    print("3. Delete password")
    print("4. Exit")
    print("-" * 30)
    
    choice = input("Choose (1-4): ")
    
    if choice == "1":
        # To add a password
        website = input("Enter website name: ")
        
        if website == "":
            print("Website name cannot be empty!")
            continue
        
        # This checks if the password already exists
        if website in passwords:
            print(f"Password for {website} already exists!")
            overwrite = input("Overwrite? (y/n): ").lower()
            if overwrite != "y":
                continue
        
        password = input("Enter password: ")
        passwords[website] = password
        print(f"Password saved for {website}")
    
    elif choice == "2":
        # To view passwords
        show_passwords()
    
    elif choice == "3":
        # To delete passwords
        if not passwords:
            print("\nNo passwords to delete!")
            continue
        
        show_passwords()
        website = input("\nEnter website name to delete: ")
        
        if website in passwords:
            del passwords[website]
            print(f"Deleted password for {website}")
        else:
            print(f"No password found for {website}")
    
    elif choice == "4":
        # Exit Message
        print("\nGoodbye! Keep your passwords safe!")
        break
    
    else:
        print("Invalid choice!")
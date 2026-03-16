# Day 4: A Simple Shopping List
# A basic program to manage a shopping list

shopping_list = []  # Create an empty list

while True:
    print("\n" + "=" * 30)
    print("     SHOPPING LIST")
    print("=" * 30)
    print("1. View items")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")
    print("=" * 30)
    
    choice = input("Choose (1-4): ")
    
    if choice == "1":
        # To view items
        if not shopping_list:
            print("\nYour list is empty!")
        else:
            print("\nYour items:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
    
    elif choice == "2":
        # To add items
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"Added: {item}")
    
    elif choice == "3":
        # To remove items
        if not shopping_list:
            print("\nNothing to remove!")
        else:
            print("\nYour items:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
            try:
                num = int(input("Enter number to remove: "))
                removed = shopping_list.pop(num - 1)
                print(f"Removed: {removed}")
            except:
                print("Invalid number!")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice!")
# Day 16: Calculator with Memory
# Same thing as in Day 2 but now remembers last result

print("=" * 35)
print("   CALCULATOR WITH MEMORY")
print("=" * 35)

memory = 0  # Stores last result

while True:
    print("\n" + "-" * 30)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Recall memory")
    print("6. Clear memory")
    print("7. Exit")
    print("-" * 30)
    
    choice = input("Choose (1-7): ")
    
    if choice == "7":
        print("Goodbye!")
        break
    
    # Gets the numbers
    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except:
            print("Invalid number!")
            continue
        
        # Calculates
        if choice == "1":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero!")
                continue
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        
        # Saves to memory
        memory = result
        print(f"Saved to memory: {memory}")
    
    elif choice == "5":
        # Recalls the memory
        print(f"Memory: {memory}")
    
    elif choice == "6":
        # Clears the memory
        memory = 0
        print("Memory cleared!")
    
    else:
        print("Invalid choice!")
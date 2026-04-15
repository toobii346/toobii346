# Day 19: Multiplication Table

print("=" * 35)
print("   MULTIPLICATION TABLE")
print("=" * 35)

while True:
    print("\n1. Create times table")
    print("2. Create full table (1-10)")
    print("3. Exit")
    
    choice = input("\nChoose (1-3): ")
    
    if choice == "1":
        # Times table for one number
        try:
            num = int(input("Enter a number: "))
            print(f"\nTimes table for {num}:")
            print("-" * 20)
            
            for i in range(1, 13):  # 1 to 12
                result = num * i
                print(f"{num} x {i} = {result}")
        except:
            print("Please enter a valid number!")
    
    elif choice == "2":
        # New: Nested loops - loop inside a loop
        print("\n" + "=" * 40)
        print("    MULTIPLICATION TABLE (1-10)")
        print("=" * 40)
        
        # Header row
        print("   ", end="")  # Space for first column
        for top in range(1, 11):
            print(f"{top:4}", end="")  # Prints numbers from 1-10 across top
        print()
        
        # Table rows (loop inside loop!)
        for row in range(1, 11):  # Outer loop: rows
            print(f"{row:2}", end="")  # Row number
            for col in range(1, 11):  # Inner loop: columns
                result = row * col
                print(f"{result:4}", end="")  # Printw each result
            print()  # New line after each row
    
    elif choice == "3":
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choice!")
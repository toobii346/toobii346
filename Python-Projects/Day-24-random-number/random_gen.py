# Day 24: Simple Random Number Generator

import random

print("=" * 35)
print("   RANDOM NUMBER GENERATOR")
print("=" * 35)

while True:
    print("\n1. Generate one number")
    print("2. Generate multiple numbers")
    print("3. Generate with step (2,4,6...)")
    print("4. Exit")
    
    choice = input("\nChoose (1-4): ")
    
    if choice == "1":
        # Generates one random number
        try:
            low = int(input("Enter lowest number: "))
            high = int(input("Enter highest number: "))
            
            if low <= high:
                random_num = random.randint(low, high)
                print(f"\nYour random number: {random_num}")
            else:
                print("Error: Lowest must be less than highest!")
        except:
            print("Please enter valid numbers!")
    
    elif choice == "2":
        # Generates multiple random numbers
        try:
            low = int(input("Enter lowest number: "))
            high = int(input("Enter highest number: "))
            count = int(input("How many numbers to generate? "))
            
            if low <= high and count > 0:
                print(f"\n{count} random numbers:")
                for i in range(count):
                    random_num = random.randint(low, high)
                    print(f"  {i+1}. {random_num}")
            else:
                print("Error: Invalid input!")
        except:
            print("Please enter valid numbers!")
    
    elif choice == "3":
        # Generates numbers with step (like 2,4,6,8...)
        try:
            start = int(input("Start from: "))
            end = int(input("End at: "))
            step = int(input("Step by: "))
            
            if step > 0:
                numbers = list(range(start, end + 1, step))
                if numbers:
                    random_index = random.randint(0, len(numbers) - 1)
                    random_num = numbers[random_index]
                    print(f"\nPossible numbers: {numbers}")
                    print(f"Random choice: {random_num}")
                else:
                    print("No numbers in that range!")
            else:
                print("Step must be positive!")
        except:
            print("Please enter valid numbers!")
    
    elif choice == "4":
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choice!")
# Day 22: Even or Odd Checker
# Checks if a number is even or odd

print("=" * 35)
print("     EVEN OR ODD CHECKER")
print("=" * 35)

def check_number(num):
    """Check if number is even or odd"""
    # NEW: Modulo operator (%) gives remainder
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

def check_multiple(numbers):
    """Check multiple numbers at once"""
    print("\n" + "-" * 30)
    print("   RESULTS")
    print("-" * 30)
    for n in numbers:
        result = check_number(n)
        print(f"{n} is {result}")

while True:
    print("\n1. Check one number")
    print("2. Check multiple numbers")
    print("3. Exit")
    
    choice = input("\nChoose (1-3): ")
    
    if choice == "1":
        # Checks one number
        try:
            num = int(input("Enter a number: "))
            result = check_number(num)
            print(f"\n{num} is {result}!")
            
            # Shows remainder
            print(f"Remainder when divided by 2: {num % 2}")
        except:
            print("Please enter a valid number!")
    
    elif choice == "2":
        # Checks multiple numbers
        try:
            numbers_input = input("Enter numbers separated by spaces: ")
            # Convert string to list of integers
            numbers = [int(x) for x in numbers_input.split()]
            check_multiple(numbers)
        except:
            print("Please enter valid numbers!")
    
    elif choice == "3":
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choice!")
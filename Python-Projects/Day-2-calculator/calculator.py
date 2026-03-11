# Day 2: Simple Calculator
# A basic calculator that adds, subtracts, multiplies, and divides

print("=" * 30)
print("     SIMPLE CALCULATOR")
print("=" * 30)

# We first get the number from the user
num1 = float(input("Enter first number: "))

# Then the second number from user
num2 = float(input("Enter second number: "))

# Menu display
print("\nChoose operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

# We get the user's choice
choice = input("Enter choice (1/2/3/4): ")

# Does the calculation based on choice
if choice == "1":
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")
elif choice == "2":
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")
elif choice == "3":
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")
elif choice == "4":
    if num2 == 0:
        print("\nError: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"\n{num1} / {num2} = {result}")
else:
    print("\nInvalid choice!")

print("\nThank you for using the calculator! 🧮")
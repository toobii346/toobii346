# Day 21: Simple Interest Calculator

print("=" * 35)
print("   SIMPLE INTEREST CALCULATOR")
print("=" * 35)

print("\nSimple interest formula:")
print("Interest = Principal × Rate × Time")
print("Total = Principal + Interest")

while True:
    print("\n" + "-" * 30)
    print("1. Calculate interest")
    print("2. Calculate total amount")
    print("3. Exit")
    print("-" * 30)
    
    choice = input("Choose (1-3): ")
    
    if choice == "1":
        # Calculates only the interest
        try:
            principal = float(input("\nEnter principal amount (€): "))
            rate = float(input("Enter interest rate (% per year): "))
            years = float(input("Enter number of years: "))
            
            # New: Interest formula
            interest = principal * (rate / 100) * years
            
            print(f"\n RESULTS:")
            print(f"   Principal: €{principal:.2f}")
            print(f"   Rate: {rate}%")
            print(f"   Time: {years} years")
            print(f"   Interest earned: €{interest:.2f}")
        except:
            print("Please enter valid numbers!")
    
    elif choice == "2":
        # Calculates total amount (principal + interest)
        try:
            principal = float(input("\nEnter principal amount (€): "))
            rate = float(input("Enter interest rate (% per year): "))
            years = float(input("Enter number of years: "))
            
            interest = principal * (rate / 100) * years
            total = principal + interest  # New: Adds principal to interest
            
            print(f"\n RESULTS:")
            print(f"   Principal: €{principal:.2f}")
            print(f"   Rate: {rate}%")
            print(f"   Time: {years} years")
            print(f"   Interest earned: €{interest:.2f}")
            print(f"   Total amount: €{total:.2f}")
        except:
            print("Please enter valid numbers!")
    
    elif choice == "3":
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choice!")
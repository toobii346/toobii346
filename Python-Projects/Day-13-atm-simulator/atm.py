# Day 13: Simple ATM Simulator

print("=" * 35)
print("        ATM SIMULATOR")
print("=" * 35)

# The starting balance
balance = 100.00

print(f"\nWelcome! Your starting balance is €{balance:.2f}")

while True:
    # Menu
    print("\n" + "-" * 35)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("-" * 35)
    
    choice = input("Choose (1-4): ")
    
    if choice == "1":
        # Balance checking
        print(f"\n Your balance: €{balance:.2f}")
    
    elif choice == "2":
        # Money Deposit
        try:
            amount = float(input("Enter amount to deposit: €"))
            
            if amount > 0:
                balance = balance + amount
                print(f"Deposited: €{amount:.2f}")
                print(f"New balance: €{balance:.2f}")
            else:
                print("Amount must be positive!")
        except:
            print("Please enter a valid amount!")
    
    elif choice == "3":
        # Money Withdrawal
        try:
            amount = float(input("Enter amount to withdraw: €"))
            
            if amount > 0:
                if amount <= balance:
                    balance = balance - amount
                    print(f"Withdrew: €{amount:.2f}")
                    print(f"New balance: €{balance:.2f}")
                else:
                    print("Insufficient funds!")
                    print(f"Your balance is only €{balance:.2f}")
            else:
                print("Amount must be positive!")
        except:
            print("Please enter a valid amount!")
    
    elif choice == "4":
        # Exit message
        print(f"\nGoodbye! Final balance: €{balance:.2f}")
        print("Thank you for using ATM Simulator!")
        break
    
    else:
        print("Invalid choice! Please select 1-4.")
# Day 25: Simple Countdown to Event
# It calculates how many days until an event

import datetime

print("=" * 35)
print("     DAYS UNTIL EVENT")
print("=" * 35)

def get_days_difference(target_year, target_month, target_day):
    """Calculate days between today and target date"""
    # Get today's date
    today = datetime.date.today()
    
    # Creates target date
    target_date = datetime.date(target_year, target_month, target_day)
    
    # Calculates difference
    difference = target_date - today
    return difference.days

while True:
    print("\n1. Countdown to a date")
    print("2. Days since a date")
    print("3. Exit")
    
    choice = input("\nChoose (1-3): ")
    
    if choice == "1":
        # Countdown to the future date
        try:
            print("\nEnter the date you're waiting for:")
            year = int(input("Year (e.g., 2025): "))
            month = int(input("Month (1-12): "))
            day = int(input("Day (1-31): "))
            
            days = get_days_difference(year, month, day)
            
            if days > 0:
                print(f"\nCountdown: {days} days left!")
                if days <= 7:
                    print("Coming soon!")
            elif days == 0:
                print("\nToday is the day!")
            else:
                print("\nThat date has already passed!")
                
        except:
            print("Please enter valid numbers!")
    
    elif choice == "2":
        # Days since the past date
        try:
            print("\nEnter the past date:")
            year = int(input("Year: "))
            month = int(input("Month (1-12): "))
            day = int(input("Day (1-31): "))
            
            days = get_days_difference(year, month, day)
            
            if days < 0:
                days_passed = abs(days)
                print(f"\n{days_passed} days have passed since that date")
            elif days == 0:
                print("\nThat is today!")
            else:
                print("\nThat date is in the future! Use option 1 instead.")
                
        except:
            print("Please enter valid numbers!")
    
    elif choice == "3":
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choice!")
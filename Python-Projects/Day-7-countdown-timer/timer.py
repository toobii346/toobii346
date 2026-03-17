# Day 7: Countdown Timer
# A simple timer that counts down from your chosen number

import time #This lets us use time functions

print("=" * 30)
print("     COUNTDOWN TIMER")
print("=" * 30)

# Asks the user for countdown time
try:
    seconds = int(input("\nEnter seconds to count down: "))
    
    if seconds <= 0:
        print("Please enter a positive number!")
    else:
        print(f"\n Counting down from {seconds} seconds...\n")
        
        # Countdown loop using time.sleep
        while seconds > 0:
            print(f" {seconds} seconds remaining...")
            time.sleep(1)  #Pauses for 1 second
            seconds = seconds - 1
        
        # Timer finishes
        print("\n" + "=" * 30)
        print("   TIME'S UP!")
        print("=" * 30)
        print("\a")  # This makes a beep sound on some computers

except ValueError:
    print("Please enter a valid number!")
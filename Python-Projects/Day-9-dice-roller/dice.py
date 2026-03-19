# Day 9: Dice Roller

import random
import time 

print("=" * 30)
print("     DICE ROLLER")
print("=" * 30)

def roll_dice(number_of_dice, sides=6):
    """Roll multiple dice and return results"""
    results = []
    total = 0
    
    print(f"\n Rolling {number_of_dice} dice with {sides} sides...")
    time.sleep(1)  # Dramatic pause
    
    for i in range(number_of_dice):
        roll = random.randint(1, sides)
        results.append(roll)
        total = total + roll
        print(f"  Dice {i+1}: {roll}")
        time.sleep(0.5)
    
    return results, total

# Main program
while True:
    print("\n" + "-" * 30)
    print("1. Roll one 6-sided die")
    print("2. Roll two 6-sided dice")
    print("3. Roll custom dice")
    print("4. Quit")
    print("-" * 30)
    
    choice = input("Choose (1-4): ")
    
    if choice == "1":
        # Rolls one die
        results, total = roll_dice(1)
        print(f"\n Result: {results[0]}")
    
    elif choice == "2":
        # Rolsl two dices
        results, total = roll_dice(2)
        print(f"\n Results: {results[0]} and {results[1]}")
        print(f"Total: {total}")
    
    elif choice == "3":
        # Customs the dice
        try:
            num = int(input("How many dice? "))
            sides = int(input("How many sides? "))
            if num > 0 and sides > 0:
                results, total = roll_dice(num, sides)
                print(f"\n Results: {results}")
                print(f" Total: {total}")
            else:
                print("Please enter positive numbers!")
        except:
            print("Please enter valid numbers!")
    
    elif choice == "4":
        print("\nThanks for playing")
        break
    
    else:
        print("Invalid choice!")
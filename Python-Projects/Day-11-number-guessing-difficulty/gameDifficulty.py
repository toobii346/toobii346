# Day 11: Number Guessing Game with Difficulty
# The same thing as day 3 but now with difficulty levels

import random

print("=" * 40)
print("     NUMBER GUESSING GAME")
print("=" * 40)

# The Difficulty levels
print("\nChoose difficulty:")
print("1. Easy (1-20, 6 guesses)")
print("2. Medium (1-50, 4 guesses)")
print("3. Hard (1-100, 3 guesses)")

try:
    difficulty = int(input("\nEnter choice (1-3): "))
    
    # We set a range and maximum guesses based on the difficulty
    if difficulty == 1:
        max_number = 20
        max_guesses = 6
        print(f"\nEasy mode: Guess a number between 1 and {max_number}")
        print(f"You have {max_guesses} guesses")
    elif difficulty == 2:
        max_number = 50
        max_guesses = 4
        print(f"\nMedium mode: Guess a number between 1 and {max_number}")
        print(f"You have {max_guesses} guesses")
    elif difficulty == 3:
        max_number = 100
        max_guesses = 3
        print(f"\nHard mode: Guess a number between 1 and {max_number}")
        print(f"You have {max_guesses} guesses")
    else:
        print("Invalid choice! Defaulting to Medium.")
        max_number = 50
        max_guesses = 4
    
    # The game starts
    secret_number = random.randint(1, max_number)
    guesses_used = 0
    guessed_correctly = False
    
    # The game loops
    while guesses_used < max_guesses and not guessed_correctly:
        guess = input(f"\nGuess (1-{max_number}): ")
        
        # Checks if the input is a number
        if not guess.isdigit():
            print("Please enter a valid number!")
            continue
        
        guess = int(guess)
        guesses_used += 1
        guesses_left = max_guesses - guesses_used
        
        # Checks the guesses
        if guess < secret_number:
            print(f"Too low! {guesses_left} guesses left.")
        elif guess > secret_number:
            print(f"Too high! {guesses_left} guesses left.")
        else:
            guessed_correctly = True
            print(f"\nYou got it in {guesses_used} guesses!")
    
    # Game over the message
    if not guessed_correctly:
        print(f"\nGame over! The number was {secret_number}")
    
    print("\nThanks for playing!")

except ValueError:
    print("Please enter a valid number!")
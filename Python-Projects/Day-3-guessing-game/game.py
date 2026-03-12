# Day 3: The number guessing game
# The computer picks a random number, you try to guess it

import random  # This basically generate random numbers

print("=" * 40)
print("     NUMBER GUESSING GAME")
print("=" * 40)
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?")

# The computer picks a random number between 1 and 100
secret_number = random.randint(1, 100)
guesses_taken = 0
guessed_correctly = False


# Loops

# The Game loop keeps running until they guess correctly
while not guessed_correctly:
    guess = input("\nEnter your guess (1-100): ")

    if not guess.isdigit():
        print("Please enter a valid number!")
        continue
    
    guess = int(guess)
    guesses_taken += 1
    
    # Comparing guesses to the secret number using "if-elseif-else"
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        guessed_correctly = True
        print(f"\nCongratulations! You got it!")
        print(f"You guessed the number in {guesses_taken} tries!")

print("\nThanks for playing!")
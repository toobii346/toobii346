# Day 5: Rock, Paper, Scissors Game

import random  # This lets the computer make random choices

print("=" * 30)
print("   ROCK, PAPER, SCISSORS")
print("=" * 30)

# The game options
options = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while True:
    print("\n" + "-" * 20)
    print(f"Score: You {player_score} - {computer_score} Computer")
    print("-" * 20)
    
    # Player's turn
    player_choice = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    # Checks if the player wants to quit
    if player_choice == "quit":
        print("\nFinal Score:")
        print(f"You: {player_score}  Computer: {computer_score}")
        print("Thanks for playing!")
        break
    
    # Checks if the player entered valid choice
    if player_choice not in options:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue
    
    # Computer's random choice
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    
    # Determines the winner as shown in day 2 too
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        player_score += 1
    else:
        print("The computer wins!")
        computer_score += 1
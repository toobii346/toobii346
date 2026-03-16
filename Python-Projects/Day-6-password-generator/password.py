# Day 6: Random Password Generator
# It creates a secure random password for you

import random

print("=" * 30)
print("   PASSWORD GENERATOR")
print("=" * 30)

# Characters to use in the password
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

# Combining all characters
all_characters = letters + numbers + symbols

# Asks user how long they want their password to be 
try:
    length = int(input("\nHow many characters? (8-20): "))
    
    # Makes sure that the length is reasonable
    if length < 8:
        print("Password too short! Using 8 characters.")
        length = 8
    elif length > 20:
        print("Password too long! Using 20 characters.")
        length = 20
    
    # Generates password
    password = ""
    for i in range(length):
        random_character = random.choice(all_characters)
        password = password + random_character  # Adds character to string
    
    print("\n" + "=" * 30)
    print("   YOUR GENERATED PASSWORD")
    print("=" * 30)
    print(f"\n {password}")
    print(f"\nLength: {length} characters")
    print("\nMake sure to save it somewhere safe!")

except:
    print("Please enter a valid number!")
# Day 18: Word Reverser

print("=" * 35)
print("        WORD REVERSER")
print("=" * 35)

while True:
    print("\n1. Reverse a word")
    print("2. Exit")
    
    choice = input("\nChoose (1-2): ")
    
    if choice == "1":
        word = input("Enter a word: ")
        
        # Here it reverses the word
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        
        print(f"\nOriginal: {word}")
        print(f"Reversed: {reversed_word}")
        
        # Here it checks if it's a palindrome
        if word == reversed_word:
            print("Cool. This is a palindrome!")
    
    elif choice == "2":
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choice!")
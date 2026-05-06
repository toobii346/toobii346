# Day 23: Simple Word Counter

print("=" * 35)
print("        WORD COUNTER")
print("=" * 35)

while True:
    print("\n1. Count words and letters")
    print("2. Compare two sentences")
    print("3. Exit")
    
    choice = input("\nChoose (1-3): ")
    
    if choice == "1":
        # We get the sentence from the user
        sentence = input("\nEnter a sentence: ")
        
        # We Count words using split()
        words = sentence.split()  # Split by spaces into list
        word_count = len(words)
        
        # Count characters (without spaces)
        char_count = 0
        for char in sentence:
            if char != " ":
                char_count += 1
        
        # Count spaces
        space_count = sentence.count(" ")
        
        print("\n" + "-" * 30)
        print("     RESULTS")
        print("-" * 30)
        print(f"Sentence: {sentence}")
        print(f"Word count: {word_count}")
        print(f"Letters/numbers: {char_count}")
        print(f"Spaces: {space_count}")
        print(f"Total characters: {len(sentence)}")
    
    elif choice == "2":
        # Compares two sentences
        print("\nEnter two sentences to compare:")
        sent1 = input("Sentence 1: ")
        sent2 = input("Sentence 2: ")
        
        words1 = len(sent1.split())
        words2 = len(sent2.split())
        
        print("\n" + "-" * 30)
        print("     COMPARISON")
        print("-" * 30)
        print(f"Sentence 1: {words1} words")
        print(f"Sentence 2: {words2} words")
        
        if words1 > words2:
            print("Sentence 1 has more words")
        elif words2 > words1:
            print("Sentence 2 has more words")
        else:
            print("Both sentences have the same number of words")
    
    elif choice == "3":
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choice!")
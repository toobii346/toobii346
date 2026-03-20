# Day 10: Simple Quiz Game

print("=" * 35)
print("       QUIZ GAME")
print("=" * 35)

# A Dictionary to store questions and answers
# Each question has: text, options, correct answer
quiz = {
    "What is the capital of France?": 
    {
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    "What is 5 + 3?": 
    {
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    "What color is the sky on a clear day?": 
    {
        "options": ["A. Green", "B. Blue", "C. Red", "D. Yellow"],
        "answer": "B"
    },
    "Which animal is known as the 'King of the Jungle'?": 
    {
        "options": ["A. Tiger", "B. Elephant", "C. Lion", "D. Giraffe"],
        "answer": "C"
    },
    "What is the opposite of 'hot'?":
      {
        "options": ["A. Warm", "B. Cold", "C. Spicy", "D. Cool"],
        "answer": "B"
    }
}

score = 0
question_number = 1

# Loops through each question
for question, data in quiz.items():
    print("\n" + "=" * 35)
    print(f"Question {question_number}: {question}")
    print("=" * 35)
    
    # Shows the options
    for option in data["options"]:
        print(option)
    
    # Gets the user's answer
    user_answer = input("\nYour answer (A, B, C, or D): ").upper()
    
    # Checks if the answer is correct
    if user_answer == data["answer"]:
        print("Correct")
        score += 1
    else:
        print(f"Wrong! The correct answer was {data['answer']}")
    
    question_number += 1

# Shows the final score
print("\n" + "=" * 35)
print("       QUIZ COMPLETE!")
print("=" * 35)
print(f"\nYour score: {score} out of {len(quiz)}")
print(f"Percentage: {score / len(quiz) * 100}%")

if score == len(quiz):
    print("Perfect score! You're a genius")
elif score >= 3:
    print("Good job")
else:
    print("Keep learning! Try again")

print("\nThanks for playing")
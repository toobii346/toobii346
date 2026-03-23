# Day 12: Story Generator

print("=" * 40)
print("         STORY GENERATOR")
print("=" * 40)
print("\nFill in the blanks to create your story!\n")

# This gets the words from the user
print("Enter the following:")
print("-" * 30)

# New aspect: Collecting multiple inputs to build a story
adjective1 = input("Adjective (describing word): ")
animal = input("Animal: ")
verb1 = input("Verb (action word): ")
place = input("Place: ")
adjective2 = input("Another adjective: ")
noun = input("Noun (person/place/thing): ")
verb2 = input("Another verb: ")
emotion = input("Feeling/emotion: ")

# NEW: Using f-string to format the story
story = f"""
                  YOUR STORY                     

One day, a {adjective1} {animal} decided to {verb1} to the {place}.

It was feeling very {emotion} about the adventure ahead.

Suddenly, a {adjective2} {noun} appeared and started to {verb2}!

The {animal} didn't know what to do. What a crazy day at the {place}!

The end.
"""

# It prints the story
print(story)
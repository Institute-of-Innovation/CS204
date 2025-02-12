import random

# Welcome message
print("Welcome to the Word Guessing Game!")

# Getting player's name
name = input("What is your name? ")
print(f"Good Luck, {name}! Let's begin!")

# Word list with hints
words_with_hints = {
    'variable': "A container that holds data in Python.",
    'function': "A reusable block of code that performs a task.",
    'loop': "A control structure used to repeat a block of code.",
    'integer': "A data type used to store whole numbers.",
    'string': "A data type used to store text in Python.",
    'boolean': "A data type that holds True or False values.",
    'list': "A collection that stores multiple values in a single variable.",
    'tuple': "An immutable collection of ordered values.",
    'dictionary': "A data structure that stores key-value pairs.",
    'condition': "A statement that checks whether something is True or False.",
    'iteration': "The process of repeatedly executing a block of code.",
    'recursion': "A function that calls itself to solve a problem."
}

# Selecting a random word and its hint
word, hint = random.choice(list(words_with_hints.items()))

# Displaying hint to help the player
print("\nHint:", hint)

# Variables for game logic
guesses = ''
turns = 10

# Game loop
while turns > 0:

    failed = 0  # Counter for unguessed characters
    display_word = ""

    for char in word:
        if char in guesses:
            display_word += char + " "
        else:
            display_word += "_ "
            failed += 1

    print("\nWord: ", display_word)

    if failed == 0:
        print("\n Congratulations! You guessed the word:", word)
        break

    guess = input("\nGuess a character: ").lower()

    if guess in guesses:
        print(" You already guessed that letter. Try another one.")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print("\n Wrong guess!")
        print(f"You have {turns} turns left.")

        if turns == 0:
            print("\n Game Over! The correct word was:", word)

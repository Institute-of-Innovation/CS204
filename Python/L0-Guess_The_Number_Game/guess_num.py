import random

def guess_num():
    print("Welcome to the Number Guessing Game!")
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    max_attempts = int(input("Enter the maximum number of attempts allowed: "))

    number_to_guess = random.randint(lower, upper)
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Enter your guess (Attempts remaining: {max_attempts - attempts}): "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                return  # Exit the function if the guess is correct
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # If the loop ends without guessing the number
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

# Start the game
guess_num()
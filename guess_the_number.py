
import random

def guess_the_number():
    # Step 1: Computer selects a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the 'Guess the Number' game!")
    print("I've selected a number between 1 and 100. Can you guess it?")

    while True:
        try:
            # Step 2: Prompt the user to guess the number
            guess = int(input("Enter your guess: "))
            
            # Step 3: Check if the guess is valid
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Step 4: Increment the attempt counter
            attempts += 1

            # Step 5: Provide hints based on the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                # Step 6: Correct guess, game ends
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        
        except ValueError:
            # Handle non-numeric input
            print("Oops! That's not a valid number. Please enter an integer between 1 and 100.")

# Start the game
guess_the_number()

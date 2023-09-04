import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the initial number of guesses
max_guesses = 10
current_guesses = 0

print("Welcome to the Number Guessing Game!")
print(f"Guess the secret number between 1 and 100. You have {max_guesses} attempts.")

while current_guesses < max_guesses:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        
        current_guesses += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the secret number {secret_number} in {current_guesses} attempts!")
            break

        remaining_guesses = max_guesses - current_guesses
        if remaining_guesses > 0:
            print(f"You have {remaining_guesses} {'attempts' if remaining_guesses > 1 else 'attempt'} left.")
        else:
            print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Thank you for playing!")

import random

# Generate a random number between 1 and 100 (inclusive)
number = random.randint(1, 100)

# Initialize the number of guesses
guess_count = 0

while True:
    # Increment the guess count
    guess_count += 1

    # Get input from the user
    num_input = input("Guess a number between 1 and 100: ")

    # Check if input is a digit and within the desired range
    if not num_input.isdigit():
        print("Please input an integer.")
    elif int(num_input) < 1 or int(num_input) > 100:
        print("The number should be between 1 and 100.")
    else:
        # Convert input to integer
        guess = int(num_input)

        # Check if the guess is correct
        if number == guess:
            print(f"OK, you are so good, it is {number}. You succeeded in {guess_count} guesses!")
            break
        elif number > guess:
            print("Your number is too low.")
        elif number < guess:
            print("Your number is too high.")

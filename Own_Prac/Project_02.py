import random  # Importing Python's built-in random module to generate random numbers

# Generate a random secret number between 1 and 10
secret_num = random.randint(1,10)

# Initialize the number of attempts made by the user
attempts = 0

# Start an infinite loop - this keeps running until the user guesses correctly
while True:
    # Take the user's guess as input and convert it to an integer
    guess = int(input("Guess the number only 1 to 10 :"))

    # Increase the attempt counter by 1
    attempts = attempts + 1

    # Check if the guess is correct
    if guess == secret_num:
        # If correct, print success message with number of attempts and break the loop
        print(f"you guessed correct and in {attempts} attempts very well")
        break
    elif guess < secret_num:
        # If guess is too low, give a hint to try higher
        print("Too low! Try again")
    else:
        # If guess is too high, give a hint to try lower
        print("Too high! try again")

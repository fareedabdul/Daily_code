import random 

secret_num = random.randint(1,10)
attempts = 0


while True:
    guess = int(input("Guess the number only 1 to 10 :"))
    attempts = attempts + 1

    if guess == secret_num:
        print(f"you guessed correct and in {attempts} attempts very well")
        break
    elif guess < secret_num:
        print("Too low! Try again")
    else:
        print("Too high! try again")
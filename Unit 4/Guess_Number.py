import random

r = random.randint(1,100)
guess = 0

while guess != r:
    guess = input("Guess the number, between 1 and 100\n> ")

    guess = int(guess)

    if guess == r:
        print("You guessed right")
    elif guess > r:
        print("You guessed too high.\nTry again!")
    elif guess < r:
        print("You guessed too low.\nTry again!")
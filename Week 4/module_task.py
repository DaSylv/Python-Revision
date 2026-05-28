from random import random


def play_guess_the_number():
    min_val = int(input("Please enter the minimum value:\n"))
    max_val = int(input("Please enter the maximum value:\n"))
    secret_number = random.randint(min_val, max_val)
    print(f"I am thinking of a number between {min_val} and {max_val}")
    guess = None
    while guess != secret_number:
        guess = int(input("Try again:\n"))
        if guess < secret_number:
            print("Your guess is too low.")

        elif guess > secret_number:
            print("Your guess is too high.")

    print("Congratulations!You guessed my number!")

play_guess_the_number()
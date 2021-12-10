# Author: MOG 12/10/21

import random

number = random.choice(range(51))
x = 1
while x != 0:
    guess = input("What is your guess? ")

    if guess == "stop":
        x = 0
    elif guess == str(number):
        print("You guessed the number! It was {}.".format(guess))
        x = 0
    elif guess > str(number):
        print("{} is too high, try again.".format(guess))
    elif guess < str(number):
        print("{} is too low, try again.".format(guess))
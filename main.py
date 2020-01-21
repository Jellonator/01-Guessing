#!/usr/bin/python3

import sys
import random
import time

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

number = random.randint(1, 100)
guess = None
starting_time = time.time()
num_guesses = 0

while guess != number:
    guess_str = input("What is your guess? ")
    try:
        guess = int(guess_str)
        num_guesses += 1
        if guess < number:
            print("Your guess is too low")
        elif guess > number:
            print("Your guess is too high")
        else:
            print("Correct!")
            ending_time = time.time()
            timediff = ending_time - starting_time
            print("It took you {0} guesses within {1:,.1f} seconds.".format(num_guesses, timediff))
    except ValueError as e:
        print("Not a valid integer.")

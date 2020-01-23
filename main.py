#!/usr/bin/python3

import sys
import random
import time
import argparse

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

parser = argparse.ArgumentParser(description='Play a guessing game')
# parser.add_argument('--mode', '-m', choices=["hotcold", "lowhigh"], default="lowhigh", action="const")
parser.add_argument('--mode', '-m', type=str, choices=["hotcold", "lowhigh"], default="lowhigh")
args = parser.parse_args()

number = random.randint(1, 100)
guess = None
starting_time = time.time()
num_guesses = 0
previous_diff = None

print("I have a number between 1 and 100.")

while guess != number:
    guess_str = input("What is your guess [1-100]? ")
    try:
        guess = int(guess_str)
        if guess >= 1 and guess <= 100:
            num_guesses += 1
            if guess == number:
                print("Correct!")
                ending_time = time.time()
                timediff = ending_time - starting_time
                print("It took you {0} guesses within {1:,.1f} seconds.".format(num_guesses, timediff))
            else:
                if args.mode == "lowhigh":
                    if guess < number:
                        print("Your guess is too low")
                    else:
                        print("Your guess is too high")
                elif args.mode == "hotcold":
                    diff = abs(guess - number)
                    if previous_diff == None:
                        previous_diff = diff
                    elif diff < previous_diff:
                        print("Warmer")
                    elif diff == previous_diff:
                        print("Same")
                    else:
                        print("Colder")
                    previous_diff = diff
        else:
            print("Number is not in range.")
    except ValueError as e:
        print("Not a valid integer.")

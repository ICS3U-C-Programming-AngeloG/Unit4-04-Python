#!/usr/bin/env python3
# Created by: Angelo Garcia
# Created on: November 24th, 2025
# Program generates a random number and keeps asking the user to guess it until correct.
# Input validation prevents the program from crashing on invalid entries.

import random


def main():
    # generate random target between 1 and 10
    target = random.randint(1, 10)

    # keep asking until the user guesses correctly
    while True:
        user_input = input("Guess the number (1-10): ")
        try:
            guess = int(user_input)
            # give helpful hints
            if guess < target:
                print("Too low, try again.")
            elif guess > target:
                print("Too high, try again.")
            else:
                print(f"Correct! The number was {target}.")
                break
        except ValueError:
            # handle non-integer input
            print("Invalid entry. Please enter a whole number between 1 and 10.")


if __name__ == "__main__":
    main()

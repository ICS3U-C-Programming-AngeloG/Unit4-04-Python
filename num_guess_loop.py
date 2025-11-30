#!/usr/bin/env python3
# Created by: Angelo Garcia
# Date Created: November 30, 2025
# This program generates a random number between 1 and 100.
# It repeatedly prompts the user to guess the number until they guess correctly.
# Input validation ensures the program does not crash with invalid entries.

import random


def main():
    # Generate a random number between 1 and 100
    correct_number = random.randint(1, 100)

    user_guess = None

    # Loop until the user guesses correctly
    while user_guess != correct_number:
        user_input = input("Guess the number (between 1 and 100): ")

        try:
            val = int(user_input)
            if val < 1 or val > 100:
                print("Please enter a number between 1 and 100.")
            else:
                user_guess = val
                if user_guess < correct_number:
                    print("Too low! Try again.")
                elif user_guess > correct_number:
                    print("Too high! Try again.")
        except ValueError:
            print("That is not a valid whole number. Try again.")

    print(f"Congratulations! You guessed the correct number: {correct_number}")


if __name__ == "__main__":
    main()

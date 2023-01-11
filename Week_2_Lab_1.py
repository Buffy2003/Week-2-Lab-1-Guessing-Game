# Rashelle Ward
# CIS261
# Week 2 Lab 1, Guessing Game

import random

def display_title():
    print("Try to guess the number!")
    print()
    print()

def play_game(limit):
    number = random.randint(1, limit)
    print(f"I am thinking of a number between 1 and {limit}.\n")
    count = 1
    guess = int(input("Enter your guess: "))
    
    while (guess != number):
        if guess < number:
            print("That is too low.")
            count += 1
        elif guess > number:
            print("That is too high.")
            count += 1
        guess = int(input("Enter your guess: "))
    print(f"Correct! You guessed it in {count} tries.\n")

def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        limit = int(input("Enter the limit: "))
        play_game(limit)
        again = input("Would you like to play again? (y/n:) ")
        print()
    print("Good Bye!")


if __name__ == "__main__":
    main()

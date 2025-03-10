'''In this assignment, you will create a Python program that generates a random number between 1 and 100. Your program should allow the user to guess the number, and provide feedback on how close their guess is to the actual number.


Import the random module and use it to generate a random number between 1 and 100.

Write a while loop that allows the user to enter a guess for the number.

Inside the loop, use the abs() function to calculate the absolute difference between the guess and the actual number.

Provide feedback based on the computed difference (e.g., "Very Hot" for close guesses).

The loop should continue until the user guesses the correct number.
'''
import random


def main():
    from random import randint
    num = randint(1, 100)

    guess = int(input("Enter a number between 1 and 100: "))
    while guess != num:
        faroff = abs(num - guess)
        if faroff <= 5:
            print("Very hot")
        elif faroff <= 15:
            print("Hot")
        elif faroff <= 25:
            print("Cool")
        elif faroff >= 25:
            print("Cold")
        guess = int(input("Try again: "))
    print(f"You guessed it! The number was {num}")


main()

'''Write a short interactive Python program of your choice that uses try and except to catch and respond to at least two specific exceptions. Your program should:

    -Include a main() function.

    -Use try and except to catch specific errors like ValueError or ZeroDivisionError.

    -Provide helpful messages when errors occur.

    -Do something meaningful or fun—be creative! You could build a number guessing game, a basic calculator, or even a simple quiz with input validation.
'''
import random           # Imports random to get a random number between 0-100


def main():     # Defines main function
    actual_number = random.randint(0, 100)          # Gets the number 0-100

    while True:         # While statement to keep guessing
        try:
            user_guess = int(  # asks for user input
                input("Please enter a number between 0 and 100: "))
            if user_guess < 0 or user_guess > 100:              # Makes sure range is within 0-100
                print("\nPlease make sure your number is in the correct range!\n")
            if actual_number == user_guess:             # If guess is correct, breaks loop and ends program
                print(f"Nice guess! {actual_number} was the correct number!")
                break
            elif user_guess < actual_number:            # Gives smaller and larger hints
                print("Try a larger number")
            elif user_guess > actual_number:
                print("Try a smaller number")

        except:                 # Except value error to make sure the value is a number
            ValueError = print("\nPlease enter a valid value\n")


main()  # Calls to main

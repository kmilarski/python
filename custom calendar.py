'''In this assignment, you will write a Python program that generates a custom calendar for a user's birth month in the current year. This task will help you understand how to use Python's Calendar module, interact with users, and display data in a structured format.
Objective

Your program should ask the user for their birth month and then display the calendar for that month in the current year.
Requirements

        Your program must be contained within a main() function.
        Use the Python input() function to ask the user for their birth month (as an integer).
        Ensure your program can handle invalid inputs gracefully.
        Use Python's datetime module to find the current year.
        Generate and display the calendar for the user's birth month in the current year.
        Format the calendar output so it is easy to read and understand.

 
Steps

        Start by importing the necessary modules: calendar and datetime.
        Create a main() function where your program's logic will reside.
        Inside main(), get the current year using datetime.datetime.now().year.
        Ask the user to enter their birth month and store it in a variable.
        Validate the user input to ensure it's an integer between 1 and 12.
        Use the Calendar module to generate the calendar for the given month and year.
        Print the calendar to the console in a readable format.
        Don't forget to call the main() function at the end of your script.
'''
import calendar         # Imports calendar and datetime modules
from datetime import datetime


def main():         # Main function
    current_year = datetime.now().year          # Gets current year
    while True:  # While statement to keep prompting user if they enter an invalid month
        try:
            # Gets user birth month
            birth_month = int(input("Enter your birth month here(1-12): "))
            if 1 <= birth_month <= 12:          # Checks to see if it is between 1-12
                break
            else:
                # Prompts user again
                print("Month must be between 1 and 12. Try again.")
        except ValueError:              # Except to handle value errors
            print("VALUE ERROR. Please enter a number between 1 and 12")
    print(
        # Prints calendar for their birth month in the current year
        f"\nhere is a calendar for your birth month this year:\n\n {calendar.month(current_year, birth_month)}")


main()       # Call to main

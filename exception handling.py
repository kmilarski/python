'''Understand the Code: Review the provided Python script. It calculates the square of a user-input number.
Identify Potential Errors: Consider errors that might occur with non-numeric input.
Add Exception Handling: Implement try and except blocks to catch a ValueError. Handle incorrect data types with an error message and reprompt.
Test Your Code: Ensure the exception handling works correctly with various inputs.
GitHub Upload: Upload your py file to GitHub and hand in the link'''


# Defines square_number function
def square_number():
    while True:             # While loop to keep asking for a valid number if value error is excepted
        try:
            number = input("Enter a number to square: ")
            number = int(number)
            squared_number = number ** 2
            print(f"The square of {number} is {squared_number}.")
            break               # Breaks the function if valid input is entered

        except ValueError:
            # Asks for a valid number
            print("Please enter a valid number")


square_number()         # Main square_number function

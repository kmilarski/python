'''Assignment: Calculating Factorials
Objective: Write a Python program using a recursive function to calculate the factorial of a number. A recursive function is a function that calls itself to solve a problem.

Assignment Instructions:
Start by defining a function named factorial that takes one parameter, n, representing the number you're calculating the factorial for.
In your factorial function, first define the base case: n == 1 or n == 0, where the factorial is 1.
For the recursive step, return n * factorial(n-1) if n > 1.
Prompt the user for a non-negative integer and call factorial, printing the result.'''

# Defines the function factorial


def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return n * factorial(n-1)

# Main function that collects user input


def main():
    user_number = int(input("Please enter a non-negative integer here: "))
# Prompts user until the number entered is positive or 0
    while user_number < 0:
        user_number = int(input("Please enter a POSITIVE integer: "))
        if user_number >= 0:
            break
# Calculates user input with the factorial function and displays the answer
    user_number_factorial = factorial(user_number)
    print(f"{user_number} factorial is {user_number_factorial}!")


main()

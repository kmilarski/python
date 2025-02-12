'''In this exercise, you will practice using logical operators (and, or, not) in Python.
Your task is to create a program that prompts the user for two integer inputs and then demonstrate the use of these operators.'''

# asks user for two integers
num1 = int(input("Enter an integer:"))
num2 = int(input("Enter an integer:"))

# compares both numbers to see if they are positive

if num1 > 0 and num2 > 0:
    print("Both numbers are positive")
else:
    print("Both numbers are not positive")


# compares both numbers to see if they are both greater than 100

if num1 > 100 and num2 > 100:
    print("Both numbers are greater than 100")
else:
    print("Both numbers are not greater than 100")


# compares both numbers to see if at least one of them is even

if num1 % 2 == 0 or num2 % 2 == 0:
    print("At least one number is even")
else:
    print("Neither number is even")


# compares both numbers to see if at least one is less than 100

if num1 < 100 or num2 < 100:
    print("At least one number is less than 100")
else:
    print("Nether number is less than 100")


# compares both numbers to see if they are not equal to each other

if not num1 == num2:
    print("Num1 is not equal to num2")
else:
    print("Number 1 is equal to Number 2")


# compares both numbers to see what number is greater than the other

if not num1 > num2:
    print("Number 1 is not greater than number 2")
else:
    print("Number 1 is greater than number 2")

'''Set up your program in a main() function.
Create a Python program that asks the user to input a password.
Ensure the password meets the following criteria:
Between 8 to 20 characters long.
Contains at least one uppercase letter.
Contains at least one lowercase letter.
Includes at least one number.
Includes at least one symbol from the set: !@#$%&*.
Use a while loop to keep asking for the password until all criteria are met.
Once a valid password is entered, prompt the user to enter it again for confirmation.
Use try-except blocks to handle any errors or exceptions that occur.
If the second password entry matches the first, display a success message. Otherwise, prompt the user to start the process again.'''


def main():                # define main function
    while True:                     # While true to loop
        # Asks for user input
        user_pass = input("Please enter a password here: ")

        if len(user_pass) < 8 or len(user_pass) > 20:           # Checks length of user input
            print("Please ensure your password is in between 8 and 20 characters long")

        has_upper = False           # Sets all variables within the checks to false
        has_lower = False
        has_digit = False
        has_symbol = False

        for char in user_pass:              # Appends through all criteria checks and if criteria is met, variable is set to true
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            else:
                has_symbol = True
        # Prompts user if condition is not met for all 4 criteria listed above
        if has_upper == False:
            print("Please make sure you have at least ONE uppercase letter")
        elif has_lower == False:
            print("Please ensure you have at least ONE lowercase letter")
        elif has_digit == False:
            print("Please ensure you have at least ONE number within your password")
        elif has_symbol == False:
            print("Please ensure your password has one special character as well. ")

        # If all are true, password accepted and loop breaks
        if has_upper == True and has_lower == True and has_digit == True and has_symbol == True:
            print("Password accepted!")

        validated_password = input("Please enter the password again: ")
        if validated_password == user_pass:
            print("Password matches!")
            break
        else:
            print("please re-enter")


main()

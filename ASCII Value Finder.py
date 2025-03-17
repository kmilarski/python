'''At the end of this lesson, students will be able to:

Convert a character to its ASCII value using Python.
Convert an ASCII value back to a character.
Implement input validation using loops and error handling.
Step-by-Step Instructions
Start Your Python Script:
Open your Python environment and start a new script.
Use a main() function to organize your code.
Prompt for User Input:
Ask the user to enter a single character using input().
Validate the Input:
Ensure the user enters precisely one character.
Use len() to check input length.
Convert to ASCII Value:
Use the built-in function ord() to get the ASCII value.
Example:
ascii_value = ord(user_input)
Display the Result:
Print the ASCII value to the user.
Reverse Lookup:
Prompt the user to enter an ASCII value.
Ensure that the value is between 0 and 127.
Use a try-except block to handle invalid inputs.
Use the built-in function chr() to get the corresponding character.
Example:
character = chr(ascii_input)
Test Your Program:
Run your script and try various characters and ASCII values.
Submit Your Work:
Upload your script to GitHub.
Submit a link to your repository.'''


def main():         # Defines main function
    while True:     # WHile loop to make sure the user inputs a valid character
        user_input = input("Please enter a single character: ")
        if len(user_input) != 1:            # Len to check if user input is 1 character
            # Prompts the user to enter a SINGLE character again
            user_input = input("Please enter a SINGLE character here: ")
        else:
            break
    # ORD to find the ascii value and prints
    ascii_value = ord(user_input)
    print(f"The ASCII Value of {user_input} is {ascii_value}")

    while True:         # While loop to check if input is 0-127
        try:
            ASCII_input = int(input("Enter an ASCII value (0-127) here: "))
            if 0 <= ASCII_input <= 127:
                character = chr(ASCII_input)  # chr to get the character value
                print(
                    f"The character for ASCII value {ASCII_input} is {character}")
                break
            else:
                # else that returns this function if the value isnt between 0-127
                print("Invalid input. Please enter a value between 0 and 127.")
        except ValueError:
            # If the value error is returned, prompts user again
            print("Invalid input. Please enter a valid integer.")


main()          # Call to main

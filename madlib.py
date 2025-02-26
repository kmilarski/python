'''Develop a Python-based Madlib based on a song of your choice. 
The program should collect at least 8 different pieces of information from the user and incorporate them into the song using named arguments. 
The goal is to practice using functions, user input, and string manipulation in Python.

Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with inappropriate or offensive content.

Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, adjectives, nouns, places, etc.

Write the Function:

Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.

Use f-strings to incorporate these parameters into the song's lyrics.

Ensure the function prints the customized song lyrics.

Collect User Input:

Write code to collect user input for each of the 8 variables.

Use clear and descriptive prompts to guide the user.

Call the Function:

Call the custom_song function with the user inputs as named arguments.

Ensure the order of arguments matches the parameters in your function definition.
'''

'''Today, I woke up feeling (adjective). I put on my most (adjective) (piece of clothing) and got ready for my big day. 
My first stop was (place), where I met my (adjective) fans who wanted me to sign their (plural noun). 
After that, I had a(n) (adjective) lunch of (food) before heading to a(n) (event).
It was truly a(n) (adjective) day!'''


def song(adjective1, adjective2, clothing1, place1, adjective3, pluralnoun1, adjective4, food1, event1, adjective5):
    print("\n\n")
    print(f"Today, I woke up feeling {adjective1}.")
    print(
        f"I put on my most {adjective2} {clothing1} and got ready for my big day.")
    print(
        f"My first stop was {place1}, where I met my {adjective3} fans who wanted me to sign their {pluralnoun1}.")
    print(
        f"After that, I had a {adjective4} lunch of {food1} before heading to a {event1}.")
    print(f"It was truly a {adjective5} day!")


input_adjective1 = input("Enter an adjective: ")
input_adjective2 = input("Enter another adjective: ")
input_clothing1 = input("Enter a piece of clothing: ")
input_place1 = input("Enter a place you like: ")
input_adjective3 = input("Enter another adjective: ")
input_pluralnoun1 = input("Enter a plural noun: ")
input_adjective4 = input("Enter another adjective: ")
input_food1 = input("Enter your favorite food: ")
input_event1 = input("Enter an event you would like to go to: ")
input_adjective5 = input("Enter another adjective: ")

song(adjective1=input_adjective1, adjective2=input_adjective2, clothing1=input_clothing1, place1=input_place1, adjective3=input_adjective3,
     pluralnoun1=input_pluralnoun1, adjective4=input_adjective4, food1=input_food1, event1=input_event1, adjective5=input_adjective5)

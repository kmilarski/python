'''Your mission is to create a Python program that uses a dictionary to translate letters into the NATO Phonetic Alphabet. This program will ask users for a word and then spell it out using the NATO codes.

Steps to Follow:
Create the NATO Phonetic Alphabet Dictionary:
Construct a dictionary in Python named nato_alphabet, where each key is a letter, and its value is the corresponding NATO phonetic term.
Develop the Spelling Program:
Write a function to prompt the user for a word and iterate through each letter to find and print the NATO phonetic term.
Incorporate a Main Function:
Encapsulate your logic within a main() function for organization.
Test Your Program:
Test the program with various inputs, ensuring it works as expected.'''

# Defines the nato_alphabet dictionary
nato_alphabet = {
    'a': 'Alfa', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo',
    'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett',
    'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar',
    'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango',
    'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'Xray', 'y': 'Yankee', 'z': 'Zulu'
}
# Spell function that checks if key is in the lowercase word given


def spell(word_lower):
    for key in word_lower:
        if key in nato_alphabet:
            print(nato_alphabet[key])

# Main function to take user input and converts it to lowercase, then executes the spell function


def main():
    word = input("Enter a word here: ")
    word_lower = word.lower()

    spell(word_lower)


main()

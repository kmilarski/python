'''Write a Python program that handles exceptions related to list operations. Your program will start with a predefined list of the top ten performing artists of all time and will include functionality to modify this list based on user input.

- Modify Artist List: Write a function to replace an artist in the top_artists list. The function should ask the user for an index and a new artist name. Ensure your function catches and handles ValueError for invalid number conversion and IndexError for out-of-range indices.
- General Error Handling: Modify your function to catch both ValueError and IndexError using a single except block. Provide a general error message like "An input error occurred."



'''


def main():     # Main
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
                   # Artist list
                   "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    while True:
        try:  # While statement to loop if input is not correct

            user_index = int(input(                 # Asks for user index number
                "Please enter the index of the artist you would like to replace in the list: "))
            if user_index > 9 or user_index < 0:        # If out of range, raises index error
                raise IndexError
            user_artist = str(input(                # Replaces artist
                "Please enter the artist you would like to place in the list: "))
            # Adds new artist to list
            top_artists[user_index] = user_artist
            # Prints new artist list
            print("Your new top artists are: ")
            print(top_artists)
            break
        except:
            # Catches index error and value error
            IndexError = print("Please enter an index 0-9.")
            ValueError = print(
                "Value error. Please enter a valid number between 0-9.")


main()              # Calls to main

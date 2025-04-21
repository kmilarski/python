'''Create a Python program that uses a generator function to produce all possible two-letter combinations from a given list of characters. For example, if the list is ['a', 'b', 'c'], the program should generate 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'.

Instructions:
Define a generator function two_letter_combinations that takes a list of characters as an argument.
Use nested loops within the generator function to iterate over the list of characters. In each iteration, concatenate two characters and use the yield statement to yield the two-letter combination.
In the main method, call the generator function with a list of characters and iterate over the generator to print each combination. Create an original  5-letter list.
Include comments in your code to explain the logic behind the generator function and the use of the yield statement.'''




def two_letter_combinations(characters):         # Defines two_letter_combinations with the characters list
    for i in range(len(characters)):            # Nested loop first iterating through the list of 5 characters
        for u in range(len(characters)):        # loop inside the first loop that iterates through the other 5 characters generating combinations
            if not i == u:                      # if statement to prevent duplicates 
                yield characters[i] + characters[u]         # yield function to yield the combinations by just pausing the function to save its state

def main():                                         # Main function 
    characters = ['k', 'e', 'n', 'm', 'y']          # List of characters

    for twoletter in two_letter_combinations(characters):           # Iterates through the list to print all combinations
        print(twoletter)



main()              # call to main
'''Prompt the user to enter five names.

Store the names in a list.

Sort the list using the Bubble Sort algorithm.

Reverse the sorted list using a Python list method.

Print both the sorted and reversed lists.'''

# list of inputted names from user
names = []

# makes names lowercase
names = [name.lower() for name in names]

# if the amount of names inputted is not yet 5, asks user to input another name until 5 names are entered
for i in range(5):
    name = input("Enter a name:")
    names.append(name)

# sets swapped to true
swapped = True

# while loop that starts and sets swapped to false
while swapped:
    swapped = False
    # for loop that finds if "i" is in the range of the total amount of names (5) - 1
    for i in range(len(names) - 1):
        # if the name is greater than the next, swaps the names and sets swapped to true
        if names[i] > names[i + 1]:
            names[i], names[i + 1] = names[i + 1], names[i]
            swapped = True  # repeats loop until all 5 names are sorted

# prints list of sorted names
print("\nSorted list of names:", names)

# prints list of names reversed
names.reverse()
print("\nReverse sorted names:", names)

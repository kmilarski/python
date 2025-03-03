'''Now, let's practice using tuples. Imagine you're planning the classes for a programming certificate. You need to list out six classes. Here's what you need to do:

Create a tuple named programming_classes with these classes: 'Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals'.
Write a program that uses a for loop to print each class in the tuple.
Use the len function to print how many courses are in the tuple.
Make sure to use a main function for this program.
Try this out, and you'll understand how tuples work in Python well!'''

# Tuple defined with the 6 certifications


def main():
    programming_classes_tuple = ('Intro to Python', 'Advanced Python', 'Database Essentials',
                                 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')
    print(f"The current programming certificates available are:\n")
    for item in programming_classes_tuple:      # For loop that prints all certifications in the tuple
        print(item)
# Prints with len amount of certifications available
    print(
        f"\nThere are currently {len(programming_classes_tuple)} programming certificates available.")


main()

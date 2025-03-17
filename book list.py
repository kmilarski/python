'''In this assignment, you will create a Python program that collects book titles from a user. Your program should use a while loop to prompt the user to enter a total of 10 book titles. Follow these steps to complete your assignment:

Set Up the Main Function: Write your program inside a main function. This is where your while loop will be implemented.
Collect Book Titles: Use a while loop to ask the customer to enter 10 book titles. Store these titles in a list.
Ensure proper capitalization: Use the title function to ensure that the first letter is capitalized before storing it in the list.
Create a Sorted List: Once all titles are collected, save them to a new list named books_sorted. This list should contain the titles in alphabetical order.
Display the Titles: Use a for loop to print each title from the sorted list on a separate line.
Test Your Program: Ensure your program runs correctly and meets all the requirements.
Upload to GitHub: Once tested, upload your program to GitHub.
Submit Your Work: Submit the link to your GitHub repository on Canvas.
Ensure your program is well-commented and follows the best practices for Python programming.'''


def main():
    book_list = []      # New list of books to be entered

    while True:     # WHile loop to constantly ask for books until 10 are entered
        book_input = input("Enter a book title: ")
        book_input_cap = book_input.title()
        # Appends entries to the list
        book_list.append(book_input_cap)
        if len(book_list) == 10:
            break
    books_sorted = sorted(book_list)            # Sorts books in new list
    for i in books_sorted:          # For loop to list books line by line
        print(i)


main()          # Call to main

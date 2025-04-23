'''
    Open sales_totals in read mode (Download sales_totals.txt)
    Read each line in a loop
    Strip newline and convert to float
    Add to running total
    Count the lines
    Format and print each number
    Print the total, count, and average
    Use a main() function
    Use try and except for errors
'''


def main():         # Defines main
    total = 0.0             # sets total and count to 0
    count = 0
    try:
        with open('sales_totals.txt', 'r') as file:     # Opens file in read mode
            for line in file:           # For loop to cycle through lines of file
                try:
                    # strips line info as a float
                    line = float(line.strip())
                    total += line                       # adds each line in the loop until no line is found
                    count += 1                          # adds to the count each time
                    print(f"{line}")                    # prints the line

                except ValueError:
                    # if the line is blank via value error, "..." is printed to show the entry is a blank line
                    print(f"...")

        # If statement that starts if the count is > 0 but after the program is done looping
        if count > 0:
            average = total / count                     # Finds average
            print(f"The total is: {total:.2f}")         # prints statistics
            print(f"Number of entries: {count}")
            print(f"The average is: {average:.2f}")

    except IOError:                                     # IOError if the file is not found
        print("An IOError has occurred.")


main()                                                  # Calls main

'''
    Ask the user to input their birthday.
    Calculate the user's age in years, months, days, hours, and minutes.
    Provide detailed comments to all of the code, explaining what each line that has to do with time calculation does.
    Display the results in a user-friendly format.
    Implement the solution inside a main() function.

Instructions:

Create a Python script that performs the following steps:

    Define a main() function where your program logic will reside.
    Use my start program from GitHub: startprogram 

Links to an external site.
You can view the classroom demonstration of how we got to the code at the top of the page.
Comment explaining each line of the code

    Finish the code to get and display:
        months
        weeks
        days (done)
        years (done)

Format and print the results in a clear, understandable manner.'''

from datetime import datetime       # imports datetime from date time module


def main():     # Defines main

    print("\n\n")
    # Try block to handle errors if user inputs values out of ranges
    try:
        today = datetime.today()            # Gets todays date time
        # Asks for birth year in an int
        birth_year = int(input("What year were you born?  "))
        month = int(                # asks for month in an int
            input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  ")
                  )          # Asks for day in an int
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        # gets birthdate
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")         # Prints birthdate
        birthday_output = birthday.strftime(
            "%Y-%m-%d")             # Formats date as string
        print(birthday_output)      # Prints formatted output

        # Finds out difference between todays date and birthday entered
        delta = today - birthday
        print(f'Difference is {delta.days} days')

        delta_weeks = delta.days // 7               # Gets weeks since birthday
        print(f'You are {delta_weeks} weeks old')

        delta_months = delta.days // 30.417         # Months since birthday
        print(f'You are {delta_months} months old')

        delta_years = delta.days // 365.2425            # Years since birthday
        print(f'You are {delta_years} years old')

    except Exception as e:              # Except exception as e to print error in a readable way
        print(f"ooooops!!!:  {e}")
        main()


main()          # call to main

'''Accept a numeric grade from the user and display a letter grade. The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F

Check to see if the number given is between 0 and 100.  '''

# asks user for their numeric grade
grade = int(input("Enter your numeric grade here: "))

# calculates the user's letter assigned to their numeric grade
if grade < 60:
    alphabetical_grade = "F"

elif grade <= 69:
    alphabetical_grade = "D"

elif grade <= 79:
    alphabetical_grade = "C"

elif grade <= 89:
    alphabetical_grade = "B"

elif grade <= 100:
    alphabetical_grade = "A"

# prints result of the calculated grade
print("Your letter grade is:", alphabetical_grade)

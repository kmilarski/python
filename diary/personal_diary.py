'''Set Up Your Python Environment: Create a diary folder for this assignment, you will upload the whole file to GitHub when you are done. 
Create a New Python File: Name this file personal_diary.py.
Writing the Code:
Create this in a main function
Prompt the user to enter the current date and time, then a diary entry.
Open or create a file named diary.txt in append mode using open(). ( use append not write)
Write the user-provided date, time, and diary entry into the file. Ensure each entry is separated from the others by writing a blank line after entering the date/time line and the entry line. 
Close the file using the close() method.
Comments and Documentation: Add comments to your code explaining its functionality.
Testing the Program: Run personal_diary.py three times, each time entering a different diary entry along with the date and time. Check diary.txt to ensure entries are recorded correctly.
Submission: Submit both your personal_diary.py file and the diary.txt file containing your entries. 
 '''


def main():         # Main function
    date = input("Please enter the current date(mm/dd/yyyy): ")         # Date input
    time = input("Please enter the current time(hh:mm (AM/PM)): ")      # Time input
    diary_entry = input("Enter your diary entry here: ")                # Main diary entry
    try:
        with open('diary/diary.txt', 'a') as file:      # open diary folder, then open diary.txt as file using 'a' to append to the file, not overwrite

            file.write(date + '\n' + time + '\n' + diary_entry + '\n\n\n')      # Writes date, time, and entry in a readable manner
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occured:", e)
main()

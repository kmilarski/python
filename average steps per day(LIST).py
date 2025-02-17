'''Create a List: Start by creating a list named days that includes all seven days of the week.

Initialize an Empty List: Create an empty list called steps to store the number of steps taken each day.

User Input: Using a loop, ask the user to enter the number of steps they took for each day.

Store Steps: Append the user's input to the steps list.

Display Daily Steps: Show the user the steps recorded for each day.

Total Steps: Calculate and display the total number of steps taken in the week.

Average Steps: Calculate and display the average steps.'''

# creates a list named "days"
days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]

# Empty list that stores number of steps each day
steps = []

# asks user for amount of steps taken every day by starting at sunday and appending the steps variable
for i in range(len(days)):
    day = days[i]
    step_input = int(
        input(f"Enter the amount of steps you took on {day}:"))
    steps.append(int(step_input))

# displays daily steps recorded for each day
print("\nsteps recorded per day:\n")
for i in range(len(days)):
    print(f"{days[i]}: {steps[i]} steps")


# calculates total steps
total_steps = 0
for step in steps:
    total_steps += step
print(f"\nTotal Steps:", total_steps)

# calculates average steps
average_steps = total_steps / (len(days))
print(f"Average Steps per day: {average_steps:.2f}")

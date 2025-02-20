'''Create a Python script to track heart rate readings and calculate the average heart rate.

-Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").

-Use a loop to prompt the user for heart rate (in BPM) at each time slot.

-Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.

-Calculate the average heart rate and display it.'''
total = 0
average = 0
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rate = []

for time in time_slots:
    while True:
        rate = input(
            f"Enter your heart rate in beats per minute(BPM) in the {time}: ")
        if rate.isdigit():
            heart_rate.append([time, int(rate)])
            total += int(rate)
            break
        else:
            print("Please enter a valid heart rate")


average = total / 4
print(f"Your average heart rate for today was: {average:.2f} BPM")

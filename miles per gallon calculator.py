'''program uses the distance traveled and divides it by the tank size to calculate miles per gallon'''

# TODO: replace tank size with amount of gallons consumed to get a more accurate reading of miles per gallon

# defines the vehicle's tank capacity in gallons
tank_size = 15

# Define the total distance covered
distance = 600

# Calculate miles per gallon
mpg = distance / tank_size

# Print the result
# only shows the miles per gallon when going from a completely filled tank to completely empty
print("Miles per gallon:", mpg)

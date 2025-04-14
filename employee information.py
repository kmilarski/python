'''Assignment Part 1: Defining Classes
File 1: Write an Employee class with the following attributes:

Employee name
Employee number
Create a subclass named ProductionWorker that inherits from Employee. This subclass should include additional attributes:

Shift number (integer: 1 for day, 2 for night)
Hourly pay rate
Implement accessor and mutator methods (getters and setters) for each class.'''

class Employee:     # Defines employee class
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name            # initializes name and number
        self.__employee_number = employee_number

    def get_employee_name(self):        #Getters and setters for name and number
        return self.__employee_name
    def set_employee_name(self, value):
        self.__employee_name = value

    def get_employee_number(self):
        return self.__employee_number
    def set_employee_number(self, value):
        self.__employee_number = value

class ProductionWorker(Employee):       # Production worker class 
    def __init__(self, employee_name, employee_number, shift_number, hourly_rate):          # Inlcudes shift number and hourly rate
        super().__init__(employee_name, employee_number)        # calls to super class to inherit name and number
        self.__shift_number = shift_number          # initializes shift and hourly rate
        self.__hourly_rate = hourly_rate

    def get_shift_number(self):     # Getter and setters for shift number and hourly rate
        return self.__shift_number
    def set_shift_number(self, value):
        self.__shift_number = value
    
    def get_hourly_rate(self):
        return self.__hourly_rate
    def set_hourly_rate(self, value):
        self.__hourly_rate = value

    def get_shift_name(self):           # getter for shift_name which takes the inputted number (1 or 2) and converts it to day or night for easier readability
        if self.__shift_number == 1:            
            return "Day"
        elif self.__shift_number == 2:
            return "Night"

'''Assignment Part 2: Implementing and Testing
 

Part 2: Write a script to:

Create an instance of ProductionWorker.
Prompt the user for each attribute's data.
Store and then display the data using the object's methods.'''


def main():     # Defines main
    print("Please enter employee information here: ")
    name = input("Name: ")      # Input name and number
    number = input("Number: ")
    while True:
        try:
            shift = int(input("Enter shift number (1 for day, 2 for night): "))     # While loop to ask for shift number (1 or 2)
            if shift > 2 or shift < 1:
                print("Please enter 1 for day or 2 for night")
            else:
                break
        except ValueError:
            print("Please enter a valid integer (1 for day OR 2 for night)")        # Value error re-prompts user to enter a valid integer
    
    while True:
        try:            # While loop to ask for a float of hourly rate
            hourly_rate = float(input("Please enter your hourly rate: "))
            break
        except ValueError:          # Value error to re-prompt user to enter a valid hourly rate as a float
            print("Please enter a valid hourly rate")

    worker_instance = ProductionWorker(name, number, shift, hourly_rate)        # Creates worker instance under production worker subclass

    print("Employee information:")      # Prints employee information
    print("---------------------")
    print("Name:", worker_instance.get_employee_name())                 # Gets name, number, CONVERTED shift time (marked as name), and hourly rate returned as a float to the 0.00 decimal place
    print("Employee Number:", worker_instance.get_employee_number())
    print("Shift:", worker_instance.get_shift_name())
    print(f"Pay Rate:, {worker_instance.get_hourly_rate():.2f}")


        # Call to main
main()
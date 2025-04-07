'''Assignment Steps:

Class Creation: Design a class named Person with the following data: name, address, age, and phone number.
Accessor and Mutator Methods: Write get and set methods for each piece of data. These methods allow you to access and change the data safely.
Creating Instances: Write a program that creates three instances (objects) of the Person class. Use one instance for your made-up information and the other two for imaginary friends or family members.
Display Data: Print out the information stored in each instance. Ensure the output is formatted and easy to read.'''

class Person:           # Class definition for Person
    def __init__(self, name, address, age, phone_number):       # Init private variables
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number
#Method to format string of person's info
    def get_info(self):
        return f"Name: {self.__name}\nAddress: {self.__address}\nAge: {self.__age}\nPhone Number: {self.__phone_number}"
#Getter for name      
    def get_name(self):
        return self.__name
#Getter for address    
    def get_address(self):
        return self.__address
#Getter for age    
    def get_age(self):
        return self.__age
#Getter for phone number    
    def get_phone_number(self):
        return self.__phone_number
    
#Setter for name
    def set_name(self, name):
        self.__name = name
#Setter for address
    def set_address(self, address):
        self.__address = address
#Setter for age
    def set_age(self, age):
        self.__age = age
#Setter for phone number
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number 
#Main function to take instances and print data stored
def main():
    person1 = Person("Jerry", "1866 S State Street", "35", "847-826-1127")
    person2 = Person("Kyle", "285 High Point Dr.", "23", "224-783-9261")
    person3 = Person("Kenny", "981 Boycott Rd.", "22", "815-167-8814")

    print(person1.get_info())
    print()
    print(person2.get_info())
    print()
    print(person3.get_info())

main()
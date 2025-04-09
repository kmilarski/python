'''
        Create the Pet Class:
            Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
            Implement get and set methods for each of these attributes.
            Add a method called print_details that prints the details of the pet.
        Create Instances:

        Create three objects of the Pet class with different kinds, breeds, and names.

        Call the print_details method for each object that you created
        Demonstrate a Special Method or Function:

        Choose three of the following and demonstrate its use with the Pet class instances:
            __name__: Display the name of the class.
            type(): Show the class used to instantiate a pet object.
            __module__: Return the module name in which the Pet class is defined.
            __bases__: Display the base classes of the Pet class (if any).
            getattr(): Use it to access an attribute of a Pet instance.
            isinstance(): Check if an instance is of the Pet class.
'''


class Pet:          # Class Pet
    def __init__(self, kind, breed, name):      # Init kind breed name
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    def get_kind(self):     # Getter and setter for kind
        return self.__kind

    def set_kind(self, kind):
        self.__kind = kind

    def get_breed(self):    # Getter and setter for breed
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

    def get_name(self):     # Getter and setter for name
        return self.__name

    def set_name(self, name):
        self.__name = name
# Print details function

    def print_details(self):
        print("-----------------------")
        print(f"Pet kind: {self.__kind}")
        print()
        print(f"Pet breed: {self.__breed}")
        print()
        print(f"Pet name: {self.__name}")


# 3 pet instances
pet1 = Pet("Dog", "Husky", "Koda")
pet2 = Pet("Rat", "Grey Rat", "Stella")
pet3 = Pet("Cat", "Tabby", "Tika")
# Gets pet details for pet 1
pet1.print_details()
# returns name of module in which pet class is defined
print(f"pet1.__module: {pet1.__module__}")
# Gets pet details for pet 2
pet2.print_details()
# Checks if pet2 is in the instance of Pet class
print(f"pet2 isinstance(pet2, Pet): {isinstance(pet2, Pet)}")
# Gets pet details for pet 3
pet3.print_details()
# Checks class used to instantiate a pet object
print(f"type(pet3): {type(pet3)}")

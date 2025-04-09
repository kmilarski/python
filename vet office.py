'''
Define a Pet Class:
            Create private properties: owner_first_name, owner_last_name, pet_id, pet_name, and pet_type.
            Set a default value for pet_type as "Dog".
            Implement getter and setter methods for all properties.
            Include a class variable vet_name set to the name of your veterinary office.
            Add a method display_pet_info to print all details of the pet and owner.
Create Pet Objects:
            Instantiate at least three pet objects with different details.
            Show the use of setter methods for at least one pet object.
Implement Property Existence Check:
            Write a function check_property that uses hasattr() to verify if a property exists in a pet object.
Display Information:
            Use display_pet_info to print details for each pet.
            Show examples of check_property being used on various properties and pets.
'''


def main():
    class Pet:          # Class variable 'Pet'
        vet_name = "Huntley Vet"            # Vet name

        # Properties for pets
        def __init__(self, first_name, last_name, pet_id, pet_name, pet_type="Dog"):
            self.__first_name = first_name
            self.__last_name = last_name
            self.__pet_id = pet_id
            self.__pet_name = pet_name
            self.__pet_type = pet_type

    # Owner first name get and set
        def get_first_name(self):
            return self.__first_name

        def set_first_name(self, name):
            self.__first_name = name

    # Owner last name get and set
        def get_last_name(self):
            return self.__last_name

        def set_last_name(self, name):
            self.__last_name = name

    # Pet ID get and set
        def get_pet_id(self):
            return self.__pet_id

        def set_pet_id(self, pet_id):
            self.__pet_id = pet_id

    # Pet name get and set
        def get_pet_name(self):
            return self.__pet_name

        def set_pet_name(self, name):
            self.__pet_name = name

    # Pet type get and set
        def get_pet_type(self):
            return self.__pet_type

        def set_pet_type(self, pet_type):
            self.__pet_type = pet_type
    # Defines display pet info

        def display_pet_info(self):
            print(f"Owner: {self.__first_name} {self.__last_name}")
            print()
            print(f"Pet ID: {self.__pet_id}")
            print()
            print(f"Pet name: {self.__pet_name}")
            print()
            print(f"Pet type: {self.__pet_type}")
            print()
            print(f"Vet office: {Pet.vet_name}")
            print()
# 3 different pets listed
    pet_1 = Pet("Kenny", "Milarski", 9937, "Koda")
    pet_2 = Pet("Ingrid", "Johnson", 7375, "Uma", "Cat")
    pet_3 = Pet("Alyssa", "Martin", 5343, "Stella", "Rat")
# Example of using setter to change pet_2's pet ID
    pet_2.set_pet_id("8887")

# Checking properties with hasattr
    def check_property(pet, property):
        return hasattr(pet, property)
# Displays pet_1's info
    pet_1.display_pet_info()
# Uses check_property function to check if pet_1 has display_pet_info
    print("pet_1 has 'display_pet_info':",
          check_property(pet_1, 'display_pet_info'))
# Displays pet_2's info
    pet_2.display_pet_info()
# Uses check_property function to check if pet_2 has get_pet_type
    print("pet_2 has 'get_pet_type':", check_property(pet_2, 'get_pet_type'))
# Displays pet_3's info
    pet_3.display_pet_info()


main()

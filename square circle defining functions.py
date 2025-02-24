"""Start with Function Definitions:

Define two functions: square and circle.
Each function should take one parameter (side for square, radius for circle).
Write the square Function:

Calculate the area as side * side and display the result: "The area of the square is [result] square units."
Write the circle Function:

Calculate the area using the formula: area = π * radius * radius. Use 3.14 for π.
Display the result: "The area of the circle is [result] square units."
Test Your Functions:

Call square and circle with sample values."""


# Defines square function with side variable
side = 5


def square(side):
    area_squ = side * side
    print(f"The area of the square is{area_squ: .2f} square units.")


# Calls square with side var
square(side)

# Defines circle function with radius variable

rad = 12


def circle(rad):
    area_cir = rad * rad * 3.14
    print(f"The area of the circle is{area_cir: .2f} square units.")


# Calls circle with rad var
circle(rad)

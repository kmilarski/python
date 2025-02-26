'''Objective: Create a BMI calculator that takes a user's weight and height, calculates their BMI, and categorizes it as underweight, normal weight, overweight, or obese.

Requirements:
Global Variables:
    -Conversion constants for weight (1 lb = 0.453592 kg) and height (1 in = 0.0254 m).
Main Function:
    -Prompt the user for their weight in pounds and height in inches.
    -Convert the inputs to metric units using global conversion constants.
    -Calculate BMI using the formula bmi = weight / (height * height).
    -Determine the BMI category based on standard ranges.
    -Display the BMI value and category.
Commenting:
    -Include comments to explain key parts of the code.'''

# Global conversion constants
LB_TO_KG = 0.453592
IN_TO_M = 0.0254

# converting bmi to metric


def calculate_bmi(weight_lbs, height_in):
    weight_kg = weight_lbs * LB_TO_KG
    height_m = height_in * IN_TO_M
    bmi = weight_kg / (height_m * height_m)
    return bmi

# categorizing bmi


def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 24.9:
        return "Normal Weight"
    elif bmi >= 24.9 and bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Main function


def main():
    weight_lbs = float(input("Enter your weight in pounds here: "))
    height_in = float(input("Enter your height in inches here: "))

    if weight_lbs <= 0 or height_in <= 0:
        print("Please enter a valid weight and height")
        return
    bmi = calculate_bmi(weight_lbs, height_in)
    category = categorize_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are considered: {category}")


main()

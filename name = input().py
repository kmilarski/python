'''Design a Python program that prompts users to enter their total budget (ask them for their net monthly income) and amounts for spending categories:
Housing (rent or mortgage)
Utilities
Groceries
Transportation
Health Care
Personal Care
Clothing
Debt
Calculate the percentage of the total budget spent in each category.
Display the results in a user-friendly format using f-strings.
Ensure your code is well-commented to explain the functionality of different sections.'''

# ask for net monthly income
net_income = float(input("What is your net monthly income?: "))
# asks monthly spending on housing
spending_housing = float(
    input("How much do you spend on housing per month?: "))
# asks monthly spending on utilities
spending_utilities = float(
    input("How much do you spend on utilities per month?: "))
# asks monthly spending on groceries
spending_groceries = float(
    input("How much do you spend on groceries per month?: "))
# asks monthly spending on transportation
spending_transportation = float(
    input("How much do you spend on transportation per month?: "))
# asks monthly spending on health care
spending_health_care = float(
    input("How much do you spend on health care per month?: "))
# asks monthly spending on personal care
spending_personal_care = float(
    input("How much do you spend on personal care per month?: "))
# asks monthly spending on clothing
spending_clothing = float(
    input("How much do you spend on clothing per month?: "))
# asks monthly spending on paying off debt
spending_debt = float(input("How much do you spend on paying off debt?: "))

# calculates the percentage of net monthly income used for housing
housing_percentage = spending_housing / net_income
# calculates the percentage of net monthly income used for utilities
utilities_percentage = spending_utilities / net_income
# calculates the percentage of net monthly income used for groceries
groceries_percentage = spending_groceries / net_income
# calculates the percentage of net monthly income used for transportation
transportation_percentage = spending_transportation / net_income
# calculates the percentage of net monthly income used for health care
health_care_percentage = spending_health_care / net_income
# calculates the percentage of net monthly income used for personal care
personal_care_percentage = spending_personal_care / net_income
# calculates the percentage of net monthly income used for clothing
clothing_percentage = spending_clothing / net_income
# calculates the percentage of net monthly income used for debt
debt_percentage = spending_debt / net_income


# Prints percentage of total budget spent on housing per month
print(f"You spend {
      housing_percentage:.2%} of your monthly income on housing.")
# Prints percentage of total budget spent on utilities per month
print(f"You spend {
      utilities_percentage:.2%} of your monthly income on utilities.")
# Prints percentage of total budget spent on groceries per month
print(f"You spend {
      groceries_percentage:.2%} of your monthly income on groceries.")
# Prints percentage of total budget spent on transportation per month
print(f"You spend {
      transportation_percentage:.2%} of your monthly income on transportation.")
# Prints percentage of total budget spent on health care per month
print(f"You spend {
      health_care_percentage:.2%} of your monthly income on healthcare.")
# Prints percentage of total budget spent on personal care per month
print(f"You spend {
      personal_care_percentage:.2%} of your monthly income on personal care.")
# Prints percentage of total budget spent on clothing per month
print(f"You spend {
      clothing_percentage:.2%} of your monthly income on clothing.")
# Prints percentage of total budget spent on debt per month
print(f"You spend {
      debt_percentage:.2%} of your monthly income on paying off debt.")

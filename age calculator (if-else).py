# asks for the user's age
age = int(input("what is your age?: "))

# determines if the user can drive and responds
if age == 15:
    print("You're old enough to drive with a guardian! Congrats!")
elif age > 15:
    print("You can drive!")
else:
    print("Sadly you cannot drive. Just a few more years!")

# determines if the user can vote and responds
if age >= 18:
    print("Congrats! You can vote!")
else:
    print("Sadly you cannot vote!")

# determines if the user can buy alcohol legally and responds
if age >= 21:
    print("Congrats! You can legally buy alcohol! Drink responsibly!")
else:
    print("You are not old enough to legally buy alcohol.")

# determines if the user is eligible for a senior discount
if age >= 60:
    print("Wow! You can get a senior discount at most places!")
else:
    print("You are not eligible for a senior discount.")

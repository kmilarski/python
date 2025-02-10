'''Write a Python program to find and print all numbers divisible by 7 between 1 and 300. 
Use a for loop and the modulus operator (%).'''

# finds numbers between 1 and 300 that have a remainder of 0 when divided by 7 and prints them
for i in range(1, 300):
    if i % 7 == 0:
        print(i)

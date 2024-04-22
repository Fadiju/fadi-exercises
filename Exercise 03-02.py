# Exercise 2:

# Write a program that prints whether an integer is in between 1000 and 2000. If it is not, print
# whether it is lower than 1000 or higher than 2000.
# ANSER is>>>>>>

number = int(input("Enter number: "))

if number >= 1000 and number <= 2000:
    print("This number is in between 1000 and 2000")
elif number < 1000:
    print("This number is lower than 1000")
elif number > 2000:
    print("This number is larger than 2000")

else: 
    print("Wrong enter ( **you must enter valid number** )")
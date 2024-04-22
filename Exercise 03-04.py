# Exercise 4:

# Write a program that finds the largest of 4 numbers.
# Output:
# The largest number is 24
# ANSER is>>>>>>

num1 = int(10)
num2 = int(12)
num3 = int(8)
num4 = int(24)


if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print(f"The largest number is {num1}")
    
elif num2 >= num3 and num2 >= num4 and num2 >= num1:
    print(f"The largest number is {num2}")
    
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    print(f"The largest number is {num3}")
    
elif num4 >= num1 and num4 >= num2 and num4 >= num3:
    print(f"The largest number is {num4}")
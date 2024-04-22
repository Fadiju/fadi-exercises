# Exercise 3:

# Write a program that prints the sum of 3 given numbers, but if all 3 numbers are the same it
# should print 4 times the sum of the 3 numbers
# ANSER is>>>>>>

num1 = int(input("Enter  num1: "))
num2 = int(input("Enter  num2: "))
num3 = int(input("Enter  num3: "))

sum_result = num1 + num2 + num3
a = sum_result * 4

if num1 == num2 and num2 == num3:
    print("These numbers are the same")
    print(f"The sum of these number is {sum_result} ")
    print(f"Multiplied by 4 this becomes {a}")      
else:
    print(f"The sum of these numbers is {sum_result}")
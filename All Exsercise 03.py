# Exercise 1: 
# Write a program that tells the user whether a letter is a vowel or not.
# # ANSER is>>>>>>

# vowel_letter = "a", "o", "u", "e", "i", "A", "O", "U", "E", "I"
# letter_check = input(str("enter letter to see: "))

# if letter_check in vowel_letter:
#     print("this is an vowel letter")
# else:
#     print("this is not vowel letter")
    
# ------------------------------------

# Exercise 2:

# Write a program that prints whether an integer is in between 1000 and 2000. If it is not, print
# whether it is lower than 1000 or higher than 2000.
# ANSER is>>>>>>

# number = int(input("Enter number: "))

# if number >= 1000 and number <= 2000:
#     print("This number is in between 1000 and 2000")
# elif number < 1000:
#     print("This number is lower than 1000")
# elif number > 2000:
#     print("This number is larger than 2000")

# else: 
#     print("Wrong enter ( **you must enter valid number** )")
          
# ------------------------------------

# Exercise 3:

# Write a program that prints the sum of 3 given numbers, but if all 3 numbers are the same it
# should print 4 times the sum of the 3 numbers
# ANSER is>>>>>>

# num1 = int(input("Enter  num1: "))
# num2 = int(input("Enter  num2: "))
# num3 = int(input("Enter  num3: "))

# sum_result = num1 + num2 + num3
# a = sum_result * 4

# if num1 == num2 and num2 == num3:
#     print("These numbers are the same")
#     print(f"The sum of these number is {sum_result} ")
#     print(f"Multiplied by 4 this becomes {a}")      
# else:
#     print(f"The sum of these numbers is {sum_result}")
    
# ------------------------------------

# Exercise 4:

# Write a program that finds the largest of 4 numbers.
# Output:
# The largest number is 24
# ANSER is>>>>>>

# num1 = int(10)
# num2 = int(12)
# num3 = int(8)
# num4 = int(24)


# if num1 >= num2 and num1 >= num3 and num1 >= num4:
#     print(f"The largest number is {num1}")
    
# elif num2 >= num3 and num2 >= num4 and num2 >= num1:
#     print(f"The largest number is {num2}")
    
# elif num3 >= num1 and num3 >= num2 and num3 >= num4:
#     print(f"The largest number is {num3}")
    
# elif num4 >= num1 and num4 >= num2 and num4 >= num3:
#     print(f"The largest number is {num4}")
    
# ------------------------------------

# Exercise 5:

# In a certain tax system, people who earn more have to pay a higher percentage of taxes. For
# example:
# People earning under €67000 have to pay 24% of all of their earnings to the government in
# taxes.
# People earning under €97000 have to pay 31% of all of their earnings to the government in
# taxes.
# People earning more than €97000 have to pay 34% of all of their earnings to the government
# in taxes.

# Write a program that calculates how much money someone has left after taxes, given their
# income.

# Example 1:
# income = 58200
# Output:
# Your income after taxes is 44232 euro’s
# Example 2:
# income = 101000
# Output:
# Your income after taxes is 66660 euros

# ANSER is>>>>>>

# income = float(input("Enter your incom: "))


# tax_livel_1 = (24 / float(100)) * income
# tax_livel_2 = (31 / float(100)) * income
# tax_livel_3 = (34 / float(100)) * income

# the_rest_1 = income - tax_livel_1
# the_rest_2 = income - tax_livel_2
# the_rest_3 = income - tax_livel_3


# if income <= 67000:
#     print(f"the rest of yor incom is:{the_rest_1} \n After you pay teh tax")
# elif income > 67001 and income < 97000:
#     print(f"the rest of yor incom is:{the_rest_2} \n After you pay teh tax")
# elif income > 97000:
#     print(f"the rest of yor incom is:{the_rest_3} \n After you pay teh tax")
    
# ------------------------------------
# Exercise 6:
# Write a program that takes a string with a maximum size of 5. Do something different
# depending on the size of the string:
# 1 Letter: Print the letter 6 times (a = aaaaaa)
# 2 Letters: Switch the position of the letters (at = ta)
# 3 Letters: Move the last letter from the back to the front (Dog = gDo)
# 4 Letters: Print the reverse of the word (Wait = taiW)
# 5 Letters: Print the word divided by t (Brain = Btrtatitn)
# ANSER is>>>>>>

# # 01 
# a = "a"
# print(a * 6)

# # 02
# b = "at"
# print(b[::-1])

# # 03
# c = "Dog"
# c1 = (c[:-1])
# c2 = ("g" + c1)
# print(c2)

# # 04
# d = "Wait"
# print(d[::-1])

# # 05

# e = "Brain"
# e1 = ("t".join(e))
# print(e1)

# # or this suliotion 
# # print("t".join(e))

# ------------------------------------

# Exercise 7:

# Write a program that gives the user a basic test with three questions. If they have a question
# wrong stop the quiz, if they have it right give them the next question.

# Example 1:
# What is 2 * 2? 4
# That is correct!
# What is 6 / 3? 2
# That is also correct!
# What is 9 * 9? 18
# Correct! You passed the test!

   
# Example 2:
# What is 2 * 2? 4
# That is correct!
# What is 6 / 3? 20
# That is false, you failed the test
# ANSER is>>>>>>

# while True:
    
#     questions_1 = int(input("This is question 1 \n-What is 2 * 2 = "))

#     if questions_1 == 4:
#         print("That is correct. good \n")    
#     elif questions_1 != 4:
#         print("That is false, you failed the test")
#         break
         
#     questions_2 = int(input("This is question 2 \n-What is 6 / 3 = "))
#     if questions_2 == 2:
#         print("That is correct. fantastic! \n")
#     elif questions_2 != 2:
#         print("That is false, you failed the test")
#         break
    
#     questions_3 = int(input("This is question 3 \n-Waht is 9 * 9 = "))
#     if questions_3 == 81:
#         print("That is correct. you are smart \nThat was the end \nThanks...\n")
#         break  
#     elif questions_3 != 81:
#         print("That is false, you failed the test")
#         break
    
# ------------------------------------
           
    
 



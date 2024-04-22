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

while True:
    
    questions_1 = int(input("This is question 1 \n-What is 2 * 2 = "))

    if questions_1 == 4:
        print("That is correct. good \n")    
    elif questions_1 != 4:
        print("That is false, you failed the test")
        break
         
    questions_2 = int(input("This is question 2 \n-What is 6 / 3 = "))
    if questions_2 == 2:
        print("That is correct. fantastic! \n")
    elif questions_2 != 2:
        print("That is false, you failed the test")
        break
    
    questions_3 = int(input("This is question 3 \n-Waht is 9 * 9 = "))
    if questions_3 == 81:
        print("That is correct. you are smart \nThat was the end \nThanks...\n")
        break  
    elif questions_3 != 81:
        print("That is false, you failed the test")
        break
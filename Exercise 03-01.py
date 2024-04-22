# Exercise 1: 
# Write a program that tells the user whether a letter is a vowel or not.
# # ANSER is>>>>>>

vowel_letter = "a", "o", "u", "e", "i", "A", "O", "U", "E", "I"
letter_check = input(str("enter letter to see: "))

if letter_check in vowel_letter:
    print("this is an vowel letter")
else:
    print("this is not vowel letter")
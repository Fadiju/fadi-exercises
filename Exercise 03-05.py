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

income = float(input("Enter your incom: "))


tax_livel_1 = (24 / float(100)) * income
tax_livel_2 = (31 / float(100)) * income
tax_livel_3 = (34 / float(100)) * income

the_rest_1 = income - tax_livel_1
the_rest_2 = income - tax_livel_2
the_rest_3 = income - tax_livel_3


if income <= 67000:
    print(f"the rest of yor incom is:{the_rest_1} \nAfter you pay teh tax")
elif income > 67001 and income < 97000:
    print(f"the rest of yor incom is:{the_rest_2} \nAfter you pay teh tax")
elif income > 97000:
    print(f"the rest of yor incom is:{the_rest_3} \nAfter you pay teh tax")
# Exercise 6:
# Write a program that takes a string with a maximum size of 5. Do something different
# depending on the size of the string:
# 1 Letter: Print the letter 6 times (a = aaaaaa)
# 2 Letters: Switch the position of the letters (at = ta)
# 3 Letters: Move the last letter from the back to the front (Dog = gDo)
# 4 Letters: Print the reverse of the word (Wait = taiW)
# 5 Letters: Print the word divided by t (Brain = Btrtatitn)
# ANSER is>>>>>>

# 01 
a = "a"
print(a * 6)

# 02
b = "at"
print(b[::-1])

# 03
c = "Dog"
c1 = (c[:-1])
c2 = ("g" + c1)
print(c2)

# 04
d = "Wait"
print(d[::-1])

# 05

e = "Brain"
e1 = ("t".join(e))
print(e1)

# or this suliotion 
# print("t".join(e))
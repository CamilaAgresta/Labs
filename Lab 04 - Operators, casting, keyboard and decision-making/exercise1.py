"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 3/10/25 at 17:43
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 1

The only "real" assignment operator is the equal symbol (=), but Python has also some other assignment
operators as the following example shows (copy it into a program and run it). How do these operators work?
"""

a = 4
a += 2 # Write a += 2 is the same thing to write a = a +2
# therefore the variable a now is a = 4 +2 = 6
print(a)
a -= 3 # a -= 3 --> a = a - 3
print(a) # a = 6 - 3 = 3
a *= 3 # a *= 3 --> a = a * 3
print(a) # a = 3*3 = 9
a /= 2  # a /= 2 --> a = a / 2
print(a) # a = 9/2 = 4.5
a %= 4 #a %= 4 --> a = a % 4 (a will be the remainder of dividing a by 4)
print(a) # a = 4.5 % 4 = 0.5
a //= 2 # a //= 2 --> a = a // 2
print(a) # a = 0.5 / 2 = 0.25. The nearest integer is 0
a == 0 # This has no meaning. == is only for comparison
print(a) # It does not chance the value of a


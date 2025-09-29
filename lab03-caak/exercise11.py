"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 28/9/25 at 22:17
Universidad Carlos III de Madrid
Student

-------
Lab 3
Exercise: 11 - Multiple line strings
Write a Python program to store into a pair of variables the string: Twinkle, twinkle, little
star, how I wonder what you are! Up above the world so high, like a
diamond in the sky. Twinkle, twinkle, little star, how I wonder what you
are. In the first variable use triple quotes to do it, in the second one use regular quotes and escape
sequences. It must be stored in a way that when printing it we obtain the following specific format:
Twinkle, twinkle, little star,
how I wonder what you are!
Up above the world so high,
like a diamond in the sky.
Twinkle, twinkle, little star,
how I wonder what you are.
"""

text1 = """Twinkle, twinkle, little
star, how I wonder what you are! Up above the world so high, like a
diamond in the sky. Twinkle, twinkle, little star, how I wonder what you
are. """
print(text1)

print()
text2 = ('Twinkle, twinkle, little star, '
        '\n\thow I wonder what you are! '
         '\n\t\tUp above the world so high, '
         '\n\t\tlike a diamond in the sky. '
         '\nTwinkle, twinkle, little star, '
         '\n\thow I wonder what you are. ')

print(text2)

"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 3/10/25 at 18:18
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 2

Execute the following code and explain the result
(you can ask your favourite Generative-AI about it)
"""

a = 5 # We asign the value 5 to a variable a
if a == 2 or 3: # Python first evaluates a == 2 and then applies or,
    # so the condition is interpreted as (a == 2) or 3, not as “a == 2 or a == 3.
    # Since 3 is a non-null value, in a boolean context it is considered true,
    # so the whole condition results in True almost always, even if a is not 2.
    # That’s why the if always enters the upper block
 print("The variable is 2 or 3")
else:
 print("The variable has any other value")

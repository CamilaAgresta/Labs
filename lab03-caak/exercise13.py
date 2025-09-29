"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 28/9/25 at 22:29
Universidad Carlos III de Madrid
Student

-------
Lab 3
Exercise: 13 -  Printing with format
Copy the following program:
name = 'Johnny Depp'
age = 55
height = 1.78
weight = 65.8
eyes = 'brown'
hair = 'brown'
print("Let’s talk about %s." %name)
print("He's %i years old" %age)
print("He’s %.2f meters tall." %height)
print("He’s %.0f kilograms heavy." %weight)
print("Actually that’s not too heavy.")
print("He has %s eyes and %s hair." % (eyes, hair))
Execute it and check that you get the following outcome:
Let’s talk about Johnny Depp.
He’s 1.78 meters tall.
He’s 66 kilograms heavy.
Actually that’s not too heavy.
He’s got brown eyes and brown hair.
In class, we saw a different use of the print function, such as print("Let’s talk about", name).
Copy the same program but rewrite the print statements using this format. Is there any difference in the
output between the two methods?
"""

name = 'Johnny Depp'
age = 55
height = 1.78
weight = 65.8
eyes = 'brown'
hair = 'brown'
print("format 1:")
print("Let’s talk about %s." %name)
print("He's %i years old" %age)
print("He’s %.2f meters tall." %height)
print("He’s %.0f kilograms heavy." %weight)
print("Actually that’s not too heavy.")
print("He has %s eyes and %s hair." % (eyes, hair))

print()
print("format 2:")
print("Let’s talk about",name)
print("He's", age , "years old")
print("He’s", height ,"meters tall.")
print("He’s", weight ,"kilograms heavy.")
print("Actually that’s not too heavy.")
print("He has",eyes,"eyes and",hair,"hair.")

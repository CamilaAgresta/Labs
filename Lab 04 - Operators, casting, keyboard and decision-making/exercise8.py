"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 3/10/25 at 20:13
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 8

Create a program asking to enter the coordinates of a point in a plane, i.e. two integer values, x
and y, not equal to zero. The program must print the quadrant where this point lies (1st quadrant if x>0 and
y>0, 2nd if x<0 and y>0, etc.) (Note: you can use the flow diagram of practice 2). For example for (1,1) it must
print: 1st. If x or y are zero it must print "The values are not valid" and finish.
"""

print("Enter the coordinates of a plane")
x = int(input("x: "))
y = int(input("y: "))

quadrant = ""

if x == 0 or y == 0:
    print("The values are not valid")

else:
    if x > 0:
        if y > 0:
            quadrant = "1st"
        else:
            quadrant = "4th"
    if x < 0:
        if y > 0:
            quadrant = "2nd"
        else:
            quadrant = "3rd"

    print("The point is in the", quadrant ,"quadrant")
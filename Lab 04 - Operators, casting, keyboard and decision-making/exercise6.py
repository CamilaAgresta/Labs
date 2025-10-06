"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 3/10/25 at 19:16
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 6

Create a program receiving by keyboard a number of seconds and converting it to its hours
equivalent (for example 3680 seconds are 1 hour, 1 minute and 20 seconds and will be printed like
01:01:20). Notice the leading zeros.
"""

sec = int(input("Enter the number of seconds you want to convert it to its hour: "))
min = 0
hour = 0

if sec >= 0:
    if sec > 60:
        min = sec//60
        sec %= 60

        if min > 60:
            hour = min//60
            min %= 60
else:
    print("The seconds must be positive")

#print(hour,":",min,":",sec, sep="") # sep="" --> no spaces are inserted between the arguments

# better way
print("%02d:%02d:%02d" % (hour, min, sec))
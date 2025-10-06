"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 3/10/25 at 20:31
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 10

A year is leap-year if it is a multiple of 4, except if it is a multiple of 100. In this last case it will be
leap-year only if it is also a multiple of 400. For example the year 1900 was not a leap-year, but the year 2000
was. Create a program that reads a number by keyboard and calculates if it is a leap year.
(Note: you can use the flow diagram of week 2).

Example of outputs (notice the use of past or future tense):
    1901 was not a leap year
    2016 was a leap year
    2400 will be a leap year
    2401 will be not a leap year
"""

year = int(input("Enter a year to know if it is a leap-year: "))
be = ""
verb_tense = ""

if year < 2025:
    verb_tense = "was"
elif year > 2025:
    verb_tense = "will be"
else:
    verb_tense = "is"

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            be = ""
        else:
            be = "not"
else:
    be = "not"


if be:
    print(year, verb_tense, be, "a leap year")

else:
    print(year, verb_tense,"a leap year")







"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 12/10/25 at 18:46
Universidad Carlos III de Madrid
Student

-------
Lab 5
Exercise: 6

Define a program which requests the mark of the exam for each student in a class and
calculates the highest mark, the lowest, the average and the number of students attending to
the exam. The data input must finish when a negative number is introduced
"""

highest = 0
lowest = 10
average = 0
marks_sum = 0
n_students = 0
mark = 0

while mark >= 0:
    mark = int(input("Enter the mark of the exam of each student: "))
    if 0 <= mark <= 10:
        n_students += 1
        marks_sum += mark
        if mark < lowest:
            lowest = mark
        if mark > highest:
            highest = mark
    else:
        print("Invalid note")

if n_students > 0:
    average = marks_sum / n_students

print("The highest mark is:" , highest)
print("The lowes mark is:" , lowest)
print("The average of the marks is:" , average)
print("The number of students attending to the exam is:" , n_students)
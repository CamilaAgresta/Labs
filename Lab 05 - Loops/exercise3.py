"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 9/10/25 at 16:16
Universidad Carlos III de Madrid
Student

-------
Lab 5
Exercise: 3

Create a program to generate and print on screen the N perfect numbers smaller than the
value that the user introduces using the keyboard. A number is a perfect number when it is
equal to the addition of all its divisors except itself (You can rely on the flow diagram of the
similar exercise of a previous week). Example:
    Introduce the top limit to generate perfect numbers and press Enter
    10000
    The number 6 is perfect
    The number 28 is perfect
    The number 496 is perfect
    The number 8128 is perfect
"""

n_lim = int(input("Introduce the top limit to generate perfect numbers and press Enter: "))

n = 1
b = 1

while n <= n_lim:
    sum_div = 0
    b = 1

    while b <= n // 2:
        if n % b == 0:
            sum_div += b
        b += 1

    if sum_div == n and n != 0:
        print("The number", n, "is a perfect number")

    n += 1
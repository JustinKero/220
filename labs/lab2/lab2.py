"""
Name: Justin Kerosetz
lab2.py
"""
import math


def sum_of_threes():
    bound = eval(input("Enter the highest number the number should reach: "))
    totalsum = 0
    for i in range(3, bound, 3):
        totalsum += i
    print("Your total is: ", totalsum)

def triangle_area():
    a = eval(input("Enter length a: "))
    b = eval(input("Enter length b: "))
    c = eval(input("Enter length c: "))
    s = (a+b+c) / 2

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("This is the area for a triangle", area)

def sumSquares():
    num1 = eval(input("what will be the lowest bound?: "))
    num2 = eval(input("what will be the highest bound?: "))
    for i in range(num1, num2):
        calc = (num1**2)+(i**2)+(num2**2)
    print(calc)

def power():
    base = eval(input("What will be the base: "))
    pow = eval(input("what will be the power: "))
    for i in range(pow):
        totalsum = base**pow
    print(base, "^", pow, "=", totalsum)
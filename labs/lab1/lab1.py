"""
Name: Justin Kerosetz
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("The volume is: ", volume)

def shooting_percentage():
    numbshots = eval(input("Enter the amount of shots taken: "))
    shotsmade = eval(input("Enter the amount of shots made: "))
    percen = (shotsmade / numbshots) * 100
    print("The percentage of shots made is: %", percen)

def coffee():
    pounds = eval(input("Enter the amount of pounds of coffee: "))
    coffeepds = pounds * 10.50
    shipping = pounds * .86
    order = 1.50
    total = coffeepds + shipping + order
    print("Your total comes out to be: $", total)

def kilometers_to_miles():
    kilo = eval(input("Enter the amount of kilometers: "))
    miles = kilo / 1.61
    print("You will travel", miles, "miles")


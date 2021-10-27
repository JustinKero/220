"""
Name: Justin Kerosetz
lab9.py
"""
import math
from graphics import *

def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
        return acc

def toNumbers(strList):
    for i in range(strList):
        strList[i] = float(strList[i])
        pass

def writeSumOfSquares():
    inp = input("Enter a number: ")
    infile = open(inp, "r")
    outfile = open("output.txt", "wr")
    for line in infile:
        num = line.split(" ")
        toNumbers(num)
        squareEach(num)
        sum = sumList(num)
        outfile.write("sum = " + str(sum) + "\n")

def starter():
    weight = eval(input("Enter weight: "))
    wins = eval(input("Enter the number of wins: "))

    if weight < 160 and weight >= 150 and wins >= 5:
        print("This player is a starter.")
    elif (weight > 199) and wins > 20:
        print("This players is a starter.")
    else:
        print("This player is not a starter")

def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("This is a leap year")
    else:
        print("This is not a leap year")
def circleOverlap():
    win = GraphWin("Circle Overlap", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    circle = Circle(p1, radius)
    circle.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    circle2 = Circle(p3, radius2)
    circle2.draw(win)

    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    point = Point(200, 350)
    if distance > radius + radius2:
        msg1 = Text(point, "The circles do not overlap")
        msg1.draw(win)
    elif distance < radius + radius2:
        msg2 = Text(point, "The circles overlap")
        msg2.draw(win)
    else:
        print()

    win.getMouse()
    win.close()



def main():
    pass


main()
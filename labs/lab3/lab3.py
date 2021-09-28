"""
Name: <Justin Kerosetz>
<ProgramName>.py
"""
import math
def average():
    hw = int(input("How many homeworks: "))
    total_sum = 0
    for i in range(hw):
        number = float(input("Enter your grade on HW " + str(i+1)))
        total_sum += number
    avg = total_sum/hw
    print('Average of ', total_sum, 'number is :', avg)

def tip_jar():
    total_sum = 0
    for i in range(5):
        number = float(input("How much money would you like to donate? " + str(i)))
        total_sum += number
    print("There is ", total_sum, "dollars in the jar")

def newton():
    x = eval(input("Enter a number for x: "))
    refine = eval(input("How many times to improve the approximation"))
    approx = x/2
    for i in range(refine):
        approx = (approx + (x/approx))/2
    print(approx)

def sequence():
    terms = eval(input("Enter the number of terms in a series"))
    for i in range(1, terms + 1):
        y = 1 + (i // 2 * 2)
        print(y)
def pi():
    terms = eval(input("Enter the number n "))
    acc = 1
    for i in range(terms):
        num = 2 + (i//2*2)
        denom = 1 + ((i+1)//2*2)
        acc = acc*(num/denom)
    print(acc * 2)

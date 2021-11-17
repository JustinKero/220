"""
Name: Justin Kerosetz
lab12.py
"""
from random import randint

def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Justin"
    except:
        pass

def read_data(filename):
    f = open(filename, "r")
    d = f.readlines()
    d = d[0].split()
    i = 0
    while i < len(d):
        d[i] = int(d[i])
        i += 1
    return d

def is_in_linear(value, lst):
    i = 0
    while i < len(lst):
        if value == lst:
            return True
        else:
            return False

def good_input():
    x = eval(input("choose number from 1-10: "))
    while x < 1 or x > 10:
        x = eval(input("Not a valid number choose a number from 1-10: "))
    return x

def num_digits():
    x = eval(input("Enter positive integer: "))
    while x > 0:
        i = 0
        while x != 0:
            i += 1
            x //= 10
        print(i)
        x = eval(input("Enter positive integer: "))

def hi_lo_game():
    number = randint(1, 100)
    x = eval(input("Enter number from 1-100: "))
    guess = 0
    if x != number:
        guess = guess + 1
    while x != number and guess != 7:
        if x > number:
            print("Your number was too high")
            x = eval(input("Enter number from 1-100: "))
            guess = guess + 1
        elif x < number:
            print("Your number was too low")
            x = eval(input("Enter number from 1-100: "))
            guess = guess + 1
    if x == number and guess != 7:
        print("You won! The correct number was ", number, "It took you", guess, "number of tries")
    if guess == 7 and x != number:
        print("You lost the correct number was: ", number)
    if guess == 7 and x == number:
        print("You won! The correct number was ", number, "It took you", guess, "number of tries")



def main():

    pass


main()

"""
Name: Justin Kerosetz
lab7.py
"""
import math

def cash_conversion():
    number = eval(input("Enter the value: "))
    format_float = "{:.2f}".format(number)
    print("$" + format_float)

def encode():
    sentence = str(input("Enter a string: "))
    key = int(input("Enter a key: "))
    encryption = ""
    for i in sentence:
        encryption += chr((ord(i) - 97 + key) % 26 + 97)
    print("The encryption is: ", encryption)

def sphere_area(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return(volume)

def sum_n(n):
    acc = 0
    for i in range(n):
        acc += 1
    return acc

def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc += i ** 3
    return acc

def encode_better():
    sentence = input("Enter a string: ")
    key = input("Enter a key: ")
    encryption = ""
    for i in range(len(sentence)):
        s = ord(sentence[i])
        k = ord(key[i % len(key)])
        k = k - 97
        s = s + k
        new_s = chr(s)
        encryption += new_s

    print(encryption)

def main():
    cash_conversion()
    encode()
    print(sphere_area(3))
    print(sphere_volume(3))
    print(sum_n(3))
    print(sum_n_cubes(3))
    encode_better()

main()

"""
Name: Justin Kerosetz
lab13.py
"""

def is_in_binary(search_val, values):
    mid = values[len(values)//2]
    while mid and len(values) != 1:
        if mid > search_val:
            values = values[:[len(values)//2]]
        else:
            values = values[(len(values)//2) + 1:]
        mid = values[len(values)//2]
    if mid == search_val:
        return True
    else:
        return False

def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if j < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]

def get_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    w = abs(p1.getX() - p2.getX())
    h = abs(p1.getY() - p2.getY())
    return w * h

def rectangles(values):
    d = {}
    areas = []
    for rect in values:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    for i in range(len(areas)):
        values[i] = d[values[i]]

def trade_alert(filename):
    acc = 0
    infile = open(filename, "r")
    data = infile.read().split()
    for i in range(len(data)):
        acc += 1
        if int(data[i]) >= 830:
            print("Alert at ", acc, "seconds. Trading volume exceeded 830")
        if int(data[i]) >= 500:
            print("Alert at ", acc, "seconds. Trading volume exceeded 500")
def main():
    # add other function calls here
    pass


main()

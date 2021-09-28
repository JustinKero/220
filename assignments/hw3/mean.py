'Justin Kerosetz'
'Chapter 3'

import math
import statistics

def main():

    num = int(input("Enter the values to be entered: "))
    total_sum = 0
    mylist = []
    for i in range(num):
        number = int(input("Enter value: "))
        rms = number**2
        total_sum += rms
        mylist.append(number)
    hm = statistics.harmonic_mean(mylist)
    geo = statistics.geometric_mean(mylist)
    x = math.sqrt(total_sum) / 2
    y = hm
    z = geo
    rsavg = round(x, 3)
    hmavg = round(y, 3)
    geoavg = round(z, 3)
    print(rsavg)
    print(hmavg)
    print(geoavg)

if __name__ == '__main__':
    main()

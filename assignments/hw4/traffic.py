"""
Justin Kerosetz
HW 4
"""
import math

def main():
    road = eval(input("How many roads were surveyed?: "))
    carnum = 0
    for i in range(road):
        day = str(i+1)
        days = eval(input("How many days was road " + day + " surveyed?: "))
        total_sum = 0
        for j in range(days):
            number = int(input("How many cars traveled on Day " + str(j+1) + "? "))
            total_sum += number
            avg = total_sum / days
            carnum += number
            caravg = carnum / road
        roundavg = math.ceil(avg * 100) / 100
        print("Road " + str(i+1), "average vehicles per day: ", roundavg)
    roundcaravg = math.ceil(caravg * 100) / 100
    print("Total number of vehicles on all roads: ", carnum)
    print("Average number of vehicles per road: ", roundcaravg)

if __name__ == '__main__':
    main()

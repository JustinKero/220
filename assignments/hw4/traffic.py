"""
Justin Kerosetz
HW 4
"""

def main():
    road = eval(input("How many roads were surveyed?: "))
    carnum = 0
    for i in range(road):
        day = str(i+1)
        days = eval(input("How many days was road " + day + " surveyed?: "))
        total_sum = 0
        for _ in range(days):
            number = float(input("How many cars traveled on Day " + str(_+1) + "? "))
            total_sum += number
            avg = total_sum / days
            carnum += number
            caravg = carnum / road
        print("Road " + str(i+1), "average vehicles per day", avg)
    print("Total number of vehicles on all roads: ", carnum)
    print("Average number of vehicles per road: ", caravg)
if __name__ == '__main__':
    main()
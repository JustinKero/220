import math

def main():
    num1 = eval(input("Enter the interest rate(Ex:15= 15%): "))
    num2 = eval(input("Enter number of days in the billing cycle: "))
    num3 = eval(input("Enter the previous net balance: "))
    num4 = eval(input("Enter the amount paid: "))
    num5 = eval(input("Enter the day of the month it was paid: "))
    print()
    # code for math
    interestrate = (num1/12)
    rate = (interestrate/100)
    netbalance = (num3 * num2)
    daypaid = (num2 - num5)
    amountpaid = (num4 * daypaid)
    balance = (netbalance - amountpaid)
    avgdaily = (balance/num2)
    monthlyinterest = (avgdaily * rate)
    roundinterest = math.ceil(monthlyinterest * 100)/100
    print("Your monthly interest rate is: $", roundinterest)
if __name__ == '__main__':
    main()


stocks = 12

print("Hello, This is a bike rental shop.\n"
      "Please choose the rate and number of bikes")


def order():
    x = 0
    try:
        while x == 0:
            choice = int(input("1- Rent bikes on hourly basis for 5£\n"
                           "2- Rent bikes on daily basis for 20£\n"
                           "3- Rent bikes on weekly basis for 60£\n"))
            if choice == 1 or choice == 2 or choice == 3:
                x = 1
            else:
                continue
    except ValueError:
        print("Please enter a number")

    try:
        while True:
            bikes_ordered = int(input("Please choose the number of bikes you want to rent by maximum of 5: "))
            if bikes_ordered >= 1 and bikes_ordered <= 5:
                break
            else:
                print("please choose a number from 1 to 5")
                continue
    except ValueError:
        print("Please enter a number")

    if choice == 1:
        stock = Hour(stocks, bikes_ordered)
        stock.Hour_charge()



order()
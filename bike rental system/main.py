from base import *
initial_stock = 10
total_orders = 0
result = 0
bike_orders = 0
choice_2 = 0
choice_1 = 0
while True:

    while True:
        choice_1 = int(input("1-Bike rental\n2-Bike return\n"))
        if choice_1 == 1 or choice_1 == 2:
            break
        else:
            print("Please chose one from the above choices! ")
    if choice_1 == 1:
        while True:
            try:
                choice_2 = int(input("1- Rent bikes on hourly basis for 5£\n"
                                     "2- Rent bikes on daily basis for 20£\n"
                                     "3- Rent bikes on weekly basis for 60£\n"))

                if choice_2 == 1 or choice_2 == 2 or choice_2 == 3:
                    break
                else:
                    print("Please choose one of the above choices")
            except ValueError:
                print("Please enter a number for the above choices")

        while True:
            try:
                bike_orders = int(input("Please choose the number of bikes you want to rent by maximum of 5: "))
                if 1 <= bike_orders <= 5:
                    break
                else:
                    print("Please enter a number from 1 to 5!")
            except ValueError:
                print("Please enter a number!")

        if choice_2 == 1:
            while True:
                try:
                    time_used = float(input("for how many hours you want to use them:  "))
                    if 0 < time_used < 24:
                        break
                    else:
                        print("use a value from 0 to 24 or switch to another pay rate!")
                except ValueError:
                    print("Enter a number! ")
            a = Hourly(stock=initial_stock, bikes_ordered=bike_orders, usage=time_used, total_value=result)
            a.hour_charge()
            initial_stock = a.stock
            result = a.total_value
            total_orders += a.bikes_ordered

        elif choice_2 == 2:
            while True:
                try:
                    time_used = float(input("For how long you want to use them: "))
                    if 1 <= time_used <= 7:
                        break
                    else:
                        print("use a value from 1 day to 7 days! ")
                except ValueError:
                    print("Enter a number!")
            a = Daily(stock=initial_stock, bikes_ordered=bike_orders, usage=time_used, total_value=result)
            a.daily_charge()
            initial_stock = a.stock
            result = a.total_value
            total_orders += a.bikes_ordered

        elif choice_2 == 3:
            while True:
                try:
                    time_used = float(input("For how long you want to use them: "))
                    if 1 <= time_used <= 12:
                        break
                    else:
                        print("use a value from 1 week to 12 weeks! ")
                except ValueError:
                    print("Enter a number!")
            a = Weekly(stock=initial_stock, bikes_ordered=bike_orders, usage=time_used, total_value=result)
            a.weekly_charge()
            initial_stock = a.stock
            result = a.total_value
            total_orders += a.bikes_ordered

    elif choice_1 == 2:
        print("Thanks for using our service\nNumber of bikes ordered: ", total_orders, "\nTotal fees will be equal to: ", result)
        break

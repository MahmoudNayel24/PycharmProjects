
class Bike:
    def __init__(self,stock, bikes_ordered, usage, total_value=0):
        self.stock = int(stock)
        self.bikes_ordered = int(bikes_ordered)
        self.total_value = float(total_value)
        self.usage = float(usage)
    def set_stock(self, new_stock):
        self.stock = new_stock

    def get_stock(self):
        return self.stock

class Hourly(Bike):
    def __init__(self, stock, bikes_ordered, usage, total_value):
        super().__init__(stock, bikes_ordered, usage, total_value)
    def hour_charge(self):
        hour = int(5)
        Sum = 0
        if self.bikes_ordered <= self.stock:
            Sum += self.bikes_ordered * hour * int(self.usage)
            self.stock -= self.bikes_ordered
            if self.bikes_ordered >= 3:
                Sum -= Sum * 0.3

        else:
            print("Number of bikes available in  stock is less than the number you ordered")
        self.total_value += Sum
        return self.total_value


class Daily(Bike):
    def __init__(self, stock, bikes_ordered, usage, total_value):
        super().__init__(stock, bikes_ordered, usage, total_value)

    def daily_charge(self):
        daily = 20
        Sum = 0
        if self.bikes_ordered <= self.stock:
            Sum += self.bikes_ordered * daily * self.usage
            self.stock -= self.stock
            if self.bikes_ordered >= 3:
                Sum -= Sum * 0.3
        else:
            print("Number of bikes available in  stock is less than the number you ordered")
        self.total_value += Sum
        return self.total_value


class Weekly(Bike):
    def __init__(self, stock, bikes_ordered, usage, total_value):
        super().__init__(stock, bikes_ordered, usage, total_value)

    def weekly_charge(self):
        weekly = 60
        Sum = 0
        if self.bikes_ordered <= self.stock:
            Sum += self.bikes_ordered * weekly * self.usage
            self.stock -= self.stock
            if self.bikes_ordered >= 3:
                Sum -= Sum * 0.3
        else:
            print("Number of bikes available in  stock is less than the number you ordered")
        self.total_value += Sum
        return self.total_value

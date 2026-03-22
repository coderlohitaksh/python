class Computer :
    def __init__ (self):
        self.__maxprice = 200000

    def sell(self):
        print("The selling price is {}".format(self.__maxprice))

    def setMaxprice(self , price):
        self.max_price = price

c = Computer()
c.sell()
c.__maxprice = 200000
c.sell()
c.setMaxprice = 200000
c.sell()
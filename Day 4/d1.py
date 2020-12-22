class Apparel:
    counter = 100

    def __init__(self, price, item_type):
        self.__item_id = item_type[0].upper() + str(Apparel.counter + 1)
        self.__price = price
        self.__item_type = item_type
        Apparel.counter += 1

    def get_item_id(self):
        return self.__item_id

    def get_price(self):
        return self.__price

    def get_item_type(self):
        return self.__item_type

    def set_price(self, price):
        self.__price = price

    def calculate_price(self):
        self.__price *= 1.05


class Cotton(Apparel):
    def __init__(self, price, discount):
        super(Cotton, self).__init__(price, "Cotton")
        self.__discount = discount

    def calculate_price(self):
        super(Cotton, self).calculate_price()
        price = super(Cotton, self).get_price()
        price *= (100 - self.__discount) / 100
        price *= 1.05
        super(Cotton, self).set_price(price)

    def get_discount(self):
        return self.__discount


class Silk(Apparel):
    def __init__(self, price):
        super(Silk, self).__init__(price, "Silk")
        self.__points = 0

    def get_points(self):
        return self.__points

    def calculate_price(self):
        super(Silk, self).calculate_price()
        price = super(Silk, self).get_price()
        if price > 10000:
            self.__points += 10
        else:
            self.__points += 3

        price *= 1.10
        super(Silk, self).set_price(price)


c = Cotton(1000, 10)
print(c.get_item_id())
s = Silk(1000)
print(s.get_item_id())
c.calculate_price()
print(c.get_price())
s.calculate_price()
print(s.get_price())

flower_name = ['orchid', 'rose', 'jasmine']
level = [15, 25, 40]


class Flower:
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None

    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name.lower()

    def get_flower_name(self):
        return self.__flower_name

    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg

    def get_price_per_kg(self):
        return self.__price_per_kg

    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available

    def get_stock_available(self):
        return self.__stock_available

    def validate_flower(self):
        if self.__flower_name in flower_name:
            return True
        else:
            return False

    def validate_stock(self, required_quantity):
        if self.__stock_available >= required_quantity:
            return True
        else:
            return False

    def sell_flower(self, required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available -= required_quantity

    def check_level(self):
        if self.validate_flower():
            flower_level = level[flower_name.index(self.__flower_name)]
            if self.__stock_available < flower_level:
                return True
        return False


flower = Flower()
flower.set_flower_name('Rose')
flower.set_stock_available(100)
flower.set_price_per_kg(200)
print(flower.validate_stock(20))
print(flower.sell_flower(40))
print(flower.check_level())

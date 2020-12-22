from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass


class Furniture(Product):
    pass


class Mobile(Product):
    def return_policy(self):
        print("All mobiles must be returned within 10 days of purchase")


class Shoe(Product):
    def return_policy(self):
        print("All shoes must be returned within 7 days of purchase")


from abc import ABCMeta, abstractmethod


class Parent(metaclass=ABCMeta):
    def __init__(self):
        self.num = 5

    @abstractmethod
    def show(self):
        pass


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var = 10

    def show(self):
        print(self.num)
        print(self.__var)


obj = Child()
obj.show()

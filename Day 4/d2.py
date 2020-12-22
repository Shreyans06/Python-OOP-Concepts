class FruitInfo:
    __fruit_name_list = ['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    __fruit_price_list = [200, 80, 70, 110, 60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            return FruitInfo.__fruit_price_list[FruitInfo.__fruit_name_list.index(fruit_name)]
        else:
            return -1

    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list


class Customer:
    def __init__(self, customer_name, cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type

    def get_customer_name(self):
        return self.__customer_name

    def get_cust_type(self):
        return self.__cust_type


class Purchase:
    __counter = 101

    def __init__(self, customer, fruit_name, quantity):
        self.__purchase_id = "P" + str(Purchase.__counter)
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
        Purchase.__counter += 1

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_quantity(self):
        return self.__quantity

    def calculate_price(self):
        if FruitInfo.get_fruit_price(self.__fruit_name) != -1:
            final_fruit_price = self.__quantity * FruitInfo.get_fruit_price(self.__fruit_name)
            if FruitInfo.get_fruit_price(self.__fruit_name) == max(
                    FruitInfo.get_fruit_price_list()) and self.__quantity > 1:
                final_fruit_price = (100 - 2) * final_fruit_price / 100
            if FruitInfo.get_fruit_price(self.__fruit_name) == min(
                    FruitInfo.get_fruit_price_list()) and self.__quantity >= 5:
                final_fruit_price = (100 - 5) * final_fruit_price / 100
            if self.__customer.get_cust_type() == "wholesale":
                final_fruit_price = (100 - 10) * final_fruit_price / 100
            return final_fruit_price
        else:
            return -1


cust1 = Customer("Shreyans", "wholesale")
cust2 = Customer("Naman", "Retail")

purchase1 = Purchase(cust1, "Appaae", 10)
purchase2 = Purchase(cust2, "Guava", 5)

print(purchase1.calculate_price())
print(purchase2.calculate_price())

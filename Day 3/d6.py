class Item:
    def __init__(self, item_id, description, price_per_quantity):
        self.__item_id = item_id.lower()
        self.__description = description.lower()
        self.__price_per_quantity = price_per_quantity

    def get_item_id(self):
        return self.__item_id

    def get_description(self):
        return self.__description

    def get_price_per_quantity(self):
        return self.__price_per_quantity


class Customer:
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.__payment_status = None

    def get_customer_name(self):
        return self.__customer_name

    def get_payment_status(self):
        return self.__payment_status

    def pays_bill(self, bill):
        self.__payment_status = "Paid"
        print(self.get_customer_name())
        print(bill.get_bill_id(), bill.get_bill_amount())


class Bill:
    counter = 1000

    def __init__(self):
        self.__bill_id = 0
        self.__bill_amount = 0

    def get_bill_id(self):
        return self.__bill_id

    def get_bill_amount(self):
        return self.__bill_amount

    def generate_bill_amount(self, item_quantity, items):
        if not self.__bill_amount:
            for key, value in item_quantity.items():
                for item in items:
                    if item.get_item_id() == key.lower():
                        self.__bill_amount += value * item.get_price_per_quantity()
                        continue
            if self.__bill_amount > 0:
                self.__bill_id = "B" + str(Bill.counter + 1)
                Bill.counter += 1


item1 = Item('IR987', "Sunfeast Marie", 100.0)
item2 = Item('ir658', "Kellogs Oats", 151.0)
item3 = Item('Ir346', "Maggie Noodles", 35.75)
item4 = Item('iR234', "Kissan Jam", 100.0)
item5 = Item('IR123', "Nescafe", 55.5)
item6 = Item('IR111', "Milk", 100.0)
list_of_items = [item1, item2, item3, item4, item5, item6]
c1 = Customer("Shreyans")

b1 = Bill()
item_quantity = {'IR658': 4, 'IR123': 2, 'IR346': 2, 'Ir987': 3}

b1.generate_bill_amount(item_quantity, list_of_items)
c1.pays_bill(b1)

class Purchase:
    list_of_items = ['Apple', 'Biscuits', 'Chocolates', 'Jam', 'Butter', 'Milk', 'Soap', 'Hand Sanitizer']
    list_of_count_of_each_item_sold = [0] * len(list_of_items)

    def __init__(self):
        self.__items_purchased = []
        self.__item_on_offer = None

    def get_items_purchased(self):
        return self.__items_purchased

    def get_item_on_offer(self):
        return self.__item_on_offer

    def provide_offer(self):
        if "Soap" in self.__items_purchased:
            Purchase.list_of_count_of_each_item_sold[Purchase.list_of_items.index("Hand Sanitizer")] += 1
            self.__item_on_offer = "HAND SANITIZER"

    def sell_items(self, list_of_items_to_be_purchased):
        for item in list_of_items_to_be_purchased:
            if item.title() in Purchase.list_of_items:
                Purchase.list_of_count_of_each_item_sold[Purchase.list_of_items.index(item.title())] += 1
                self.__items_purchased += [item.title()]

        print(self.__items_purchased)
        if "Soap" in list_of_items_to_be_purchased:
            self.provide_offer()

    @staticmethod
    def find_total_items_sold():
        return sum(Purchase.list_of_count_of_each_item_sold)


purchase = Purchase()
purchase.sell_items(["JAM", "CHOcolates", "Ghee", "Soap", "Hand Sanitizer"])
print(purchase.find_total_items_sold())

class Customer:
    def __init__(self, customer_name, quantity):
        self.__customer_name = customer_name
        self.__quantity = quantity

    def get_customer_name(self):
        return self.__customer_name

    def get_quantity(self):
        return self.__quantity

    def validate_quantity(self):
        if 1 <= self.__quantity <= 5:
            return True
        else:
            return False


class Pizzaservice:
    counter = 100

    def __init__(self, customer, pizza_type, additional_topping):
        self.__customer = customer
        self.__pizza_type = pizza_type
        self.__additional_topping = additional_topping
        self.pizza_cost = 0
        self.__service_id = None

    def get_service_id(self):
        return self.__service_id

    def get_pizza_type(self):
        return self.__pizza_type

    def get_customer(self):
        return self.__customer

    def get_additional_topping(self):
        return self.__additional_topping

    def validate_pizza_type(self):
        if self.__pizza_type.lower() in ["small", "medium"]:
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            if self.__pizza_type.lower() == "small":
                self.__service_id = "S" + str(Pizzaservice.counter + 1)
                Pizzaservice.counter += 1
                if self.__additional_topping:
                    self.pizza_cost = self.__customer.get_quantity() * 150 + self.__customer.get_quantity() * 35
                else:
                    self.pizza_cost = self.__customer.get_quantity() * 150
            elif self.__pizza_type.lower() == "medium":
                self.__service_id = "M" + str(Pizzaservice.counter + 1)
                Pizzaservice.counter += 1
                if self.__additional_topping:
                    self.pizza_cost = self.__customer.get_quantity() * 200 + self.__customer.get_quantity() * 50
                else:
                    self.pizza_cost = self.__customer.get_quantity() * 200
        else:
            self.pizza_cost = -1


class Doordelivery(Pizzaservice):
    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        super(Doordelivery, self).__init__(customer, pizza_type, additional_topping)
        self.__distance_in_kms = distance_in_kms
        self.__delivery_charge = 0

    def get_delivery_charge(self):
        return self.__delivery_charge

    def get_distance_in_kms(self):
        return self.__distance_in_kms

    def validate_distance_in_kms(self):
        if 1 <= self.__distance_in_kms <= 10:
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super(Doordelivery, self).calculate_pizza_cost()
            if self.pizza_cost != -1:
                for distance in range(1, self.__distance_in_kms + 1):
                    if distance <= 5:
                        self.pizza_cost += 5
                    else:
                        self.pizza_cost += 7
        else:
            self.pizza_cost = -1


customer1 = Customer("Shreyans", 4)

pizza = Pizzaservice(customer1, "sMALL", True)
pizza.calculate_pizza_cost()
print(pizza.get_service_id())
print(pizza.pizza_cost)

delivery = Doordelivery(customer1, "sMALL", True, 5)
delivery.calculate_pizza_cost()
print(delivery.pizza_cost)

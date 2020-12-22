class Vehicle:
    def __init__(self):
        self.mileage = None
        self.fuel_left = None

    def identify_distance_that_can_be_travelled(self):
        if self.fuel_left <= 5:
            return 0
        else:
            distance = (self.fuel_left - 5) * self.mileage
            return distance

    def identify_distance_travelled(self, initial_fuel):
        if initial_fuel > self.fuel_left:
            distance = (initial_fuel - self.fuel_left) * self.mileage
            return distance
        return 0


v1 = Vehicle()
v1.mileage = 20
v1.fuel_left = 12
print(v1.identify_distance_that_can_be_travelled())
print(v1.identify_distance_travelled(10))


class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location


list_of_customers = [Customer(101, 'Mark', 'US'),
                     Customer(102, 'Jane', 'Japan'),
                     Customer(103, 'Kumar', 'India')]

dict_of_customer = {}

for c in list_of_customers:
    dict_of_customer[c.cust_id] = c.location

print(dict_of_customer)

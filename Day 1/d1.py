
def check_type(veh_type):
    if veh_type in ['Two Wheeler', 'Four Wheeler']:
        return 1
    else:
        return 0


class Vehicle:
    def __init__(self):
        self.__vehicle_id = None
        self.__vehicle_cost = None
        self.__vehicle_type = None
        self.__premium_amount = None

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost

    def set_vehicle_type(self, vehicle_type):
        if check_type(vehicle_type):
            self.__vehicle_type = vehicle_type
        else:
            print("Invalid vehicle details")

    def set_premium_amount(self, premium_amount):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount = 0.02 * premium_amount
        if self.__vehicle_type == "Four Wheeler":
            self.__premium_amount = 0.06 * premium_amount
        self.display_vehicle_details()

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_vehicle_cost(self):
        return self.__vehicle_cost

    def get_vehicle_type(self):
        return self.__vehicle_type

    def get_premium_amount(self):
        return self.__premium_amount

    def calculate_premium(self):
        self.set_premium_amount(self.__vehicle_cost)
        return self.__premium_amount

    def display_vehicle_details(self):
        print(str(self.__vehicle_id), " is a ", self.__vehicle_type, " costing ", str(
            self.__vehicle_cost), " with a premium ", str(self.__premium_amount))

    id = property(get_vehicle_id, set_vehicle_id)
    type = property(get_vehicle_type, set_vehicle_type)
    cost = property(get_vehicle_cost, set_vehicle_cost)


v1 = Vehicle()
v1.id = 10
v1.type = "Two Wheeler"
v1.cost = 105000
v1.calculate_premium()

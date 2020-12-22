from abc import ABCMeta, abstractmethod


class Logistics(metaclass=ABCMeta):
    __counter = None

    def __init__(self, start_reading, end_reading):
        self.__consumer_id = None
        self.__start_reading = start_reading
        self.__end_reading = end_reading

    def get_consumer_id(self):
        return self.__consumer_id

    def get_start_reading(self):
        return self.__start_reading

    def get_end_reading(self):
        return self.__end_reading

    def validate_meter_reading(self):
        if self.__start_reading < self.__end_reading:
            return True
        else:
            return False

    def generate_consumer_id(self):
        if Logistics.__counter is None:
            Logistics.__counter = 7001
        self.__consumer_id = Logistics.__counter
        Logistics.__counter += 1
        # implement the code to generate the consumer id

    @abstractmethod
    def calculate_bill_amount(self):
        pass


class PassengerLogistics(Logistics):
    __list_vehicle = ["BMW", "TOYOTA", "FORD"]
    __list_minimum_charge = [4250, 2570,
                             1205]
    # these lists are storing vehicle type, minimum charge, rate per kilometer for first hundred and rate per kilometer for rest of distance
    __list_charge_for_hundred = [32, 20, 12]  # there is a one to one correspondence
    __list_charge_after_hundred = [20, 15, 11]

    def __init__(self, vehicle_type, start_reading, end_reading):
        super().__init__(start_reading, end_reading)
        self.__vehicle_type = vehicle_type

    def get_vehicle_type(self):
        return self.__vehicle_type

    def validate_vehicle_type(self):
        for index in range(0, len(PassengerLogistics.__list_vehicle)):
            if PassengerLogistics.__list_vehicle[index] == self.__vehicle_type:
                return index
        return -1

    def calculate_bill_amount(self):
        # implement the code to calculate the bill amount according to the requirement
        if self.validate_vehicle_type() != -1 and self.validate_meter_reading():
            self.generate_consumer_id()
            distance_travelled = self.get_end_reading() - self.get_start_reading()
            bill_amount = 0
            if distance_travelled <= 100:
                charge_per_km = PassengerLogistics.__list_charge_for_hundred[
                    PassengerLogistics.__list_vehicle.index(self.__vehicle_type)]

                bill_amount = distance_travelled * charge_per_km


            elif distance_travelled > 100:
                charge_per_km = PassengerLogistics.__list_charge_after_hundred[
                    PassengerLogistics.__list_vehicle.index(self.__vehicle_type)]

                bill_amount = (distance_travelled - 100) * charge_per_km
                bill_amount += 100 * PassengerLogistics.__list_charge_for_hundred[
                    PassengerLogistics.__list_vehicle.index(self.__vehicle_type)]

            if bill_amount < PassengerLogistics.__list_minimum_charge[
                PassengerLogistics.__list_vehicle.index(self.__vehicle_type)]:
                bill_amount = PassengerLogistics.__list_minimum_charge[
                    PassengerLogistics.__list_vehicle.index(self.__vehicle_type)]

            bill_amount = bill_amount + 0.05 * bill_amount
            return bill_amount
        else:
            return -1


class GoodsLogistics(Logistics):
    __carrier_dict = {"TATA": 20, "EICHER": 30,
                      "FORCE": 35}  # stores the carrier type and rate per kilometer for 1000kg

    def __init__(self, carrier_type, goods_weight, start_reading, end_reading):
        super().__init__(start_reading, end_reading)
        self.__carrier_type = carrier_type
        self.__goods_weight = goods_weight

    def get_carrier_type(self):
        return self.__carrier_type

    def get_goods_weight(self):
        return self.__goods_weight

    def validate_carrier_type(self):
        for carrier in GoodsLogistics.__carrier_dict:
            if carrier == self.__carrier_type:
                return True
        return False

    def calculate_bill_amount(self):
        if self.validate_carrier_type():
            if self.validate_meter_reading():
                self.generate_consumer_id()
                total_distance = self.get_end_reading() - self.get_start_reading()
                if self.__goods_weight <= 1000:
                    charge_per_kilometer = self.__carrier_dict[self.__carrier_type]
                elif 1000 < self.__goods_weight <= 2000:
                    charge_per_kilometer = 2 * self.__carrier_dict[self.__carrier_type]
                elif 2000 < self.__goods_weight <= 3000:
                    charge_per_kilometer = 4 * self.__carrier_dict[self.__carrier_type]
                else:
                    charge_per_kilometer = 200
                bill_amount = total_distance * charge_per_kilometer
                bill_amount = bill_amount + (bill_amount * 0.1) + 2000
                return bill_amount
            else:
                return -1
        else:
            return -1


passenger_logistic = PassengerLogistics("BMW", 299, 400)
bill_amount = passenger_logistic.calculate_bill_amount()
if bill_amount == -1:
    print("Invalid vehicle type or meter reading ")
else:
    print("Consumer id    :", passenger_logistic.get_consumer_id())
    print("Start reading  :", passenger_logistic.get_start_reading())
    print("End reading    :", passenger_logistic.get_end_reading())
    print("Total Amount   :", bill_amount)
print("------------------------------------------------------------")
goods_logistic = GoodsLogistics("FORCE", 3000, 300, 400)
bill_amount = goods_logistic.calculate_bill_amount()
if bill_amount == -1:
    print("Invalid career type or meter reading ")
else:
    print("Consumer id    :", goods_logistic.get_consumer_id())
    print("Goods weight   :", goods_logistic.get_goods_weight())
    print("Start reading  :", goods_logistic.get_start_reading())
    print("End reading    :", goods_logistic.get_end_reading())
    print("Total Amount   :", bill_amount)

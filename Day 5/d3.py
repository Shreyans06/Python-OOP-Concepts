from abc import abstractmethod, ABCMeta


class Customer(metaclass=ABCMeta):
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.bill_amount = 0
        self.bill_id = 0

    @abstractmethod
    def calculate_bill_amount(self):
        pass

    def get_customer_name(self):
        return self.__customer_name


class OccasionalCustomer(Customer):
    __counter = 1000

    def __init__(self, customer_name, distance_in_kms):
        super(OccasionalCustomer, self).__init__(customer_name)
        self.bill_id = "O" + str((OccasionalCustomer.__counter + 1))
        self.__distance_in_kms = distance_in_kms
        OccasionalCustomer.__counter += 1

    def get_distance_in_kms(self):
        return self.__distance_in_kms

    def validate_distance_in_kms(self):
        if 1 <= self.__distance_in_kms <= 5:
            return True
        else:
            return False

    def calculate_bill_amount(self):
        if self.validate_distance_in_kms():
            tiffin_cost = 50
            delivery_charges = 0
            if 1 <= self.__distance_in_kms <= 2:
                delivery_charges = self.__distance_in_kms * 5
            elif 2 < self.__distance_in_kms <= 5:
                delivery_charges = self.__distance_in_kms * 7.5
            self.bill_amount = tiffin_cost + delivery_charges
            return self.bill_amount
        else:
            self.bill_amount = -1
            return self.bill_amount


class RegularCustomer(Customer):
    __counter = 100

    def __init__(self, customer_name, no_of_tiffin):
        super(RegularCustomer, self).__init__(customer_name)
        self.bill_id = "R" + str((RegularCustomer.__counter + 1))
        self.__no_of_tiffin = no_of_tiffin
        RegularCustomer.__counter += 1

    def get_no_of_tiffin(self):
        return self.__no_of_tiffin

    def validate_no_of_tiffin(self):
        if 1 <= self.__no_of_tiffin <= 7:
            return True
        else:
            return False

    def calculate_bill_amount(self):
        if self.validate_no_of_tiffin():
            self.bill_amount = 50 * self.__no_of_tiffin * 7
            return self.bill_amount
        else:
            self.bill_amount = -1
            return self.bill_amount


occasional_cust = OccasionalCustomer("Naman", 5)
regular_cust = RegularCustomer("Shreyans", 7)
print(occasional_cust.calculate_bill_amount())
print(occasional_cust.bill_amount)

print(regular_cust.bill_id)
regular_cust1 = RegularCustomer("Shreyans", 7)
regular_cust2 = RegularCustomer("Shreyans", 7)
regular_cust3 = RegularCustomer("Shreyans", 7)
print(regular_cust3.bill_id)
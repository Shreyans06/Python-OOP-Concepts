from abc import ABCMeta, abstractmethod

Base_pack_name = {"Silver": 350.00, "Gold": 440.00, "Platinum": 560.00}


class DirectToHomeService(metaclass=ABCMeta):
    __counter = 101

    def __init__(self, consumer_name):
        self.__consumer_number = DirectToHomeService.__counter
        self.__consumer_name = consumer_name
        DirectToHomeService.__counter += 1

    def get_consumer_name(self):
        return self.__consumer_name

    def get_consumer_number(self):
        return self.__consumer_number

    @abstractmethod
    def calculate_monthly_rent(self):
        pass


class BasePackage(DirectToHomeService):
    def __init__(self, consumer_name, base_pack_name, subscription_period):
        super(BasePackage, self).__init__(consumer_name)
        self.__base_pack_name = base_pack_name
        self.__subscription_period = subscription_period

    def get_base_pack_name(self):
        return self.__base_pack_name

    def get_subscription_period(self):
        return self.__subscription_period

    def validate_base_pack_name(self):
        if self.__base_pack_name not in Base_pack_name.keys():
            self.__base_pack_name = "Silver"
            print("Base package name is incorrect, set to Silver")

    def calculate_monthly_rent(self):
        if 1 <= self.__subscription_period <= 24:
            self.validate_base_pack_name()

            monthly_rent = Base_pack_name[self.__base_pack_name]

            if self.__subscription_period > 12:
                discount = monthly_rent
            else:
                discount = 0

            final_monthly_rent = ((monthly_rent * self.__subscription_period) - discount) / self.__subscription_period

            return final_monthly_rent
        else:
            return -1


base1 = BasePackage("Shreyans", "Gold", 10)
print(base1.calculate_monthly_rent())

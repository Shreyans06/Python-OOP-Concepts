class Bill:
    def __init__(self, bill_id, patient_name):
        self.__bill_id = bill_id
        self.__patient_name = patient_name
        self.__bill_amount = 0

    def get_bill_id(self):
        return self.__bill_id

    def get_patient_name(self):
        return self.__patient_name

    def get_bill_amount(self):
        return self.__bill_amount

    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        medicine_price = [a * b for a, b in zip(quantity_list, price_list)]
        self.__bill_amount = consultation_fees + sum(medicine_price)
        print(self.get_bill_id())
        print(self.get_patient_name())
        print(self.get_bill_amount())


b1 = Bill(1, "Shreyans")
b1.calculate_bill_amount(100, [1, 3, 4], [20, 40, 10])

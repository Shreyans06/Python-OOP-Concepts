dog_breed_price = {"Labrador Retriever": 800, "German Shepherd": 1230, "Beagle": 650}


class Dog:
    counter = 100
    dog_breed_dict = {"Labrador Retriever": 10, "German Shepherd": 6, "Beagle": 4}

    def __init__(self, breed_list, accessories_required):
        self.__dog_id_list = []
        self.__breed_list = breed_list
        self.__price = 0
        self.__accessories_required = accessories_required

    def get_dog_id_list(self):
        return self.__dog_id_list

    def get_breed_list(self):
        return self.__breed_list

    def get_price(self):
        return self.__price

    def get_accessories_required(self):
        return self.__accessories_required

    def validate_breed(self):
        for breed in self.__breed_list:

            if breed in Dog.dog_breed_dict.keys():
                continue
            else:
                return False
        return True

    def validate_quantity(self):
        for breed in self.__breed_list:
            if Dog.dog_breed_dict.get(breed) >= 1:
                continue
            else:
                return False
        return True

    def generate_dog_id(self, breed):
        Dog.counter += 1
        return breed[0] + str(Dog.counter)

    def get_dog_price(self, breed):
        return dog_breed_price[breed]

    def calculate_total_price(self):
        if self.validate_breed():

            if self.validate_quantity():

                for breed in self.__breed_list:
                    Dog.dog_breed_dict[breed] -= 1
                    self.__dog_id_list += [self.generate_dog_id(breed)]
                    self.__price += dog_breed_price[breed]

                if self.__accessories_required:
                    self.__price += 350

                if self.__price > 1500:
                    self.__price = (100 - 5) * self.__price / 100
            else:
                return -2
        else:
            return -1


dog = Dog(["Beagle", "Labrador Retriever"], True)
dog.calculate_total_price()
print(dog.get_dog_id_list())
print(dog.get_price())

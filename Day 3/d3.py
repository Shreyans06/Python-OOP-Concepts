class Parrot:
    __counter = 7000

    def __init__(self, name, color):
        self.__unique_number = Parrot.__counter + 1
        self.__name = name
        self.__color = color
        Parrot.__counter += 1

    def get_unique_number(self):
        return self.__unique_number

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color


p1 = Parrot("Shreyans", "Blue")
p2 = Parrot("Naman", "Red")

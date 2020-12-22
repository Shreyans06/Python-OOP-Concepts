# OOPR-Exer-8
class Juggler:
    def __init__(self, name):
        self.__name = name
        self.__juggling_item = None

    def juggles(self, juggling_item):
        # write the code to make the juggler juggle
        self.__juggling_item = juggling_item
        print(self.__name + "is juggling with " + self.__juggling_item.get_name())


class JugglingItem:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


j1 = Juggler("Jack Bremlov")
ji = JugglingItem("knives")
ji1 = JugglingItem("balls")
j2 = Juggler("Anthony Gatto")

j1.juggles(ji)
j2.juggles(ji1)


class Foo:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.num2 = num2

    def __str__(self):
        return str(self.__dict__)


f1 = Foo(10, 20)
f2 = Foo(20, 30)
f3 = Foo(30, 40)
print(f1, f2, f3)

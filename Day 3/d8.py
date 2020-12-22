destination = ['mumbai', 'chennai', 'pune', 'kolkata']


class Ticket:
    counter = 0

    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__source = source
        self.__destination = destination
        self.__ticket_id = 0

    def get_ticket_id(self):
        return self.__ticket_id

    def get_passenger_name(self):
        return self.__passenger_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def validate_source_destination(self):
        if str(self.__source).lower() == 'delhi' and str(self.__destination).lower() in destination:
            return True
        else:
            return False

    def generate_ticket(self):
        if self.validate_source_destination():
            self.__ticket_id = self.__source[0] + self.__destination[0] + "{:02}".format(Ticket.counter + 1)
            Ticket.counter += 1
        else:
            self.__ticket_id = None


t = Ticket("Shreyans", "Delhi", "Mumbai")
t.generate_ticket()
print(t.get_ticket_id())
print(t.get_passenger_name())
print(t.get_source())
print(t.get_destination())

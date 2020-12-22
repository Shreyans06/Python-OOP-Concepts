class Multiplex:
    __list_movie_name = ["movie1", "movie2"]
    __list_total_tickets = [100, 60]
    __list_last_seat_number = [None, None]
    __list_ticket_price = [150, 200]

    def __init__(self):
        self.__seat_numbers = None
        self.__total_price = None

    def calculate_ticket_price(self, movie_index, number_of_tickets):
        self.__total_price = Multiplex.__list_ticket_price[movie_index] * number_of_tickets

    @staticmethod
    def check_seat_availability(movie_index, number_of_tickets):
        if Multiplex.__list_total_tickets[movie_index] < number_of_tickets:
            return False
        else:
            return True

    def get_total_price(self):
        return self.__total_price

    def get_seat_numbers(self):
        return self.__seat_numbers

    def book_ticket(self, movie_name, number_of_tickets):
        if movie_name not in Multiplex.__list_movie_name:
            return 0
        if not self.check_seat_availability(Multiplex.__list_movie_name.index(movie_name),
                                            number_of_tickets):
            return -1
        else:
            self.__seat_numbers = self.generate_seat_number(Multiplex.__list_movie_name.index(movie_name),
                                                            number_of_tickets)
            self.calculate_ticket_price(Multiplex.__list_movie_name.index(movie_name), number_of_tickets)

    def generate_seat_number(self, movie_index, number_of_tickets):
        self.__seat_numbers = []
        last_seat = 0
        Multiplex.__list_total_tickets[movie_index] -= number_of_tickets
        if Multiplex.__list_last_seat_number[movie_index]:
            last_seat = int(Multiplex.__list_last_seat_number[movie_index][3:])
        for seats in range(last_seat, last_seat + number_of_tickets):
            if Multiplex.__list_movie_name[movie_index] == "movie1":
                self.__seat_numbers.append("M1-" + str(seats + 1))
            elif Multiplex.__list_movie_name[movie_index] == "movie2":
                self.__seat_numbers.append("M2-" + str(seats + 1))

        Multiplex.__list_last_seat_number[movie_index] = self.__seat_numbers[-1]
        return self.__seat_numbers


booking1 = Multiplex()
status = booking1.book_ticket("movie1", 10)
if status == 0:
    print("invalid movie name")
elif status == -1:
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())

print("-----------------------------------------------------------------------------")

booking2 = Multiplex()
status = booking2.book_ticket("movie2", 6)
if status == 0:
    print("invalid movie name")
elif status == -1:
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())

print("-----------------------------------------------------------------------------")

booking3 = Multiplex()
status = booking3.book_ticket("movie2", 6)
if status == 0:
    print("invalid movie name")
elif status == -1:
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking3.get_seat_numbers())
    print("Total amount to be paid:", booking3.get_total_price())

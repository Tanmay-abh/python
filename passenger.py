# Class 1: PassengerDetails
class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_passenger_info(self):
        print(f"Passenger Name: {self.name}")
        print(f"Age: {self.age}")


# Class 2: TicketDetails
class TicketDetails:
    def __init__(self, ticket_number, seat_number):
        self.ticket_number = ticket_number
        self.seat_number = seat_number

    def display_ticket_info(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Seat Number: {self.seat_number}")


# Class 3: Booking (inherits from both PassengerDetails and TicketDetails)
class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticket_number, seat_number):
        PassengerDetails.__init__(self, name, age)
        TicketDetails.__init__(self, ticket_number, seat_number)

    def display_booking_info(self):
        print("=== Booking Details ===")
        self.display_passenger_info()
        self.display_ticket_info()


# Creating an object and displaying information
booking1 = Booking("Tanmay", 35, "TK123456", "12A")
booking1.display_booking_info()

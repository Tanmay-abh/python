# Base class: Flight
class Flight:
    def __init__(self, flight_number, airline):
        self.flight_number = flight_number
        self.airline = airline

    def display_info(self):
        print(f"Flight Number: {self.flight_number}")
        print(f"Airline: {self.airline}")


# Derived class: ScheduledFlight
class ScheduledFlight(Flight):
    def __init__(self, flight_number, airline, departure_time, arrival_time):
        super().__init__(flight_number, airline)
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def display_info(self):
        super().display_info()
        print(f"Departure Time: {self.departure_time}")
        print(f"Arrival Time: {self.arrival_time}")


# Create a ScheduledFlight object and display its information
scheduled_flight = ScheduledFlight("AI202", "Air India", "10:30 AM", "2:45 PM")
scheduled_flight.display_info()

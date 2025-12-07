from abc import ABC, abstractmethod

class BookingSystem(ABC):
    @abstractmethod
    def book_flight(self, passager_name , destination):
        pass


class CustomerBooking(BookingSystem):
    def book_flight(self, passager_name , destination):
        print(f" Flight Booked for {passager_name} to {destination}")
        print("Seat assigned and the payment has been processes=d")

class PilotAcces(BookingSystem):
    def book_flight(self, flight_number, schedule):
        print(f" Flight Booked for {flight_number} to {schedule}")
        print("Passenger details hidden.")



customer = CustomerBooking()
customer.book_flight(passager_name="Iza", destination="London")

pilot = PilotAcces()
pilot.book_flight(1001, "10:00AM - Bucharest to London")
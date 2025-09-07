from datetime import datetime

class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_drivers(self, driver):
        self.drivers.append(driver)

    def __repr__(self):
        return f"Company name: {self.company_name} with Riders: {len(self.riders)} and Drivers: {len(self.drivers)}"

class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.start_time = None
        self.end_time = None
        self.driver = None
        self.rider = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self):
        return f"Ride details: start location - {self.start_location} and end location - {self.end_location}"


class RideRequest:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location


class RideMatching:
    def __init__(self, drivers):
        self.available_drivers = drivers
    
    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            print("Looking for drivers...")
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            # set ride to driver
            driver.accept_ride(ride)

            return ride
        else:
            print("No driver in your location right now.")
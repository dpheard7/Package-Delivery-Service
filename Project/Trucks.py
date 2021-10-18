from datetime import timedelta, datetime, date


# Creates a truck object
class DeliveryTruck:
    packages = []

    # Constructor
    # ORIGINAL
    def __init__(self, truck_id, truck_location, departure_time, mileage, package_list=[]):
        self.truck_id = truck_id
        self.truck_location = ""
        self.destination = ""
        self.destination_distance = float()
        self.departure_time = departure_time
        self.mileage = mileage
        self.package_list = package_list
        self.speed = 18
        self.capacity = 16
        self.truck_time = ""

    def get_truck_location(self):
        return self.truck_location

    def set_truck_location(self):
        self.truck_location = self.truck_location

# def deliver_packages(truck, time):
#     i = 0
#     truck_mileage = 0
#     departure_time = truck.departure_time
#     starting_distance = float(100)

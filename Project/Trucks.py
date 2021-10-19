"""
Model for Truck class used to build package objects. Accepts parameters of truck details inserted later into the program.
Operations are constant.
Time: O(1)
Space: O(1)
"""
class DeliveryTruck:
    packages = []

    # Constructor
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
        self.return_time = ""
        self.truck_status = ""
        self.time_list = []



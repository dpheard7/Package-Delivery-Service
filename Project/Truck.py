from datetime import timedelta, datetime, date


class DeliveryTruck:
    driving_distance = 0
    packages = []

    def __init__(self, truck_id, truck_location, departure_time, mileage, package_list=[]):
        self.truck_id = truck_id
        self.truck_location = truck_location
        self.departure_time = departure_time
        self.mileage = mileage
        self.package_list = package_list
        self.speed = 18
        self.capacity = 16
        self.truck_list = []
        self.truck_time = datetime.now()
        self.location = ""


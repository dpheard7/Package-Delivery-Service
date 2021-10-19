class Package:

    def __init__(self, package_id, address, city, state, postal, deadline, weight, notes, status, truck_id):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.postal = postal
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = "At hub"
        self.delivery_time = None
        self.hub_departure = ""
        self.miles = 0.0
        self.truck_id = truck_id

    def __str__(self):
        return f"""
        {self.address}
        """

        # ORIGINAL
        # return f"""
        # Package ID: {self.package_id}
        # Address: {self.address}
        # Truck: {self.truck_id}
        # """

    def get_package_address(self):
        return self.address

    def set_package_address(self, new_address):
        self.address = self.address

    def fix_address(self):
        self.address = "410 S State St"
        self.city = "Salt Lake City"
        self.postal = "84111"

    def get_package_stats(self):
        return self.status

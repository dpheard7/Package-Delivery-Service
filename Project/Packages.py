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
        self.status = ""
        self.delivery_time = ""
        self.truck_id = truck_id

    def __str__(self):
        return f"""
        Package ID: {self.package_id}
        Address: {self.address}
        Truck: {self.truck_id}
        """

    def get_package_address(self):
        return self.address

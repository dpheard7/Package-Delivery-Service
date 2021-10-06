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
        self.delivery_time = None
        self.truck_id = truck_id

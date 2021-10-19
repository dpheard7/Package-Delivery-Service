
class Package:
    """
    Model for Package class used to build package objects. Accepts parameters of package details read from csv.
    Time: O(1)
    Space: O(1)
    """

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
        self.hub_departure = None
        self.miles = 0.0
        self.truck_id = truck_id

    def __str__(self):
        return f"""
        {self.address}
        """

    def fix_address(self):
        self.address = "410 S State St"
        self.city = "Salt Lake City"
        self.postal = "84111"


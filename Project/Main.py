import csv
from datetime import timedelta
from Project.HashTable import ChainingHashTable
from Project.Package import Package
from Truck import DeliveryTruck

truck_1_load = []
truck_2_load = []
truck_3_load = []

hub_address = "4001 South 700 East"

truck_1 = DeliveryTruck(1, hub_address, timedelta(hours=8), 0, truck_1_load)
truck_2 = DeliveryTruck(2, hub_address, timedelta(hours=8), 0, truck_2_load)
truck_3 = DeliveryTruck(3, hub_address, timedelta(hours=9, minutes=45), 0, truck_3_load)


def load_trucks(self):
    with open("Resources/WGUPS Package File.csv") as packages_csv:
        read_packages = csv.reader(packages_csv, delimiter=",")
        for row in read_packages:
            truck_id = row[0]
            p_id = (row[1])
            address = row[2]
            city = row[3]
            state = row[4]
            postal = row[5]
            deadline = row[6]
            weight = row[7]
            notes = row[8]
            status = ""

            if "Wrong" in notes:
                address = "410 S State St.,Salt Lake City, UT 84111"

            hashtable = ChainingHashTable
            new_package = Package(p_id, address, city, state, postal, deadline, weight, notes, status, truck_id)
            hashtable.insert(self, p_id, new_package)
            hashtable.set(int(new_package.package_id), new_package)

            if truck_id == 1:
                truck_1_load.append(new_package)
            elif truck_id == 2:
                truck_2_load.append(new_package)
            elif truck_id == 3:
                truck_3_load.append(new_package)

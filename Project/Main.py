import csv
import datetime
from datetime import timedelta

from Project.Delivery import new_distance_search
from Project.Distances import distance_array
from Project.HashTable import ChainingHashTable
from Project.Packages import Package
from Trucks import DeliveryTruck

# Packages presorted by distance and package requirements, trucks loaded manually with package list
truck_1_load = ["13", "14", "15", "16", "19", "20", "21", "24", "25", "29", "33", "34", "40"]
truck_2_load = ["1", "2", "3", "5", "7", "11", "17", "18", "23", "26", "30", "31", "35", "36", "37", "38"]
truck_3_load = ["4", "6", "8", "9", "10", "12", "27", "28", "32", "39"]
truck_mileage_list = []
all_trucks_mileage = []
delivery_time_list = []
hashtable = ChainingHashTable()

# Starting address for trucks
hub_address = "4001 South 700 East"

# Three truck objects initialized with IDs, hub address, starting time, and list of packages.
# Truck 3 also leaves after Truck 1 arrives back at hub, verified with time stamps.
truck_1 = DeliveryTruck(1, hub_address, timedelta(hours=8), 0, truck_1_load)
truck_2 = DeliveryTruck(2, hub_address, timedelta(hours=8), 0, truck_2_load)
truck_3 = DeliveryTruck(3, hub_address, timedelta(hours=9, minutes=41), 0, truck_3_load)

"""
Reads package file and inserts data objects into hash table, creating Package objects.
Package 9 has the wrong address. This will be updated automatically and the package isn't delivered until well after
the new information comes in. 
Time/space complexity of O(N) as space needed is directly proportional to input size.
"""
with open("Resources/WGUPS_Package_File.csv") as packages_csv:
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

        new_package = Package(p_id, address, city, state, postal, deadline, weight, notes, status, truck_id)

        if "Wrong" in notes:
            new_package.fix_address()

        hashtable.insert(int(p_id), new_package)
        hashtable.set(int(new_package.package_id), new_package)


# PRINT TEST AREA

#  calculates the time it takes to reach an address by the miles traveled
def time_calculator(miles):
    time = miles / 18
    return timedelta(hours=time)


package_distances = []


def get_shortest_route(truck_load, current_address):
    delivery_distance = 999
    delivery_index = -1
    for package_id in truck_load:
        current_package = hashtable.search(int(package_id))
        # print(f"current package: {package_id}")
        # breakpoint()
        distance, selected_delivery_index = new_distance_search(current_address, current_package.address)
        if distance < delivery_distance:
            delivery_distance = distance
            delivery_index = selected_delivery_index
    return delivery_distance, delivery_index


"""
Main function/nearest neighbor algorithm to deliver packages. The function cycles through each truck's package list, 
searching the hash table for package addresses. It then delivers the package to that location, timestamps the 
delivery time, and records mileage.
"""


def deliver_packages(truck, truck_load, start_address):
    visited_queue = []

    while len(truck_load) > 0:
        for package in truck_load:
            # Gets shortest route from truck's starting point to closest available package destination.
            # Appends trip mileage into mileage list to be summed later
            delivery_distance, delivery_index = get_shortest_route(truck_load, start_address)

            truck_mileage_list.append(delivery_distance)

            # Calculates trip time based on mileage
            trip_time = time_calculator(delivery_distance)
            delivery_time_list.append(trip_time)

            # Searches hash table and sets next stop as next package's address
            package = hashtable.search(int(package))
            start_address = package.address
            package.hub_departure = truck.departure_time
            # print(f"start address : {start_address}\n")

            package.delivery_time = sum(delivery_time_list, datetime.timedelta()) + truck.departure_time
            print(f"package status : {package.status}")
            print(f"delivery time of package {package.package_id}: {package.delivery_time}")
            package.status = "Delivered!"
            print(f"package status : {package.status}")

            visited_queue.append(package.address)
            print(f"visited queue : {visited_queue}")
            truck_load.remove(package.package_id)

    if len(truck_load) == 0:
        return_distance, index = new_distance_search(visited_queue[-1], hub_address)
        truck_mileage_list.append(return_distance)
        delivery_time_list.append(time_calculator(return_distance))
        truck.truck_location = hub_address
        delivery_time_list.clear()

        print(f"return distance: {return_distance}")

    # Sums mileage for entire delivery route
    total_miles = sum(truck_mileage_list)
    print(f"truck mileage list : {len(truck_mileage_list)}")

    truck.mileage = round(total_miles, 2)
    print(f"total truck miles: {truck.truck_id}, {float(truck.mileage)}")
    delivery_time_spent = time_calculator(truck.mileage)
    return_time = delivery_time_spent + truck.departure_time
    truck.return_time = return_time
    print(f"truck return time: {return_time}")

    all_trucks_mileage.append(truck.mileage)
    print(f"all trucks mileage: {all_trucks_mileage}")
    truck_mileage_list.clear()


def set_package_status(package):
    if package.delivery_time is None:
        package.status = "No"



def calc_total_mileage(all_miles_list):
    cumulative_mileage = round(sum(all_miles_list), 2)
    return cumulative_mileage


def run_delivery():
    deliver_packages(truck_1, truck_1_load, hub_address)
    print(f"truck 1 departure time: {truck_1.departure_time}")
    deliver_packages(truck_2, truck_2_load, hub_address)
    print(f"truck 2 departure time: {truck_2.departure_time}")
    deliver_packages(truck_3, truck_3_load, hub_address)
    print(f"truck 3 departure time: {truck_3.departure_time}")

    cumulative_mileage = calc_total_mileage(all_trucks_mileage)
    print(f"truck 1 mileage: {truck_1.mileage}")
    print(f"truck 2 mileage: {truck_2.mileage}")
    print(f"truck 3 mileage: {truck_3.mileage}")
    print(f"cumulative mileage: {cumulative_mileage}")


run_delivery()

# cumulative_miles = sum(all_trucks_mileage)
# print(f"mileage for all trucks: {cumulative_miles}")
# print(f"cumulative miles: {cumulative_miles}")

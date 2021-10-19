# Damon Heard
# Student ID 001670334

import csv
import datetime
from datetime import datetime, timedelta

from Project.Distances import new_distance_search
from Project.HashTable import ChainingHashTable
from Project.Packages import Package
from Trucks import DeliveryTruck

# Packages presorted by distance and package requirements, trucks loaded manually with package list
# Contains list of all packages to be sorted by numerical value later
truck_1_load = ["13", "14", "15", "16", "19", "20", "21", "24", "25", "29", "33", "34", "40"]
truck_2_load = ["1", "2", "3", "5", "7", "11", "17", "18", "22", "23", "26", "30", "31", "35", "36", "37", "38"]
truck_3_load = ["4", "6", "8", "9", "10", "12", "27", "28", "32", "39"]
all_packages = ["13", "14", "15", "16", "19", "20", "21", "24", "25", "29", "33", "34", "40", "1", "2", "3", "5", "7",
                "11", "17", "18", "22", "23", "26", "30", "31", "35", "36", "37", "38", "4", "6", "8", "9", "10", "12",
                "27", "28", "32", "39"]

# Lists to help with calculating mileages and delivery times.
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


# Reads package file and inserts data objects into hash table, creating Package objects.
# Package 9 has the wrong address. This will be updated automatically and the package isn't delivered until well after
# the new information comes in.
# Time/space complexity of O(N) as processing time and space needed is directly proportional to input size.
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


# Takes a distance parameter and converts to a timedelta to use for later timestamps
def miles_to_time(distance):
    time_to_convert = distance / 18
    return timedelta(hours=time_to_convert)


def get_shortest_route(truck_load, current_address):
    """
    Nearest Neighbor algorithm. Uses truck's package list and truck's current address to identify the shortest route to
    the next stop.
    :param truck_load: list of packages
    :param current_address: truck's current address
    :return: returns distance and index of the selected point
    O(N)
    """
    delivery_distance = 999
    delivery_index = -1
    for package_id in truck_load:
        current_package = hashtable.search(int(package_id))
        distance, selected_delivery_index = new_distance_search(current_address, current_package.address)
        if distance < delivery_distance:
            delivery_distance = distance
            delivery_index = selected_delivery_index
    return delivery_distance, delivery_index


def deliver_packages(truck, truck_load, start_address):
    """
    Main function which implements nearest neighbor algorithm to deliver packages. The function cycles through each
    truck's package list, searching the hash table for package addresses. It then delivers the package to that location,
    timestamps the delivery time, and records mileage.
    :param truck: active truck object
    :param truck_load: list of package objects associated with truck
    :param start_address: starting address of truck
    :return: returns mileage and distance of trucks
    O(N) due to for loop which operates proportional to data processed while while loop conditions
    are true. The functions within the for loop are O(1), so it does not increase the complexity of the larger function.
    """
    visited_queue = []

    while len(truck_load) > 0:
        for package in truck_load:
            # Gets shortest route from truck's starting point to closest available package destination.
            # Appends trip mileage into mileage list to be summed later
            delivery_distance, delivery_index = get_shortest_route(truck_load, start_address)

            truck_mileage_list.append(delivery_distance)

            # Calculates trip time based on mileage
            trip_time = miles_to_time(delivery_distance)
            delivery_time_list.append(trip_time)

            # Searches hash table and sets next stop as next package's address
            package = hashtable.search(int(package))
            start_address = package.address
            package.hub_departure = truck.departure_time

            package.delivery_time = sum(delivery_time_list, timedelta()) + truck.departure_time
            # print(f"delivery time of package {package.package_id}: {package.delivery_time}")
            truck.truck_location = package.address

            visited_queue.append(package.address)
            set_package_status(package)
            truck_load.remove(package.package_id)

    # When truck is empty of package objects, it returns back to the hub and appends mileage and time to lists for further
    # calculations.
    # O(1)
    if len(truck_load) == 0:
        return_distance, index = new_distance_search(visited_queue[-1], hub_address)
        truck_mileage_list.append(return_distance)
        delivery_time_list.append(miles_to_time(return_distance))
        truck.truck_location = hub_address
        delivery_time_list.clear()

    # Sums mileage for entire delivery route
    total_miles = sum(truck_mileage_list)

    # Records total truck mileage and returns truck back to hub
    truck.mileage = round(total_miles, 2)
    delivery_time_spent = miles_to_time(truck.mileage)
    return_time = delivery_time_spent + truck.departure_time
    truck.return_time = return_time

    all_trucks_mileage.append(truck.mileage)
    truck_mileage_list.clear()

# Sets package status according to delivery and hub departure times.
# O(1)
def set_package_status(package):
    if (package.hub_departure is not None) and (package.delivery_time is None):
        package.status = "En route"
        print(f"package status: {package.status}")
    elif (package.hub_departure is None) and (package.delivery_time is None):
        package.status = "At hub"
    elif (package.hub_departure is not None) and (package.delivery_time is not None):
        package.status = "Delivered!"


# Calculates total mileage using miles appended to list
# O(1)
def calc_total_mileage(all_miles_list):
    cumulative_mileage = round(sum(all_miles_list), 2)
    return cumulative_mileage


# Implements deliver_packages function and prints relevant statistics for the user.
# As this executes the deliver_packages function, it inherits its time/space complexity of O(N).
def run_delivery():
    deliver_packages(truck_1, truck_1_load, hub_address)
    print(f"Truck 1 departure time: {truck_1.departure_time}")
    print(f"Truck 1 return time: {truck_1.return_time}")
    print(f"Truck 1 mileage: {truck_1.mileage}")
    print("------------------------------------------------------------------------------------------------")

    deliver_packages(truck_2, truck_2_load, hub_address)
    print(f"Truck 2 departure time: {truck_2.departure_time}")
    print(f"Truck 2 return time: {truck_2.return_time}")
    print(f"Truck 2 mileage: {truck_2.mileage}")
    print("------------------------------------------------------------------------------------------------")

    deliver_packages(truck_3, truck_3_load, hub_address)
    print(f"Truck 3 departure time: {truck_3.departure_time}")
    print(f"Truck 3 return time: {truck_3.return_time}")
    print(f"Truck 3 mileage: {truck_3.mileage}")
    print("------------------------------------------------------------------------------------------------")

    cumulative_mileage = calc_total_mileage(all_trucks_mileage)
    print(f"Cumulative mileage: {cumulative_mileage}")
    print("------------------------------------------------------------------------------------------------")


def main():
    """
    Main method to launch the program. Gives user options for information to display.
    O(N) due to single (non-nested) loop in option 2.
    """
    print(f"\nWelcome to the WGUPS Delivery Service!"
          f"\nPlease enter a choice from the options below: "
          f"\n1: Lookup package details by package ID "
          f"\n2: Lookup current truck and package status by time "
          f"\n3: View truck mileage "
          f"\n4: Exit")

    user_selection = int(input(""))

    if user_selection == 1:
        run_delivery()

        selected_package = int(input("Please enter a package ID: "))
        returned_package = hashtable.search(int(selected_package))
        if (returned_package.package_id == "9") and (returned_package.status != "Delivered!"):
            returned_package.address = "300 State St"
            returned_package.postal = "84103"

        print("------------------------------------------------------------------------------------------------")
        print(f"Package {returned_package.package_id}: "
              f"\nDelivery address: {returned_package.address}"
              f"\nDeadline: {returned_package.deadline} "
              f"\nDelivery City: {returned_package.city} "
              f"\nZipcode: {returned_package.postal} "
              f"\nPackage weight: {returned_package.weight} "
              f"\nStatus: {returned_package.status} "
              f"\nDelivery time: {returned_package.delivery_time}")
        print("------------------------------------------------------------------------------------------------")
        second_selection = int(input("Press 1 to exit."))
        if second_selection == 1:
            exit()
        else:
            print("Invalid selection. Exiting program.")
            exit()

    elif user_selection == 2:
        run_delivery()

        sorted_packages = [int(i) for i in all_packages]
        sorted_packages.sort()

        input_time = str(input("Please enter a time in 24-hr HH:MM format "
                               "\n(ex: 3:35 pm = 15:25) :\n"))
        query_time_format = "%H:%M"
        query_time = datetime.strptime(input_time, query_time_format)
        query_delta = timedelta(hours=query_time.hour, minutes=query_time.minute)

        for package in sorted_packages:
            package = hashtable.search(int(package))
            if (package.package_id == "9") and (query_delta < timedelta(hours=10, minutes=21)):
                package.address = "300 State St"
                package.postal = "84103"

            if query_delta < package.hub_departure:
                print(f"Package {package.package_id} status: At hub")
                print(
                    "------------------------------------------------------------------------------------------------")
            elif (query_delta > package.hub_departure) and (query_delta < package.delivery_time):
                print(f"Package {package.package_id} status: En route")
                print(
                    "------------------------------------------------------------------------------------------------")
            elif (query_delta > package.hub_departure) and (query_delta > package.delivery_time):
                print(f"Package {package.package_id} delivered at {package.delivery_time}!")
                print(
                    "------------------------------------------------------------------------------------------------")
        second_selection = int(input("Press 1 to exit."))
        if second_selection == 1:
            exit()
        else:
            print("Invalid selection. Exiting program.")
            exit()

    elif user_selection == 3:
        run_delivery()

        cumulative_mileage = calc_total_mileage(all_trucks_mileage)
        print("------------------------------------------------------------------------------------------------")
        print(f"Truck 1 mileage: {truck_1.mileage}")
        print(f"Truck 2 mileage: {truck_2.mileage}")
        print(f"Truck 3 mileage: {truck_3.mileage}")
        print(f"cumulative mileage: {cumulative_mileage}")
        print("------------------------------------------------------------------------------------------------")
        second_selection = int(input("Press 1 to exit."))
        if second_selection == 1:
            exit()
        else:
            print("Invalid selection. Exiting program.")
            exit()

    elif user_selection == 4:
        print("Goodbye!")
        exit()

    else:
        print("Invalid selection. Exiting program.")
        exit()


main()

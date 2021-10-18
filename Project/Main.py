import csv
from datetime import timedelta

from Project.Delivery import new_distance_search
from Project.Distances import Graph, distance_array
from Project.HashTable import ChainingHashTable
from Project.Packages import Package
from Trucks import DeliveryTruck

hashtable = ChainingHashTable()

# Packages presorted by distance and package requirements, trucks loaded manually with package list
truck_1_load = ["1", "2", "4", "13", "14", "15", "16", "19", "20", "21", "22", "24", "29", "33", "34", "40"]
truck_2_load = ["3", "5", "7", "11", "17", "18", "23", "25", "26", "30", "35", "36", "37", "38"]
truck_3_load = ["6", "8", "9", "10", "12", "27", "28", "31", "32", "39"]

# Starting address for trucks
hub_address = "4001 South 700 East"
hub_address1 = "Western Governors University\n4001 South 700 East, \nSalt Lake City, UT 84107"

# Three truck objects initialized with IDs, hub address, starting time, and list of packages
truck_1 = DeliveryTruck(1, hub_address, timedelta(hours=8), 0, truck_1_load)
truck_2 = DeliveryTruck(2, hub_address, timedelta(hours=8), 0, truck_2_load)
truck_3 = DeliveryTruck(3, hub_address, timedelta(hours=9, minutes=45), 0, truck_3_load)
print(f"truck 1: {truck_1}")

# Reads package file, inserts package objects into hash table
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

        if "Wrong" in notes:
            address = "410 S State St.,Salt Lake City, UT 84111"

        new_package = Package(p_id, address, city, state, postal, deadline, weight, notes, status, truck_id)
        hashtable.insert(int(p_id), new_package)
        hashtable.set(int(new_package.package_id), new_package)
        # print(f"package {new_package.package_id}, loaded on truck {new_package.truck_id}")


# PRINT TEST AREA
print(f"new distance search:\n{new_distance_search('4001 South 700 East', '1060 Dalton Ave S')}")

# print(f"invoking get_distance : {get_distance('4001 South 700 East', '1060 Dalton Ave S')}")
# get_shortest_route(truck_1, hub_address)

# def search_truck(truck_load):
#     packages = []
#     for package in truck_load:
#         packages.append(new_package.package_id)
#         search_result = hashtable.search(int(new_package.package_id))
#         print(f"search result: {search_result}")
#         # print(f"package list: {}")
#         print(len(packages))

# for package in truck_load:
#     hashtable.search(new_package.package_id)
#     print()


#  calculates the time it takes to reach an address by the miles traveled
def time_calculator(miles):
    time = miles / 18
    return timedelta(hours=time)


# truck_graph = draw_graph()

package_distances = []


def get_shortest_route(truck_load, current_address):
    delivery_distance = 999
    delivery_index = -1
    for package_id in truck_load:
        current_package = hashtable.search(int(package_id))
        print(f"current package: {package_id}")
        distance, selected_delivery_index = new_distance_search(current_address, current_package.address)
        if distance < delivery_distance:
            delivery_distance = distance
            delivery_index = selected_delivery_index
    return delivery_distance, delivery_index


def deliver_packages(truck_load, start_address):
    total_miles = 0.0
    total_mileage = []
    unvisited_queue = []
    visited_queue = []

    while len(truck_load) > 0:
        for package in truck_load:
            # Gets shortest route from truck's starting point to closest available package destination.
            # Appends trip mileage into mileage list to be summed later
            delivery_distance, delivery_index = get_shortest_route(truck_load, start_address)
            total_mileage.append(delivery_distance)

            # Calculates trip time based on mileage
            trip_time = time_calculator(delivery_distance)
            print(f"trip time: {trip_time}")

            # Sums mileage for entire delivery route
            total_miles = sum(total_mileage)
            print(f"total miles: {total_miles}")

            package = hashtable.search(int(package))
            start_address = package.address

            truck_load.remove(package)


deliver_packages(truck_1_load, hub_address)


# def get_shortest_route(truck, g, delivery_time, current_address):
#     truck.set_truck_location()
#     truck_load = truck.package_list
#     current_address = hub_address
#     current_distance = float(100)
#     current_mileage = 0
#     current_time = truck.departure_time
#     i = 0
#     j = i + 1
#     # g = Graph
#     address_list = []
#     route_list = {}
#     next_stop = None
#     next_stop_dist = None
#     pack_start = None
#     filtered_dist = None
#     pack_dest = None
#     pack1 = Package
#     path = None
#     unvisited_queue = []
#     minimum_distance = 999.9
#     visited_queue = []
#     # print(f"route graph items: {route_graph.items()}")
#     total_mileage = 0.0
#     visited_locations = []
#     start_address = 'HUB'
#     dict_1 = {}
#     g = Graph()
#     current_location = None
#     package_address = None
#
#     # Retrieves addresses of truck's package list and inserts into address_list
#     while len(truck_load) > 0:
#
#         for package in truck_load:
#             result = hashtable.search(package)
#             current_package = result.address
#             print(f"current package: {current_package}")
#             if current_package > current_address:
#                 dist = float(distance_array[current_package][current_address])
#             else:
#                 dist = float(distance_array[current_address][current_package])
#             # If this route is shorter than others we've checked, use it for now
#             if dist < minimum_distance:
#                 short_route = dist
#                 next_package = package
#                 next_addr_num = current_package
#
#         return next_package, next_addr_num, minimum_distance


        # result = hashtable.search(int(package))
            # package_address = result.address
            # print(f"result address {package_address}")
            # address_list.append(package_address)
            # truck_load.pop(0)
            # visited_locations.append(package_address)
            # print(f"truckload size: {len(truck_load)}")
            #
            # current_location = hub_address
            # print(f"current location: {current_location}")
            # print(f"package addy: {package_address}")

#             route_list_1 = [value for key, value in route_graph.items() if str(key[0]) == str(current_location) and str(key[1]) == str(package_address)]
#             print(f"route list 1: {route_list_1}")
#
#
# run_delivery(truck_1, route_graph, timedelta(hours=8))

# address_list.append(package.get_package_address())
#
# Algorithm.get_shortest_path(hub_address, route_graph)
# shortest_distance = Algorithm.get_shortest_path(route_graph)
#
# index = 0
# test_truck.truck_location = hub_address
# value = None
#
# while len(test_truck.package_list) != 0:
#     while index < len(test_truck.package_list):
#         # breakpoint()
#
#         current_truck_location = test_truck.truck_location
#         print(f"truck location: {current_truck_location}")
#         current_package = hashtable.search(int(test_truck.package_list[index]))
#         print(f"current package is: {current_package}")
#         # print("current package: " + str(current_package.address))
#         package_address = current_package.address
#         # breakpoint()
#         new_distance = Algorithm.get_shortest_path(hub_address, route_graph)
#         print(f"new distance: {new_distance}")
#
#         if float(current_distance) > float(new_distance):
#             current_distance = float(new_distance)
#             location = current_package.address
#             package = current_package
#             value = test_truck.package_list[index]
#         index = index + 1
#     index = 0
#
#     test_truck.truck_location = location
#     test_truck.package_list.remove(value)
#     test_truck.mileage = current_mileage + float(current_distance)
#     current_time = package.delivery_time = current_time + time_calculator(current_distance)
#     current_distance = float(100)


# def start_routes(time):
#     run_delivery(truck_1, route_graph, timedelta(hours=8))
#
#
# start_routes(timedelta(8))


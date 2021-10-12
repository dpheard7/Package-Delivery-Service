import csv
import operator
from datetime import timedelta

import self

from Project import Algorithm
from Project.Algorithm import get_shortest_path, shortest, dijkstra
from Project.Distances import Graph, route_graph, distance_list, draw_graph
from Project.HashTable import ChainingHashTable
from Project.Packages import Package
from Trucks import DeliveryTruck

hashtable = ChainingHashTable()

# Packages presorted by distance and package requirements, trucks loaded manually with package list
truck_1_load = ["1", "2", "4", "13", "14", "15", "16", "19", "20", "21", "22", "24", "29", "33", "34", "40"]
truck_2_load = ["3", "5", "7", "11", "17", "18", "23", "25", "26", "30", "35", "36", "37", "38"]
truck_3_load = ["6", "8", "9", "10", "12", "27", "28", "31", "32", "39"]

# Starting address for trucks
hub_address = "HUB"

# Three truck objects initialized with IDs, hub address, starting time, and list of packages
truck_1 = DeliveryTruck(1, hub_address, timedelta(hours=8), 0, truck_1_load)
truck_2 = DeliveryTruck(2, hub_address, timedelta(hours=8), 0, truck_2_load)
truck_3 = DeliveryTruck(3, hub_address, timedelta(hours=9, minutes=45), 0, truck_3_load)

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
print(f"route graph (adjacency matrix): {len(route_graph)}")


# print(f"graph data type: {(type(route_graph))}")
# print(f"distance list: {distance_list}")
# paths = get_shortest_path("" + hub_address, route_graph)
# print(f"shortest path: {paths}")


# print(hashtable.__dict__)
# for key, value in hashtable:
#     print(hashtable.get(key, value))
# print(hashtable)


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


# search_truck(truck_2_load)

# search_package = hashtable.search(10)

# print(f"search package: {str(search_package)}")

# print(f"shortest distance: {get_shortest_path(route_graph)}")

def find_min(g):
    m = min(i for i in g if i > 0)
    for value in g.items:
        if value == 0:
            continue
    # print(f"rg min: {min(route_graph.items(), key=lambda x:x[1])}")


# for d in route_graph:
#     print(f"keys: {route_graph.values()}")

# print(f"shortest path: {shortest(route_graph)}")

# print(f"rg1: {route_graph[0]}")


# def nearest_neighbor(drawn_graph):
#     shortest_path = 0
#     for k in drawn_graph:
#         if k == k:
#             continue


# print(Algorithm.dijkstra(route_graph, 'HUB')) - prints 'None'
# print(truck_1.__dict__)


#  calculates the time it takes to reach an address by the miles traveled
def time_calculator(miles):
    time = miles / 18
    return timedelta(hours=time)


# truck_graph = draw_graph()

print(f"distance list: {distance_list}")

package_distances = []

# def find_distance(current_location, destination, package):
#     if()

string = "address list : "


def run_delivery(truck, g, delivery_time):
    test_truck = truck_1
    test_truck.set_truck_location()
    truck_load = test_truck.package_list
    current_distance = float(100)
    current_mileage = 0
    current_time = test_truck.departure_time
    i = 0
    j = i + 1
    # g = Graph
    address_list = []
    route_list = {}
    next_stop = None
    next_stop_dist = None
    pack_address = None
    filtered_dist = None
    pack_dest = None
    pack1 = Package
    path = None
    best_route = []
    min_dist = 999

    print(f"test truck's package list is: {test_truck.package_list}")
    # load = get_package_info(truck_2_load, hashtable)
    # print(f"truck 2 package info: {load}")

    # while len(truck_load) > 1:
    for package in truck_load:
        result = hashtable.search(int(package))
        address_list.append(result)

        # breakpoint()
        for x in address_list:
            pack_address = x.address
            # print(f"pack x address = {pack_address}")

            for y in address_list:
                pack_dest = y.address

            for route, mileage in g.items():
                if str(pack_address) and str(pack_dest) in str(route):
                    if mileage > 0.0:
                        next_stop = route
                        next_stop_dist = mileage
                        kv = next_stop, next_stop_dist
                        route_list.update({kv})
    path = get_shortest_path(route_list)
    # print(f"shortest path: {path}")

    # print(*address_list)
    # print(f"len: {len(address_list)}")
    print(f"pack addresses # = {len(pack_address)}")
    # print(f"pack addresses: {pack_address}")
    print(f"pack destinations: {len(pack_dest)}")

    print(f"route list: {route_list}")
    print(f"route list length: {len(route_list)}")

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


def start_routes(time):
    run_delivery(truck_1, route_graph, timedelta(hours=8))


start_routes(timedelta(8))
print(f"Mileage:\nTruck 1: {truck_1.mileage}")

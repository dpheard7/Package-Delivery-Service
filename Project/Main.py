import csv
from datetime import timedelta

from Project import Distances
from Project.Distances import Graph
from Project.HashTable import ChainingHashTable
from Project.Package import Package
from Truck import DeliveryTruck

hashtable = ChainingHashTable(40)

# Packages presorted by distance and package requirements, trucks loaded manually with package list
truck_1_load = ["1", "2", "4", "13", "14", "15", "16", "19", "20", "21", "22", "24", "29", "33", "34", "40"]
truck_2_load = ["3", "5", "7", "11", "17", "18", "23", "25", "26", "30", "35", "36", "37", "38"]
truck_3_load = ["6", "8", "9", "10", "12", "27", "28", "31", "32", "39"]

# Starting address for trucks
hub_address = "4001 South 700 East"

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

final_graph = Graph()

final_graph.add_vertex(Distances.distance_list)
final_graph.add_undirected_edge()
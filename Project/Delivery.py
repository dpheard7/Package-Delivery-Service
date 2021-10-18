import csv
from datetime import timedelta

from Project import Trucks
from Project.Distances import Graph, distance_array, address_array
from Project.HashTable import ChainingHashTable
from Project.Packages import Package

hashtable = ChainingHashTable()

# Starting address for trucks
hub_address = "4001 South 700 East"

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
            address = "410 S State St.,Salt Lake City, UT\n(84111)"

        new_package = Package(p_id, address, city, state, postal, deadline, weight, notes, status, truck_id)
        hashtable.insert(int(p_id), new_package)
        hashtable.set(int(new_package.package_id), new_package)
        # print(f"package {new_package.package_id}, loaded on truck {new_package.truck_id}")


# PRINT TEST AREA

# def get_distance(current_location, destination):


def new_distance_search(current_location, destination):
    # breakpoint()
    i = 0
    for row_data in distance_array:
        if current_location in row_data[0]:
            current_index = i
            break
        i += 1
    i = 0
    for row_data in distance_array:
        if destination in row_data[0]:
            destination_index = i
            break
        i += 1
    # breakpoint()
    miles = float(distance_array[current_index][destination_index + 1])
    return miles, i


#  calculates the time it takes to reach an address by the miles traveled
def time_calculator(miles):
    time = miles / 18
    return timedelta(hours=time)




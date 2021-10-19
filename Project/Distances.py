import csv

from Project import Algorithm

distance_array = []
address_array = []

# Reads distances from csv and appends to distance_array, skipping the first column (addresses)
# O(N)
with open("Resources/WGUPS Distance Table_csv1.csv", encoding='utf-8-sig') as distances_csv:
    read_distances = csv.reader(distances_csv, delimiter=",")
    next(read_distances)
    for i in read_distances:
        distance_array.append(i)
# print(f"distance array unformatted: {distance_array}")
# print("distance array formatted: \n" + '\n'.join([''.join(['{:4}'.format(item) for item in row])
#                                                   for row in distance_array]))

# print(f"test: {distance_array[4][2]}")
# for distance array, first number is rows down, second is columns across. eg distance_array[4][2] = 5 rows down,
# 3 rows across (starting with 0 as the first row


# Reads addresses only from csv and appends to address_array, skipping all of the distance information
# O(N)
with open("Resources/Locations.csv", encoding='utf-8-sig') as addresses_csv:
    read_addresses = csv.reader(addresses_csv, delimiter=",")
    for row in read_addresses:
        row[1].strip()
        address_array.append(row)
# print(f"address array in Distances = {address_array}")

import csv

distance_array = []
address_array = []

# Reads distances from csv and appends to distance_array, skipping the first column (addresses)
# O(N) due to processing proportional to data in file.
with open("Resources/WGUPS Distance Table_csv1.csv", encoding='utf-8-sig') as distances_csv:
    read_distances = csv.reader(distances_csv, delimiter=",")
    next(read_distances)
    for i in read_distances:
        distance_array.append(i)


# Reads addresses only from csv and appends to address_array, skipping all of the distance information
# O(N) due to processing proportional to data in file.
with open("Resources/Locations.csv", encoding='utf-8-sig') as addresses_csv:
    read_addresses = csv.reader(addresses_csv, delimiter=",")
    for row in read_addresses:
        row[1].strip()
        address_array.append(row)
# print(f"address array in Distances = {address_array}")


# Basic function to retrieve distance between two points according to data provided in csv.
# O(N) due to non-nested for loops.
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
    miles = float(distance_array[current_index][destination_index + 1])
    return miles, i


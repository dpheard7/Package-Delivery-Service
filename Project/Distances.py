import csv

from Project import Algorithm

distance_array = []


# Creates vertices for use in drawing the graph
class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float("inf")
        self.pred_vertex = None


# Directs creation of graph with undirected edges using distance list as weights and addresses from csv fire as vertices
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []
        if new_vertex in self.adjacency_list:
            return
        else:
            self.adjacency_list[new_vertex] = []
            return self.adjacency_list

    def add_directed_edge(self, from_v, to_v, weight=1.0):
        self.edge_weights[(from_v, to_v)] = weight
        self.adjacency_list[from_v].append(to_v)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def find_dist(self, start_v, end_v):
        for key, value in self.edge_weights:
            if (start_v == key[0]) and (end_v == key[1]):
                return value
        return [value for key, value in self.edge_weights.items() if key[0] == start_v and key[1] == end_v]


my_graph = Graph()

# Reads distances from csv and appends to distance_array, skipping the first column (addresses)
# O(N)
with open("Resources/WGUPS Distance Table_csv.csv", encoding='utf-8-sig') as distances_csv:
    read_distances = csv.reader(distances_csv, delimiter=",")
    next(read_distances)
    for i in read_distances:
        distance_array.append(i)
print(f"distance array unformatted: {distance_array}")
print("distance array formatted: \n" + '\n'.join([''.join(['{:4}'.format(item) for item in row])
                                                  for row in distance_array]))

# print(f"test: {distance_array[4][2]}")
# for distance array, first number is rows down, second is columns across. eg distance_array[4][2] = 5 rows down,
# 3 rows across (starting with 0 as the first row


address_array = []

# Reads addresses only from csv and appends to address_array, skipping all of the distance information
# O(N)
with open("Resources/Locations.csv", encoding='utf-8-sig') as addresses_csv:
    read_addresses = csv.reader(addresses_csv, delimiter=",")
    for row in read_addresses:
        row[1].strip()
        address_array.append(row)
print(f"address array in Distances = {address_array}")


graph = Graph()

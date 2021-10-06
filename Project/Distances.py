import csv

distance_list = []

with open("Resources/WGUPS Distance Table.csv") as distances_csv:
    read_distances = csv.reader(distances_csv, delimiter=",")
    next(read_distances, None)
    for row in read_distances:
        distance_list.append(row)


class Vertex:
    def __init__(self, label):
        self.label = label


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

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.edge_weights[(vertex_a, vertex_b)] = weight
        self.edge_weights[(vertex_b, vertex_a)] = weight


graph = Graph()


def get_distances():
    for line in distance_list:
        graph.add_vertex(line[1])

    for line in distance_list:
        for i in range(1, 28):
            graph.add_undirected_edge(line[0], distance_list[i - 1][0], float(line[i]))
    return graph.edge_weights

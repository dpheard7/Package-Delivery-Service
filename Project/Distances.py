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
        self.distance = float("inf")
        self.pred_vertex = None


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


# Draws graph using the edges and vertices created with distance_list
# The loops are not nested and therefore the operations are linear, so the complexity is O(N)
def draw_graph(name):
    for edge in distance_list:
        graph.add_vertex(edge[1])

    for edge in distance_list:
        for i in range(1, 28):
            graph.add_undirected_edge(edge[0], distance_list[i - 1][0], float(edge[i]))
    return graph.edge_weights


weights = draw_graph("Resources/WGUPS Distance Table.csv")

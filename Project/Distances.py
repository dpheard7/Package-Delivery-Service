import csv

from Project import Algorithm


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
        return [value for key, value in self.edge_weights.items() if key[0] == start_v and key[1] == end_v]


distance_list = []


with open("Resources/WGUPS Distance Table.csv") as distances_csv:
    read_distances = csv.reader(distances_csv, delimiter=",")
    # read_distances.__next__()
    next(read_distances, None)
    for i in read_distances:
        distance_list.append(i)
# print(distance_list)

graph = Graph()


# Creates graph object using the edges and vertices created with distance and address data from csv file
def draw_graph(name):
    for vertex_a in distance_list:
        graph.add_vertex(vertex_a[0])

        # Prevents HUB from referencing itself in graph
        # Complexity O(N^2)
    for edge in distance_list:
        for i in range(1, 28):
            graph.add_undirected_edge(edge[0], distance_list[i - 1][0], float(edge[i]))
    return graph.edge_weights


route_graph = draw_graph("Resources/WGUPS Distance Table.csv")


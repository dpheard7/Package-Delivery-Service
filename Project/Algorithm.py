import sys

# graph1 = Graph()


# Implementing Dijkstra's algorithm, a type of greedy algorithm which chooses best choice possible among all choices
# available.
from Project import Trucks
from Project.Distances import Graph, route_graph, draw_graph
from Project.HashTable import ChainingHashTable
from Project.Trucks import DeliveryTruck

hasher = ChainingHashTable()
g = Graph()


def dijkstra(graph, start_point, package_list):
    unvisited_queue = []
    for current_vertex in graph.adjacency_list:
        unvisited_queue.append(current_vertex)

    start_distance = 0

    while len(unvisited_queue) > 0:
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)

        for adjacent_vertex in graph.adjacency_list[current_vertex]:
            edge_weight = graph.edge_weights[(current_vertex, adjacent_vertex)]
            alternate_path = current_vertex.distance + edge_weight

            if alternate_path < adjacent_vertex.distance:
                adjacent_vertex.distance = alternate_path
                adjacent_vertex.pred_vertex = current_vertex


# def get_shortest_path(start_vertex, end_vertex):
#     # Start from end_vertex and build the path backwards.
#     path = ""
#     current_vertex = end_vertex
#     while current_vertex is not start_vertex:
#         path = " -> " + str(current_vertex.label) + path
#         current_vertex = current_vertex.pred_vertex
#     path = start_vertex.label + path
#     return path


# def get_package_info(truck_load, hash_table):
#     for package in truck_load:
#         package_search = hash_table.search(int(package))
#         return package_search


# def nearest_neighbors(g):
#     current_node = 0
#     path = [current_node]
#     n = g.number_of_nodes()
#
#     # We'll repeat the same routine (n-1) times
#     for _ in range(n - 1):
#         next_node = None
#         # The distance to the closest vertex. Initialized with infinity.
#         min_edge = float("inf")
#         for v in g.nodes():
#             if g[current_node][v]['weight'] < min_edge and v not in path:
#                 # Write your code here: decide if v is a better candidate than next_node.
#                 # If it is, then update the values of next_node and min_edge
#                 min_edge = g[current_node][v]['weight']
#                 next_node = v
#
#         assert next_node is not None
#         path.append(next_node)
#         current_node = next_node
#
#     weight = sum(g[path[i]][path[i + 1]]['weight'] for i in range(g.number_of_nodes() - 1))
#     weight += g[path[-1]][path[0]]['weight']
#     return weight

next_list = []


def get_shortest_path(g):
    my_truck = DeliveryTruck
    # next_stop = {}
    dict_1 = {}
    hub_addy = 'HUB'
    start_point = hub_addy
    current_address = hub_addy
    # filtered_min = None
    destination = None
    visited_list = []
    filtered_min = None

    for key, value in g.items():
        if current_address in key[0] and value > float(0.0):
            result = key
            min_dist = value
            kv = result, min_dist
            dict_1.update({kv})
            filtered_min = (min(dict_1.values()))
            # print(f"filtered min: {filtered_min}")
            # for loc, distance in dict_1.items():
            #     if filtered_min == distance:
            #         next_list.append(loc[1])
            #         # print(f"filtered min: {filtered_min}")
            #         # my_truck.set_truck_location(loc[1])
            #         # print(f"truck location: {my_truck.get_truck_location()}")

    for loc, distance in dict_1.items():
        if filtered_min == distance:
            kv1 = loc, distance
            # next_stop.update({kv1})
            next_list.append(loc[1])
            # print(next_list)
            # print(f"filtered min: {filtered_min}")
            # my_truck.set_truck_location(loc[1])
            # print(f"truck location: {my_truck.get_truck_location()}")
            # print(f"next stop: {next_stop}")

    set(next_list)

    print(f"Next stop {filtered_min} miles away.")
    # print(f"length of dict 1 {len(dict_1)}")
    print(f"next list: {next_list}")


# print(f"dict 1: {dict_1.items()}")


def shortest(drawn_graph, start, goal):
    explored = []
    queue = start

    if start == goal:
        print("Same node")
        return
    while queue:
        path = queue.pop
        node = path[-1]

        if node not in explored:
            neighbors = drawn_graph[node]

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)

                if neighbor == goal:
                    print("Shortest path - " * new_path)
                    return

            explored.append(node)
    print("no connected path")
    return

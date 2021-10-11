import sys

# graph1 = Graph()


# Implementing Dijkstra's algorithm, a type of greedy algorithm which chooses best choice possible among all choices
# available.
from Project.Distances import Graph, route_graph
from Project.HashTable import ChainingHashTable

hasher = ChainingHashTable()


def dijkstra(graph, package_list):
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


def get_package_info(truck_load):
    for package in truck_load:
        package_search = hasher.search(int(package.package_id))


def get_shortest_path(current_address, g):
    survey_list = []
    next_stop = {}
    dict_1 = {}
    min_dist = 99
    min_dist = None

    result = None
    result1 = None
    hub_addy = 'HUB'
    current_address = " " + hub_addy
    i = 0
    min_distance = None
    # next_stop = None
    filtered_min = None
    loc = None
    distance = None

    #
    # for package_id in truck_load:
    #     package = hasher.search(int(package_id))
    #     distance = route_graph[current_address][package.address]
    #     if min_distance is not None:
    #         if float(distance) < float(min_distance):
    #             min_distance = float(distance)
    #             survey_list.insert(0, int(package.package_id))
    #         else:
    #             survey_list.append(int(package.package_id))
    #     print(f"package addresses: {package.get_package_address()}")
    #     print(f"survey list: {survey_list}")

    for key, value in g.items():

        # print(f"key: {key}")
        # print(f"value: {value}")

        # if value == 0.0:
        #     continue
        # if g.values == 0.0:
        #     continue
        # if float(value) == 0.0:
        #     continue
        # if value < min_dist:
        #     min_dist = value
        #     continue
        if current_address in key:
            if value > float(0.0):
                result = key
                min_dist = value
                kv = result, min_dist

                # if current_address in kv:

                dict_1.update({kv})

                # print(f"dict 1: {dict_1}")

                filtered_min = (min(dict_1.values()))

    for loc, distance in dict_1.items():
        if filtered_min == distance:
            kv1 = loc, distance
            next_stop.update({kv1})

            #     return filtered_min
            # if filtered_min == value:
            #     next_stop.update({kv})

                # result1 = [key for key, value in dict_1 if filtered_min == value]
                # kv1 = result1, filtered_min

                # next_stop.update(kv1)

            # print(f"next stop: {next_stop}")

            # for key1, value1 in dict_1:
            #     if value1 == min_distance:
            #         key1 = next_stop
            #         print(next_stop)
        # next_stop = [key for key, value in dict_1 if value == min_distance]

    # print(f"result 1: {result1}")
    print(f"filtered min: {filtered_min}")
    print(f"next stop: {next_stop}")
    # print(f"dict 1: {dict_1}")

    # if value and (min_dist is not None and value < min_dist):

    # print(f"result: {result}")
    # print(f"survey size: {len(survey_list)}")
    # print(f"survey list: {survey_list}")
    # print(f"dict_1: {dict_1}")

    # if start in g.keys:
    #     survey_list.append(start)

    # for i in range(len(package_list)):
    #     for j in range(len(package_list)):
    #         package = package_list[j]
    #         address = package.get_package_address()

    #
    #
    # min_path = "", ""
    # min_miles = 100
    # for path, miles in drawn_graph:  # drawn_graph.items():
    #     lowest_miles = float(min(miles))
    #     print(f"lowest miles: {lowest_miles}")
    #     if lowest_miles < min_miles:
    #         min_miles = lowest_miles
    #         min_path = path
    # print(f"shortest path is: {min_path}")
    # print(f"lowest miles is: {min_miles}")

    # k = range(len(g))
    # print(f"k: {k}")

    # min_distance = 999
    #
    # for key, value in g:
    #     if value == float(0.0):
    #         break
    #     if key == key:
    #         break
    #     if value < min_distance:
    #         min_distance = value
    #         continue
    #
    # return min_distance

    # # i = route_graph[1]
    # # print(i)

    # ORIGINAL
    # path = ""
    # current_vertex = end_vertex
    # while current_vertex is not start_vertex:
    #     # path = " -> " + str(current_vertex.label) + path
    #     current_vertex = current_vertex.pred_vertex
    # path = start_vertex.label + path
    # return path


# def shortest(drawn_graph, start, goal):
#     explored = []
#     queue = start
#
#     if start == goal:
#         print("Same node")
#         return
#     while queue:
#         path = queue.pop
#         node = path[-1]
#
#         if node not in explored:
#             neighbors = drawn_graph[node]
#
#             for neighbor in neighbors:
#                 new_path = list(path)
#                 new_path.append(neighbor)
#
#                 if neighbor == goal:
#                     print("Shortest path - " *new_path)
#                     return
#
#             explored.append(node)
#     print("no connected path")
#     return


g = Graph()

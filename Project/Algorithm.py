# import sys
#
# # graph1 = Graph()
#
#
# # Implementing Dijkstra's algorithm, a type of greedy algorithm which chooses best choice possible among all choices
# # available.
# from Project import Trucks
# from Project.Distances import Graph, draw_graph, route_graph
# from Project.HashTable import ChainingHashTable
# from Project.Trucks import DeliveryTruck
#
# hasher = ChainingHashTable()
# g = Graph()
#
# # def dijkstra(graph, start_point, package_list):
# #     unvisited_queue = []
# #     for current_vertex in graph.adjacency_list:
# #         unvisited_queue.append(current_vertex)
# #
# #     start_distance = 0
# #
# #     while len(unvisited_queue) > 0:
# #         smallest_index = 0
# #         for i in range(1, len(unvisited_queue)):
# #             if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
# #                 smallest_index = i
# #         current_vertex = unvisited_queue.pop(smallest_index)
# #
# #         for adjacent_vertex in graph.adjacency_list[current_vertex]:
# #             edge_weight = graph.edge_weights[(current_vertex, adjacent_vertex)]
# #             alternate_path = current_vertex.distance + edge_weight
# #
# #             if alternate_path < adjacent_vertex.distance:
# #                 adjacent_vertex.distance = alternate_path
# #                 adjacent_vertex.pred_vertex = current_vertex
#
#
# # def get_shortest_path(start_vertex, end_vertex):
# #     # Start from end_vertex and build the path backwards.
# #     path = ""
# #     current_vertex = end_vertex
# #     while current_vertex is not start_vertex:
# #         path = " -> " + str(current_vertex.label) + path
# #         current_vertex = current_vertex.pred_vertex
# #     path = start_vertex.label + path
# #     return path
#
#
# # def get_package_info(truck_load, hash_table):
# #     for package in truck_load:
# #         package_search = hash_table.search(int(package))
# #         return package_search
#
# next_list = []
#
#
# # REFERENCE ONLY
# # def get_shortest_path(path):
# #     address_list = []
# #     start_point = None
# #     my_truck = DeliveryTruck
# #     next_stop = {}
# #     dict_1 = {}
# #     hub_addy = 'HUB'
# #     route = 'HUB'
# #     start_point = hub_addy
# #     current_address = hub_addy
# #     # filtered_min = None
# #     destination = None
# #     visited_list = []
# #     filtered_min = None
# #     min_dist = 999
# #     dest_addresses = []
# #     i = 0
# #     edge = route_graph.edge_weights
# #
# #     default = path
# #     optimized = [route]
# #
# #     while len(default) > 0:
# #         min_dist = [0, default]
# #         for place in default:
# #             miles = edge[optimized[-1], place]
# #             if min_dist[0] == 0:
# #                 min_dist = [miles, place]
# #             if miles < min_dist[0]:
# #                 min_dist = [miles, place]
# #             if miles != 0 and miles < min_dist:
# #                 min_dist = [miles, place]
# #         if min_dist[1] not in optimized:
# #             optimized.append(min_dist[1])
# #         default.remove(min_dist[1])
#
#
# # for i in package_list:
# #     min_dist = 999
# #     i = hasher.search(int(i))
# #     for j in package_list:
# #         distance = g.find_dist[current_address][i]
# #         if distance < min_dist:
# #             distance = min_dist
#
# #
# #
# # for key, value in g.items():
# #     if current_address in key[0] and value > float(0.0):
# #         result = key
# #         min_dist = value
# #         kv = result, min_dist
# #         dict_1.update({kv})
# #         filtered_min = (min(dict_1.values()))
# #
# # for loc, distance in dict_1.items():
# #     if filtered_min == distance:
# #         kv1 = loc, distance
# #         # next_stop.update({kv1})
# #         next_list.clear()
# #         next_list.insert(0, loc[1])
# #         # list(set(next_list))
# #
# # address_set = list(set(next_list))
# # print(f"next list: {address_set}")
# # # print(f"kv1 = {kv1}")
# # # print(f"Next stop {filtered_min} miles away.")
# # start_point = next_list[0]
# # # print(f"next start point = {start_point}")
# # # print(f"dict 1: {dict_1.items()}")
# # return start_point
#
# def get_shortest_path(g, start, package):
#     address_list = []
#     start_point = None
#     my_truck = DeliveryTruck
#     next_stop = {}
#     dict_1 = {}
#     hub_addy = 'HUB'
#     start_point = hub_addy
#     current_address = hub_addy
#     # filtered_min = None
#     destination = None
#     visited_list = []
#     filtered_min = None
#     min_dist = 999
#     dest_addresses = []
#     i = 0
#
#     for key, value in g.items():
#         if current_address in key[0] and value > float(0.0):
#             result = key
#             min_dist = value
#             kv = result, min_dist
#             dict_1.update({kv})
#             filtered_min = (min(dict_1.values()))
#
#     for loc, distance in dict_1.items():
#         if filtered_min == distance:
#             kv1 = loc, distance
#             # next_stop.update({kv1})
#             next_list.clear()
#             next_list.insert(0, loc[1])
#             # list(set(next_list))
#
#     address_set = list(set(next_list))
#     print(f"next list: {address_set}")
#     # print(f"kv1 = {kv1}")
#     # print(f"Next stop {filtered_min} miles away.")
#     start_point = next_list[0]
#     # print(f"next start point = {start_point}")
#     # print(f"dict 1: {dict_1.items()}")
#     return start_point
#
# # def shortest(drawn_graph, start, goal):
# #     explored = []
# #     queue = start
# #
# #     if start == goal:
# #         print("Same node")
# #         return
# #     while queue:
# #         path = queue.pop
# #         node = path[-1]
# #
# #         if node not in explored:
# #             neighbors = drawn_graph[node]
# #
# #             for neighbor in neighbors:
# #                 new_path = list(path)
# #                 new_path.append(neighbor)
# #
# #                 if neighbor == goal:
# #                     print("Shortest path - " * new_path)
# #                     return
# #
# #             explored.append(node)
# #     print("no connected path")
# #     return

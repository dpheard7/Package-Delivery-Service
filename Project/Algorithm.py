def djikstra(graph, start):
    unvisited_queue = []
    for current_vertex in graph.adjacency_list:
        unvisited_queue.append(current_vertex)

    start.distance = 0

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


def get_shortest_path(start_vertex, end_vertex):
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = " -> " + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path
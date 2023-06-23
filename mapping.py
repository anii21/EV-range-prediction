import math
import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappop, heappush

def calculate_distance(coord1, coord2):
    # Calculate Euclidean distance between two coordinates
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_shortest_path(graph, start, goal):
    # Implementation of Dijkstra's algorithm to find the shortest path
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(queue, (distance, neighbor))
    return distances[goal]

def find_route(start, destination, charging_stations):
    # Create a graph with coordinates of the charging stations
    graph = nx.Graph()
    all_locations = [start, destination] + charging_stations
    for location in all_locations:
        graph.add_node(location)
        for other_location in all_locations:
            if location != other_l
            ocation:
                distance = calculate_distance(location, other_location)
                graph.add_edge(location, other_location, weight=distance)

    # Print the graph representation
    print("Graph representation:")
    print("Nodes:", graph.nodes)
    print("Edges:", graph.edges)

    # Visualize the graph
    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edge_labels(graph, pos)
    plt.show()

    # Find the nearest charging station to the start and destination
    nearest_start_station = min(charging_stations, key=lambda x: calculate_distance(start, x))
    nearest_dest_station = min(charging_stations, key=lambda x: calculate_distance(destination, x))

    # Find the shortest paths
    path_start_to_station = find_shortest_path(graph, start, nearest_start_station)
    path_station_to_dest = find_shortest_path(graph, nearest_dest_station, destination)

    # Combine the paths
    route = [(start, nearest_start_station)] + [(station, station) for station in charging_stations] + [(nearest_dest_station, destination)]
    total_distance = path_start_to_station + path_station_to_dest

    return route, total_distance

# Example usage
start = (0, 0)
destination = (10, 10)
charging_stations = [(2, 2), (5, 5), (8, 8)]

route, total_distance = find_route(start, destination, charging_stations)
print("Route:", route)
print("Total Distance:", total_distance)

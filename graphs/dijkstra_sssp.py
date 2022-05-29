from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra_algorithm(graph: Graph, source):
    visited = {source: 0}
    path = defaultdict(list)
    nodes = set(graph.nodes)
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break
        nodes.remove(min_node)
        for neighbour_node in graph.edges[min_node]:
            tentative_value = visited[min_node] + graph.distances[(min_node, neighbour_node)]
            if neighbour_node not in visited or tentative_value < visited[neighbour_node]:
                visited[neighbour_node] = tentative_value
                path[neighbour_node].append(min_node)
    return visited, path


customGraph = Graph()
customGraph.add_node("A")
customGraph.add_node("B")
customGraph.add_node("C")
customGraph.add_node("D")
customGraph.add_node("E")
customGraph.add_node("F")
customGraph.add_node("G")
customGraph.add_edge("A", "B", 2)
customGraph.add_edge("A", "C", 5)
customGraph.add_edge("B", "C", 6)
customGraph.add_edge("B", "D", 1)
customGraph.add_edge("B", "E", 3)
customGraph.add_edge("C", "F", 8)
customGraph.add_edge("D", "E", 4)
customGraph.add_edge("E", "G", 9)
customGraph.add_edge("F", "G", 7)

print(dijkstra_algorithm(customGraph, "A"))



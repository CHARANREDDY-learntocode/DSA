class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.nodes = []
        self.graph = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    @staticmethod
    def print_solution(dist):
        print("Vertex Distance from Source")
        for key, value in dist.items():
            print('  ' + key, ' :    ', value)

    def bellmanford_algorithm(self, src):
        distances = {i: float('inf') for i in self.nodes}
        distances[src] = 0
        for _ in range(self.v - 1):
            for s, d, w in self.graph:
                if distances[s] != float("Inf") and (distances[s] + w < distances[d]):
                    distances[d] = distances[s] + w

        for s, d, w in self.graph:
            if distances[s] != float("Inf") and (distances[s] + w < distances[d]):
                print("negative cycle found")
                return

        self.print_solution(distances)


g = Graph(5)
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellmanford_algorithm("E")




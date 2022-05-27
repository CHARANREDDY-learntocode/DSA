from collections import defaultdict
class Graph:
    def __init__(self, gc_dict: dict = None):
        if gc_dict is None:
            gc_dict = defaultdict(list)
        self.__gc_dict = gc_dict

    def get_data(self):
        return self.__gc_dict

    def addEdge(self, vertex, edge):
        self.__gc_dict[vertex].append(edge)

    def bfs(self, vertex):
        visited_list = [vertex]
        vertexes = [vertex]
        while vertexes:
            current_vertex = vertexes.pop(0)
            print(current_vertex)
            for adjacent_vertex in self.__gc_dict[current_vertex]:
                if adjacent_vertex not in visited_list:
                    visited_list.append(adjacent_vertex)
                    vertexes.append(adjacent_vertex)

    def dfs(self, vertex):
        visited_list = [vertex]
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            print(current_vertex)
            for adjacent_vertex in self.__gc_dict[current_vertex]:
                if adjacent_vertex not in visited_list:
                    visited_list.append(adjacent_vertex)
                    stack.append(adjacent_vertex)

    def __topological_sort_util(self, vertex, visited, stack):
        visited.append(vertex)
        for child_vertex in self.__gc_dict[vertex]:
            if child_vertex not in visited:
                self.__topological_sort_util(child_vertex, visited, stack)
        stack.insert(0, vertex)

    def topological_sort(self):
        visited, stack = [], []
        for vertex in list(self.__gc_dict):
            if vertex not in visited:
                self.__topological_sort_util(vertex, visited, stack)
        print(stack)


# data = {
#         "A": ["B", "C"],
#         "B": ["A", "D", "E"],
#         "C": ["A", "E"],
#         "D": ["B", "E", "F"],
#         "E": ["D", "F"],
#         "F": ["D", "E"]
#         }


customGraph = Graph()
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")
# print(graph.get_data())
# graph.add_edge("C", "G")
# print(graph.get_data()["C"])
# graph.bfs("A")
# print("======================================================")
# graph.dfs("A")
customGraph.topological_sort()

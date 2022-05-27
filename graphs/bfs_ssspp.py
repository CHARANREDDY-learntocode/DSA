class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.__gdict = gdict

    def bfs(self, start, end):
        queue = list()
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent_vertexes in self.__gdict.get(node, []):
                new_path = list(path)
                print(adjacent_vertexes)
                new_path.append(adjacent_vertexes)
                queue.append(new_path)


custom_dict = {"a": ["b", "c"],
               "b": ["d", "g"],
               "c": ["d", "e"],
               "d": ["f"],
               "e": ["f"],
               "g": ["f"]
              }
graph = Graph(custom_dict)
print(graph.bfs("a", "f"))

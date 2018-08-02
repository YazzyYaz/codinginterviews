from collections import defaultdict


class Graph(object):
    def __init__(self, connections, directed=False):
        self.graph = defaultdict(set)
        self.directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)
    
    def add(self, node1, node2):
        self.graph[node1].add(node2)
        if not self.directed:
            self.graph[node2].add(node1)

    def get_graph(self):
        return dict(self.graph)

    def route_node(self, node1, node2, path=[]):
        path += [node1]
        if node1 == node2:
            return path
        if node1 not in self.graph:
            return None
        for node in self.graph[node1]:
            if node not in path:
                new_path = self.route_node(node, node2, path)
                if new_path:
                    return new_path
        return None


connections = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'F'), ('C', 'D'), ('D', 'F')]
graph = Graph(connections, directed=True)
print(graph.get_graph())
print(graph.route_node('A', 'F'))

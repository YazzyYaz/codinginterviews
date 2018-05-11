from collections import defaultdict


class Graph(object):
    def __init__(self, connections, directed=False):
        self.directed = directed
        self.graph = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self.graph[node1].add(node2)
        if not self.directed:
            self.graph[node2].add(node1)

    def remove(self, node):
        for n, cnxns in self.graph.iteritems():
            if node in cnxns:
                cnxns.remove(node)

        if node in self.graph:
            del self.graph[node]

    def find_path(self, node1, node2, path=[]):
        path += [node1]
        if node1 == node2:
            return path
        if node1 not in self.graph:
            return None
        for node in self.graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

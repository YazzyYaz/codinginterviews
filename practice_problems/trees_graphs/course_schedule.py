from collections import defaultdict


def course_schedule(root, courses):
    alist = root.graph.keys()
    for node in alist:
    dfs_count = dfs(root, set())

def dfs(root, lookup=None):
    if root in lookup:
        return False
    lookup.add(root)
    for node in root.connections.keys():
        
    

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

    def get_graph_connections(self):
        return dict(self.graph)


connections = [(1, 0), (0, 2), (2, 4), (0, 3)]
graph = Graph(connections)
print(graph.get_graph_connections())

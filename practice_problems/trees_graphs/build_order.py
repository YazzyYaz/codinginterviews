def build_order(projects, dependencies):
    nodes = {}
    for project in projects:
        nodes[project] = GraphNode(project)
    for dependency in dependencies:
        nodes[dependency[0]].add(dependency[1])
    queue = Queue()
    for project in projects:
        node = nodes[project]
        if not node.dependencies_left:
            queue.enqueue(node)
    build_order = []
    while not queue.is_empty():
        node = queue.dequeue()
        build_order.append(node.value)
        for dependencies in node.edges:
            dependent.dependencies_left -= 1
            if not dependent.dependencies_left:
                queue.enqueue(dependent)
    if len(build_order) < len(projects):
        return Exception("Cycle Detected")
    return build_order


class GraphNode(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.dependencies_left = 0
    def add(self, node):
        self.dependencies_left += 1
        self.edges.append(node)


class Queue(object):
    def __init__(self):
        self.array = []
    
    def enqueue(self, value):
        self.array.insert(0, value)
    
    def dequeue(self):
        return self.array.pop()

    def is_empty(self):
        return self.array == []

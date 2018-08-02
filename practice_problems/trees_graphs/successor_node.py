def successor_node(node):
    if not node:
        return None
    child = node.right
    if child:
        while child:
            child = child.left
    if child:
        return child
    if node.parent and node.parent.value > node.value:
        return node.parent
    return None

class BSTNode(object):
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right
        self.parent = None
        if self.left: self.left.parent = self
        if self.right: self.right.parent = self

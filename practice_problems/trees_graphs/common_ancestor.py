def common_ancestor(node1, node2):
    search1, search2 = node1, node2
    ancestors1, ancestors2 = {}, {}
    while search1 or search2:
        if search1:
            if search1 in ancestors2:
                return search1
            ancestors1[search1] = True
            search1 = search1.parent
        if search2:
            if search2 in ancestors1:
                return search2
            ancestors2[search2] = True
            search2 = search2.parent
    return None


class BinaryTree(object):
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right
        self.parent = None
        if self.left: self.left.parent = self
        if self.right: self.right.parent = self

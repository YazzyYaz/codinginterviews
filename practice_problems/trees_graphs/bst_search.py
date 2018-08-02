def bst_search(node, n):
    if node:
        if node.value == n:
            return node
        elif node.value > n:
            node = bst_search(node.left, n)
        elif node.value < n:
            node = bst_search(node.right, n)
        return node


class BSTNode(object):
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

bst_root = BSTNode(10)
bst_root.left = BSTNode(5)
bst_root.left.left = BSTNode(3)
bst_root.left.right = BSTNode(6)
bst_root.right = BSTNode(15)
bst_root.right.left = BSTNode(13)
bst_root.right.right = BSTNode(17)

node = bst_search(bst_root, 13)
print(node.value)

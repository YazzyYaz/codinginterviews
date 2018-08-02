# https://www.afternerd.com/blog/python-check-tree-balanced/

class BinaryTree(object):
    def __init__(self, item, left=None, right=None):
        self.item, self.left, self.right = item, left, right

def get_height(node):
    if node is None:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))

def is_balanced(node):
    # if tree is none, it's balanced
    if node is None:
        return True
    return is_balanced(node.left) and is_balanced(node.right) and (abs(get_height(node.left) - get_height(node.right)) <= 1)

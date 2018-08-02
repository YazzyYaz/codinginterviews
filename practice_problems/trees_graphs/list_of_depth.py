def depth(binarytree):
    if binarytree == None:
        return 0
    if binarytree.left == None and binarytree.right == None:
        return 1
    else:
        depth_left = 1 + depth(binarytree.left)
        depth_right = 1 + depth(binarytree.right)
        if depth_left > depth_right:
            return depth_left
        return depth_right

def list_of_depth(binarytree, result={}, d=None):
    if d == None:
        d = depth(binarytree)
    if d not in result:
        result[d] = LinkedList(binarytree.data)
    else:
        result[d].add(binarytree.data)
    if binarytree.left:
        result = list_of_depth(binarytree.left, result, d-1)
    if binarytree.right:
        result = list_of_depth(binarytree.right, result, d-1)
    return result

class BinaryTree(object):
    def __init__(self, data=None, left=None, right=None)
        self.data, self.left, self.right = data, left, right

class LinkedList(object):
    def __init__(self, data, next=None):
        self.data, self.next = data, next

    def add(self, value):
        if not self.next:
            self.next = value
        else:
            self.next.add(value)

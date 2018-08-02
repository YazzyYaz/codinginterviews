def second_largest_bst(node):
    node_list = in_order(node, [])
    return node_list[-2]

def in_order(node, alist=None):
    if not node:
        return alist
    if node.left:
        in_order(node.left, alist)
    alist.append(node.value)
    if node.right:
        in_order(node.right, alist)
    return alist

class BinarySearchTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

bst_root = BinarySearchTreeNode(50)

bst_1 = BinarySearchTreeNode(48)
bst_2 = BinarySearchTreeNode(55)

bst_3 = BinarySearchTreeNode(45)
bst_4 = BinarySearchTreeNode(49)
bst_5 = BinarySearchTreeNode(52)
bst_6 = BinarySearchTreeNode(56)

bst_1.left = bst_3
bst_1.right = bst_4

bst_2.left = bst_5
bst_2.right = bst_6

bst_root.left = bst_1
bst_root.right = bst_2
print(second_largest_bst(bst_root))

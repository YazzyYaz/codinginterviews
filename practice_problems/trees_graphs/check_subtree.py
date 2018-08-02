def check_subtree(node1, node2):
    node1_list = get_tree_string(node1)
    node2_list = get_tree_string(node2)
    node1_string = "".join(node1_list)
    node2_string = "".join(node2_list)
    if len(node1_string) > len(node2_string):
        return node2_string in node1_string
    return node1_string in node2_string


def get_tree_string(node, alist=None):
    if node.value is None:
        return alist
    if not alist:
        alist = []
    alist.append(str(node.value))
    if node.left:
        get_tree_string(node.left, alist)
    if node.right:
        get_tree_string(node.right, alist)
    return alist


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

node_7 = Node(7)
node_1 = Node(1)
node_8 = Node(8)
node_8.left = node_7
node_8.right = node_1

node_8_2 = Node(8)
node_7_2 = Node(7)
node_9 = Node(9)
node_7_2.right = node_9
node_8_2.left = node_7_2
node_8_2.right = node_1

node_5 = Node(5)
node_6 = Node(6)
node_5.left = node_6
node_5.right = node_8_2

print(check_subtree(node_8, node_8_2))
print(check_subtree(node_5, node_8_2))

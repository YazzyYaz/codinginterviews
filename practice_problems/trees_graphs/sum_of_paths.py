def sum_of_paths(node, sum):
    if not node:
        return []
    res = []
    dfs(node, sum, [], res)
    return len(res)

def dfs(node, sum, ls, res):
    if not node.left and not node.right and sum == node.value:
        ls.append(node.value)
        res.append(ls)
    if node.left:
        dfs(node.left, sum-node.value, ls + [node.value], res)
    if node.right:
        dfs(node.right, sum-node.value, ls + [node.value], res)


class BinaryTree(object):
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

bt = BinaryTree(7)
bt_1 = BinaryTree(2)
bt_2 = BinaryTree(3)
bt_3 = BinaryTree(4)
bt_1.left = bt_2
bt_1.right = bt_3
bt.left = bt_1

bt_4 = BinaryTree(5)
bt_5 = BinaryTree(6)
bt_6 = BinaryTree(7)
bt_4.left = bt_5
bt_4.right = bt_6
bt.right = bt_4
print(sum_of_paths(bt, 13))

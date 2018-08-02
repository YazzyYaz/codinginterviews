import random


class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if not self.left:
            self.left = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if not self.right:
            self.right = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right = self.right
            self.right = new_node

    def pre_order(self, alist=None):
        if not alist:
            alist = []
        if not self.value:
            return alist
        alist.append(self.value)
        if self.left:
            self.left.pre_order(alist)
        if self.right:
            self.right.pre_order(alist)
        return alist

    def random_node(self):
        alist = self.pre_order()
        print(alist)
        return random.choice(alist)

node = BinaryTree(1)
node.insert_left(2)
node.insert_left(3)
node.insert_left(4)
node.insert_left(5)
node.insert_left(6)
node.insert_left(7)
node.insert_left(8)
node.insert_right(9)
node.insert_right(10)
node.insert_right(11)
node.insert_right(12)
node.insert_right(13)
node.insert_right(14)
node.insert_right(15)

print(node.random_node())

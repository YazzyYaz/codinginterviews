class BinarySearchTree(object):
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    def find_node(self, value):
        if value < self.value and self.left_child:
            self.left_child.find_node(value)
        if value > self.value and self.right_child:
            self.right_child.find_node(value)
        return value == self.value

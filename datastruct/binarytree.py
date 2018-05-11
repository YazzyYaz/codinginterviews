from queue import Queue


class BinaryTree(object):
    def __init__(self, item):
        self.item = item
        self.right_child = None
        self.left_child = None

    def add_left(self, item):
        if not self.left_child:
            self.left_child = BinaryTree(item)
        else:
            new_node = BinaryTree(item)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def add_right(self, item):
        if not self.right_child:
            self.right_child = BinaryTree(item)
        else:
            new_node = BinaryTree(item)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def pre_order(self):
        print(self.item)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.item)
        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.item)

    def bfs(self):
        queue = Queue()
        queue.put(self)
        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)
            if current_node.left_child:
                queue.put(current_node.left_child)
            if current_node.right_child:
                queue.put(current_node.right_child)

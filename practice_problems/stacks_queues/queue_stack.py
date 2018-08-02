class MyQueue(object):
    def __init__(self):
        self.stack1, self.stack2 = Stack(), Stack()

    def enqueue(self, item, stack=None):
        if not stack:
            self.stack1.push(item)
        else:
            stack.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            item_to_queue = self.stack1.items[0]
            item_list = self.stack1.items
            for item in range(len(item_list) - 1, 0, -1):
                self.enqueue(item_list[item], self.stack2)
                del item_list[item]
            item_list.pop()
            new_item_list = self.stack2.items
            for item in range(len(new_item_list) - 1, -1, -1): 
                self.enqueue(new_item_list[item], self.stack1)
                del new_item_list[item]

    def get_queue_list(self):
        return self.stack1.items
                

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        item = self.items[-1]
        self.items.pop()
        return item

    def is_empty(self):
        return self.items == []

queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)
print(queue.get_queue_list())
queue.dequeue()
print(queue.get_queue_list())
queue.dequeue()
print(queue.get_queue_list())
queue.enqueue(11)
print(queue.get_queue_list())

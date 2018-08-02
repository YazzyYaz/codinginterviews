class Stack(object):
    def __init__(self):
       self.items = []
       self.min_value = None 
    
    def push(self, item):
        if not self.min_value or self.min_value > item:
            self.min_value = item
        self.items.append(item)
    
    def pop(self):
        self.items.pop()

    def get_min_value(self):
        return self.min_value

stack = Stack()
stack.push(4)
stack.push(6)
stack.push(2)
print(stack.get_min_value())
stack.push(1)
print(stack.get_min_value())

class StackOfPlates(object):
    def __init__(self):
        self.stack = []
        self.capacity = 10

    def push(self, item):

        if self.stack and self.stack[-1].length() < 10:
            self.stack[-1].push(item)
        else:
            new_stack = Stack()
            new_stack.push(item)
            self.stack.append(new_stack)

    def pop(self):
        self.stack[-1].pop()
        if self.stack[-1].length == 0:
            del stack[-1]
    
    def popAt(self, index):
        self.stack[index].pop()


class Stack(object):
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items

    def length(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()
    
stack = StackOfPlates()
stack.push(1)
stack.push(10)
stack.push(11)
stack.push(12)
stack.push(13)
stack.push(14)
stack.push(15)
stack.push(16)
stack.push(17)
stack.push(18)
stack.push(19)
stack.push(20)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.stack[0].items)
print(stack.stack[1].items)
stack.pop()
stack.popAt(0)
print(stack.stack[0].items)
print(stack.stack[1].items)

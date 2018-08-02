def sort_stack(stack):
    temp_stack = Stack() 
    while not stack.is_empty():
        temp = stack.peek()
        stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            temp_top_val = temp_stack.peek()
            temp_stack.pop()
            stack.push(temp_top_val)
        temp_stack.push(temp)

    while not temp_stack.is_empty():
        top_temp_val = temp_stack.peek()
        temp_stack.pop()
        stack.push(top_temp_val)
    

class Stack(object):
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()

    def is_empty(self):
        return self.items == []

    def get_list(self):
        return self.items

    def peek(self):
        top_val = self.items[-1]
        return top_val


stack = Stack()
stack.push(1)
stack.push(6)
stack.push(3)
stack.push(9)
stack.push(5)
stack.push(11)
stack.push(4)
print(stack.get_list())
sort_stack(stack)
print(stack.get_list())

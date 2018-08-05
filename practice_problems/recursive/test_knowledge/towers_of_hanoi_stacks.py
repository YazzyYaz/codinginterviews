class Stack(object):
    def __init__(self, name):
        self.items = []
        self.name = name
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def length(self):
        return len(self.items)
    def is_empty(self):
        return self.items == [] 

def TowersOfHanoi(start, end, middle, n=None):
    if n is None:
        n = len(start.items)
    if n == 0:
        return
    TowersOfHanoi(start, middle, end, n-1)
    start, end = move_disc(start, end)
    TowersOfHanoi(middle, end, start, n-1)

def move_disc(start, end):
    print("Moving from " + start.name  + "to" + end.name)
    end.push(start.pop())
    return (start, end)


start, middle, end = Stack("Tower1"), Stack("Tower2"), Stack("Tower3")
start.push(5)
start.push(4)
start.push(3)
start.push(2)
start.push(1)

TowersOfHanoi(start, end, middle)
print(end.items)
print(start.items)
print(middle.items)

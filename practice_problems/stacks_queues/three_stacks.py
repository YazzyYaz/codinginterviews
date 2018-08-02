class ThreeStacks(object):
    def __init__(self):
        self.array = [None, None, None]
        self.current = [0, 1, 2]

    def push(self, item, stack_number):
        if not stack_number in [0, 1, 2]:
            raise Exception("Bad Stack Number")
        if len(self.array) <= self.current[stack_number]:
            self.array += [None] * len(self.array)
        self.array[self.current[stack_number]] = item
        self.current[stack_number] += 3

    def pop(self, stack_number):
        if not stack_number in [0, 1, 2]:
            raise Exception("Bad Stack Number")
        if self.current[stack_number] > 3:
            self.current[stack_number] -= 3
        item = self.array[self.current[stack_number]]
        self.array[self.current[stack_number]] = None
        return item

three_stacks = ThreeStacks()
print(three_stacks.array)
print(three_stacks.current)
three_stacks.push(101, 0)
print(101, 0)
print(three_stacks.array)
print(three_stacks.current)
three_stacks.push(102, 0)
print(102, 0)
print(three_stacks.array)
print(three_stacks.current)
three_stacks.push(103, 0)
print(103, 0)
print(three_stacks.array)
print(three_stacks.current)
three_stacks.push(201, 1)
print(201, 1)
print(three_stacks.array)
print(0)
print(three_stacks.pop(0))
print(three_stacks.array)
print(three_stacks.current)


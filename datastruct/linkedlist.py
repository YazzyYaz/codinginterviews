class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_item(self, new_item):
        self.item = new_item

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def count_size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        found = False
        current = self.head
        while not found and current is not None:
            if item == current.get_item():
                found = True
            current = current.get_next()
        return found

    def remove(self, item):
        found = False
        current = self.head
        previous = None
        while not found:
            if item == current.get_item():
                found = true
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

# https://www.geeksforgeeks.org/python-program-for-reverse-a-linked-list/

def reverse_linked_list(ll):
    prev = None
    curr = ll.head
    next = curr.get_next()
    while curr:
        curr.set_next(prev)
        prev = curr
        curr = next
        if next:
            next = next.get_next()
    ll.head = prev 
    return ll
    

class Node(object):
    def __init__(self, value, next=None):
        self.value, self.next = value, next

    def get_item(self):
        return self.item
    
    def get_next(self):
        return self.next

    def set_item(self, item):
        self.item = item

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
print(ll.head.value)
reverse_linked_list(ll)
print(ll.head.value)

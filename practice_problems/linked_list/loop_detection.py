def loop_detection(node):
    slow_pointer, fast_pointer = node, node
    while slow_pointer and fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            break
    
    slow_pointer = node
    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next
        if slow_pointer == fast_pointer:
            return fast_pointer
    return None

class Node(object):
    def __init__(self, data, next=None):
        self.data, self.next = data, next
    
node1 = Node(600)
node2 = Node(700,Node(800,Node(900,node1)))
node1.next = node2
head2 = Node(500, Node(200, Node(300, node1)))
print(loop_detection(head2).data)

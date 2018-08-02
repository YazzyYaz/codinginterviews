def remove_dupes(node):
    head = node
    if head:
        lookup_hash = {head.data: True}
        while head.next: 
            if head.next.data in lookup_hash:
               head.next = head.next.next 
            else:
                head = head.next

def remove_dupes2(node):
    current = node
    if current:
        while current.next:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next


class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


ll = Node(1, Node(2, Node(3, Node(1, Node(5, None)))))
remove_dupes2(ll)
print(ll.data)
print(ll.next.data)
print(ll.next.next.data)
print(ll.next.next.next.data)

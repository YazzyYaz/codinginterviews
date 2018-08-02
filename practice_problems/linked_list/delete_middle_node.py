def delete_middle_node(ll):
    current = ll
    if not current and not current.next:
        return None
    current.data = current.next.data
    current.next = current.next.next
    return current

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

ll = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
done = False
while not done:
    ll = ll.next
    if ll.data == 3:
        done = True
new_ll = delete_middle_node(ll)
print(new_ll.data)
print(new_ll.next.data)
print(new_ll.next.next.data)

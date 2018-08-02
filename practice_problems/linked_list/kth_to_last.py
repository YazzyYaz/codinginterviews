class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def kth_to_last(k, linked_list):
    pointer1, pointer2 = linked_list, linked_list
    for _ in range(k):
        if not pointer1:
            return None
        pointer1 = pointer1.next

    while pointer1:
        pointer1, pointer2 = pointer1.next, pointer2.next
    return pointer2

def kth_to_last2(k, linked_list):
    ll_length = 0 
    head = linked_list
    while head:
        ll_length += 1 
        head = head.next

    final_head = linked_list
    while final_head.next and k != ll_length:
        final_head = final_head.next
        ll_length -= 1

    return final_head
    
ll = Node(1, Node(2, Node(3, Node(4, None))))
k = 3
newll = kth_to_last2(k, ll)
print(newll.data)
print(newll.next.data)
print(newll.next.next.data)

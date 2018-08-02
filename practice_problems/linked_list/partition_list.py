def partition_list(linked_list, partition):
    ll_length = 0
    length_head = linked_list
    while length_head:
        ll_length += 1
        length_head = length_head.next

    partition_head = linked_list
    while partition_head and partition != ll_length:
        partition_head = partition_head.next
        ll_length -= 1
    

    partition_value = partition_head.data
    large_head = None
    large_tail = None
    small_head = None
    small_tail = None
    
    head = linked_list

    while head:
        print("head")
        print(small_head)
        print("tail")
        print(small_tail)

        if head.data < partition_value:
            if small_head:
                small_tail.next, small_tail = head, head
            else:
                small_head, small_tail = head, head
        else:
            if large_head:
                large_tail.next, large_tail = head, head
            else:
                large_head, large_tail = head, head
        head = head.next
    small_tail.next = large_head
    return small_head

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        string = str(self.data)
        if self.next:
            string += ',' + str(self.next)
        return string


ll = Node(1, Node(6, Node(3, Node(7, Node(2, Node(10, Node(4, Node(8, Node(5, None)))))))))
print(ll)
new_ll = partition_list(ll, 3)       
print(str(new_ll))

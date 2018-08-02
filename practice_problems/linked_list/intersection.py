def intersection(head1, head2):
    node1 = head1 
    node1_len = 0
    node1_tail = None
    while node1:
        node1_len += 1
        if not node1.next:
            node1_tail = node1
        node1 = node1.next
    
    node2 = head2
    node2_len = 0
    node2_tail = None
    while node2:
        node2_len += 2 
        if not node2.next:
            node2_tail = node2
        node2 = node2.next
    
    if node2_tail != node1_tail:
        return False
    
    if node1_len > node2_len:
        pointer_long = head1
        pointer_short = head2
    else:
        pointer_long = head2
        pointer_short = head1

    difference = abs(node1_len - node2_len)

    while difference != 0:
        pointer_long = pointer_long.next
        difference -= 1

    while pointer_long != pointer_short:
        pointer_long = pointer_long.next
        pointer_short = pointer_short.next

    return pointer_long



node = Node(70,Node(80))
head3 = Node(50,Node(20,node))
head4 = Node(60,Node(90,Node(10,node)))



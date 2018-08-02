def palindrome(node):
    original_list = []
    while node:
        original_list.append(int(node.data))
        node = node.next
    reversed_list = list(reversed(original_list))
    return reversed_list == original_list

class Node(object):
    def __init__(self, data, next=None):
        self.data, self.next = data, next

this_list = Node(1, Node(2, Node(3, Node(4, Node(3, Node(2, Node(1, None)))))))
other_list = Node(1, Node(3, Node(4, Node(5, Node(4, Node(2, Node(1, None)))))))
print(palindrome(this_list))
print(palindrome(other_list))

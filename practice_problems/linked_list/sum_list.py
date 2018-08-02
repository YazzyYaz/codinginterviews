def sum_list(node1, node2):
    node1_list = []
    node2_list = []
    while node1:
        node1_list.insert(0, str(node1.data))
        node1 = node1.next
    while node2:
        node2_list.insert(0, str(node2.data))
        node2 = node2.next

    node1_int = int("".join(node1_list))
    node2_int = int("".join(node2_list))
    node_total = str(node1_int + node2_int)
    node_int = [int(x) for x in node_total]
    new_node = Node(None, None)
    node1new, node2new = new_node, new_node
    for x in range(len(node_int)):
        node2new.data = node_int[x]
        node2new.next = Node(None, None)
        node2new = node2new.next
    return node1new

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

node1 = Node(7, Node(1, Node(6, None)))
node2 = Node(5, Node(9, Node(2, None)))
sum_list(node1, node2)

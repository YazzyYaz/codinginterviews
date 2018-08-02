import pprint


def bst_sequences(bst):
    return bst_sequences_partial([], [bst])

def bst_sequences_partial(partial, subtrees):
    if not len(subtrees):
        return [partial]
    sequences = []
    for index, subtree in enumerate(subtrees):
        next_partial = partial + [subtree.value]
        next_subtrees = subtrees[:index] + subtrees[index+1:]
        if subtree.left:
            next_subtrees.append(subtree.left)
        if subtree.right:
            next_subtrees.append(subtree.right)
        sequences += bst_sequences_partial(next_partial, next_subtrees)
    return sequences

class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value, self.left, self.right = value, left, right

tree = Node(7,Node(4,Node(5)),Node(9))
pprint.pprint(bst_sequences(tree))

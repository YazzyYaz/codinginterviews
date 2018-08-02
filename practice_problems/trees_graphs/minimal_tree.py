import math


def minimal_bst(alist):
    if len(alist) == 0:
        return None
    print(len(alist))
    mid = len(alist) / 2
    print(mid)
    print(alist[:mid])
    print(alist[mid+1:])
    left = minimal_bst(alist[:mid])
    right = minimal_bst(alist[mid+1:])
    return BSTNode(alist[mid], left, right)

class BSTNode(object):
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right
        
    def __str__(self):
        string = "(" + str(self.value)
        if self.left:  string += str(self.left)
        else:          string += "."
        if self.right: string += str(self.right)
        else:          string += "."
        return string + ")"

test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(minimal_bst(test_array))

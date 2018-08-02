def is_bst(binarytree):
    return is_bst_helper(binarytree, -float(inf), float(inf)

def is_bst_helper(binarytree, leftbound, rightbound):
    if not binarytree:
        return True
    if binarytree.data <= leftbound or binarytree.data >= rightbound:
        return False
    return is_bst_helper(binarytree.left, leftbound, binarytree.data) and is_bst_helper(binarytree.right, binarytree.data, rightbound)

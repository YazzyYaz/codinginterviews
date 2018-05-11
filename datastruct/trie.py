class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.counter = 1
        self.children = []
        self.word_finish = False

def add(root, word):
    node = root
    for char in word:
        character_found = False
        for child in node.children:
            if child.char == char:
                character_found = True
                child.counter += 1
                node = child
                break
        if not character_found:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node

def find_prefix(root, word):
    node = root
    if not root.children:
        return False, 0
    for char in word:
        character_found = False
        for child in node.children:
            if child.char == char:
                character_found = True
                node = child
                break
        if not character_found:
            return False, 0
    return True, node.counter
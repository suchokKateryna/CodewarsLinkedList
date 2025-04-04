class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    while node:
        if not index:
            return node
        node = node.next
        index -= 1
    raise IndexError

node = Node(4, Node(3, Node(2, Node(1, None))))
print(get_nth(node, 0))
print(get_nth(node, 1))
print(get_nth(node, 2))
print(get_nth(node, 3))
print(get_nth(node, 4))
print(get_nth(node, 5))

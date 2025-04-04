class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def stringify(node):
    res = ''
    while node:
        res += f"{node.data} -> "
        node = node.next
    return f"{res}None"

def reverse(current):
    if not current or not current.next:
        return current

    rest = current.next
    reversed_rest = reverse(rest)
    rest.next = current
    current.next = None

    return reversed_rest


print(stringify(reverse(Node(1, Node(2, Node(3, None))))))
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def stringify(node):
    res = ''
    while node:
        res += f"{node.data} -> "
        node = node.next
    return f"{res}None"

def push(head, data):
    res = Node(data)
    res.next = head
    return res

def build_one_two_three():
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)
    return chained

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source: Node, dest: Node):
    if not source:
        raise ValueError('Source is not present!')
    new_source = source.next
    source.next = dest
    return Context(new_source, source)

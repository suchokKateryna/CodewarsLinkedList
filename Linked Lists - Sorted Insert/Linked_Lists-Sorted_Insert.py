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

def sorted_insert(head, data):
    if head is None:
        return Node(data, None)
    start = None
    while head.data < data:
        if not head.next:
            pr = start
            start = Node(head.data)
            start.next = pr
            head = head.next
            break
        pr = start
        start = Node(head.data)
        start.next = pr
        head = head.next
    res = Node(data)
    res.next = head
    while start:
        pr = res
        res = Node(start.data)
        res.next = pr
        start = start.next
    return res

node = Node(1, Node(2, Node(3, Node(4, None))))
print(stringify(node))
print(stringify(sorted_insert(node, 2.5)))
print(stringify(sorted_insert(node, 0.5)))
print(stringify(sorted_insert(node, -0.5)))
print(stringify(sorted_insert(Node(1, None), 0.5)))
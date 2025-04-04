class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Context:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("Input list must have at least two nodes.")

    first_head = None
    first_tail = None
    second_head = None
    second_tail = None
    current = head
    count = 0

    while current:
        if count % 2 == 0:
            if first_head is None:
                first_head = current
                first_tail = current
            else:
                first_tail.next = current
                first_tail = current
        else:
            if second_head is None:
                second_head = current
                second_tail = current
            else:
                second_tail.next = current
                second_tail = current

        current = current.next
        count += 1

    if first_tail:
        first_tail.next = None
    if second_tail:
        second_tail.next = None

    return Context(first_head, second_head)

def stringify(node):
    res = ''
    while node:
        res += f"{node.data} -> "
        node = node.next
    return f"{res}None"

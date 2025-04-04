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

def reverse(current):
    if not current or not current.next:
        return current

    rest = current.next
    reversed_rest = reverse(rest)
    rest.next = current
    current.next = None

    return reversed_rest

def remove_duplicates(head):
    if head is None:
        return None

    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head

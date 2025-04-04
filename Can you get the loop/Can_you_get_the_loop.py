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

def loop_size(node):
    if not node or not node.next:
        return 0

    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if slow != fast:
        return 0

    count = 1
    current = slow.next
    while current != slow:
        count += 1
        current = current.next

    return count

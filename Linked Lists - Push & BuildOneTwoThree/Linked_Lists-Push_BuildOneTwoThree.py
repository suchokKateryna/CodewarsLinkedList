
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

c = Node(None)
c = push(c, 3)
print(stringify(c))
print(stringify(build_one_two_three()))
class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    linked_list = None
    for i in s.split(' -> ')[::-1][1:]:
        try:
            linked_list = Node(int(i), linked_list)
        except ValueError:
            linked_list = Node(i, linked_list)
    return linked_list

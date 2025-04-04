from preloaded import Node

def swap_pairs(head):
    dummy = Node(0)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        first = current.next
        second = current.next.next

        first.next = second.next
        second.next = first
        current.next = second

        current = current.next.next

    return dummy.next

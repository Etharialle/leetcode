# implementation of a linked list data structure


class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# Choosing to use root vs head so it is more similar to trees
class LinkedList:
    def __init__(self, root=None):
        self.root = root
    
    # prepend a node

    # append a node

    # insert node at position

    # get a node

    # print the list


ln = ListNode(2)
ll = LinkedList(ln)

print(ll)



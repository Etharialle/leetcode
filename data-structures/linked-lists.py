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
    def prepend_node(self, value=None):
        if value == None:
            print("no value argument")
            return
        if self.root == None:
            self.root = ListNode(value)
            return
        newNode = ListNode(value,self.root)
        self.root = newNode
        return


    # append a node

    # insert node at position

    # get a node

    # print the list
    def print_ll(self):
        if self.root == None:
            print("empty list")
            return
        current = self.root
        result = []
        result.append(str(current.value))
        while current.next:            
            current = current.next
            result.append(str(current.value))
        print(" -> ".join(result))
        return



ll = LinkedList()
ll.prepend_node(1)
ll.prepend_node(2)
ll.prepend_node()

ll.print_ll()



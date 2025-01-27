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
        newNode = ListNode(value)
        newNode.next = self.root
        self.root = newNode
        return


    # append a node
    def append_node(self, value=None):
        if value == None:
            print("no value argument")
            return
        if self.root == None:
            self.root = ListNode(value)
            return
        current = self.root
        newNode = ListNode(value)
        while current.next:
            current = current.next
        current.next = newNode
        return

    # insert node at position
    def insert_node(self, value, index=0):
        if self.root == None:
            self.root = ListNode(value)
            return
        if index == 0:
            newNode = ListNode(value)
            newNode.next = self.root
            self.root = newNode
            return
        pointer = 1
        current = self.root
        while index > pointer and current.next:
            current = current.next
            pointer += 1
        newNode = ListNode(value)
        newNode.next = current.next
        current.next = newNode
        return


    # get length of list
    def get_size(self):
        if self.root == None:
            return 0
        pointer = 1
        current = self.root
        while current.next:
            current = current.next
            pointer += 1
        return pointer

    # get a node
    def get_index(self, index=0):
        if self.root == None:        
            print("Empty List")
        if self.get_size() <= index:
            print("index out of range returning last node")
        pointer = 0
        current = self.root
        while pointer < index and current.next:
            current = current.next
            pointer += 1
        return current.value
        
    # finde node by value
    def find_value(self, value):
        if not self.root:
            print("Empty List")
            return 
        current = self.root
        while current:
            if current.value == value:
                return current
            current = current.next
        return None


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
ll.append_node(9)
print(ll.get_index(2))
ll.insert_node(7,3)
ll.print_ll()

print(ll.find_value(4))
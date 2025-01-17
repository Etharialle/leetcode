#inputs
l1 = [9,9,9,9,9,9,9]
# 2 -> 4 -> 3
l2 = [9,9,9,9]
# 5 -> 6 -> 4
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
test_node = ListNode(l1)
# Can we make a regular list out of each linked list?
# If so then the next step is to reverse both of the new lists
# add the lists together
# use the result list to create a new linked list
class LinkedList:
    def __init__(self):
        self.head = None

    @classmethod
    def from_listnode(cls, head: ListNode):
        """Converts an existing ListNode (single-node or chain) to a LinkedList."""
        new_list = cls()
        new_list.head = head
        return new_list

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)

    def create_list(self):
        current = self.head
        new_list = []
        while current:
            new_list.append(current.val)
            current = current.next
        return new_list
    
    def pretty_print(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.val))
            current = current.next
        print(" -> ".join(result) + " -> None")
    
new_ll = LinkedList.from_listnode(test_node)
new_ll.pretty_print()

ll1 = LinkedList()
ll2 = LinkedList()

for i in range(len(l1)):
    ll1.append(l1[i])
for i in range(len(l2)):
    ll2.append(l2[i])

ll1.pretty_print()
ll2.pretty_print()

first_list = ll1.create_list()
first_list.reverse()
second_list = ll2.create_list()
second_list.reverse()


first_str = ''.join(map(str, first_list))
print(first_str)
second_str = ''.join(map(str, second_list))
first_number = int(first_str)
second_number = int(second_str)

result_int = first_number + second_number
result_array = [int(x) for x in str(result_int)]
print(result_array)
result_array.reverse()
print(result_array)
ll_result = LinkedList()
for i in range(len(result_array)):
    ll_result.append(result_array[i])

ll_result.pretty_print()
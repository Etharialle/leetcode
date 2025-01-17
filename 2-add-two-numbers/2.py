#inputs
l1_list = [2,4,3]
# 2 -> 4 -> 3
l2_list = [5,6,4]
# 5 -> 6 -> 4
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1_2 = ListNode(l1_list[2])
l1_1 = ListNode(l1_list[1],l1_2)
l1 = ListNode(l1_list[0],l1_1)

l2_2 = ListNode(l2_list[2])
l2_1 = ListNode(l2_list[1],l2_2)
l2 = ListNode(l2_list[0],l2_1)

resultNode = ListNode()
currentNode = resultNode
carry = 0

while l1 or l2 or carry:
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0

    val = v1 + v2 + carry
    carry = val // 10 # floor division (this should always be either 0 or 1)
    val = val % 10 # get the remainder
    currentNode.next = ListNode(val)

    currentNode = currentNode.next
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None


# helper functions
def get_ll_length(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

def pretty_print_linked_list(head):
    if not head:
        print("Empty Linked List")
        return
    
    current = head
    result = []
    
    while current:
        result.append(str(current.val))  # Convert values to string for joining
        current = current.next
    
    print(" -> ".join(result) + " -> None")

# result (use `return resultNode.next` for LC)
pretty_print_linked_list(resultNode.next)
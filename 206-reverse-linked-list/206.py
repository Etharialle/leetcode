# Problem Statement
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import *

# inputs:
head = [1,2,3,4,5]


def create_linked_list(array):
    if not array:
        return None
    
    head = ListNode(array[0])
    current = head
    for i in array[1:]:
        current.next = ListNode(i)
        current = current.next
    
    return head

head = create_linked_list(head)

# To print the linked list for verification:
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

print_linked_list(head)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
    def reverse_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        
        while current:
            tempNode = current.next
            current.next = previous
            previous = current
            current = tempNode
        return previous



#print_linked_list(Solution().reverseList(head))
print_linked_list(Solution().reverse_iterative(head))


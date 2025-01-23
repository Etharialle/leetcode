# Problem Statement:
# Given the roots of two binary trees p and q, write a function to check
# if they are the same or not.
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.


from collections import deque
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def create_tree(self, array):
        if not array:
            return None
        
        root = TreeNode(array[0])
        queue = [root]
        index = 1
        while index < len(array):
            current = queue.pop(0)

            if index < len(array) and array[index] is not None:
                current.left = TreeNode(array[index])
                queue.append(current.left)
            index += 1

            if index < len(array) and array[index] is not None:
                current.right = TreeNode(array[index])
                queue.append(current.right)
            index += 1
        
        return root

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


def pretty_print_binary_tree(node, prefix="", is_left=True):
    if node is not None:
        # Print the current node value
        print(prefix + ("└── " if is_left else "├── ") + str(node.val))
        # Update the prefix for the child nodes
        new_prefix = prefix + ("    " if is_left else "│   ")
        pretty_print_binary_tree(node.right, new_prefix, False)
        pretty_print_binary_tree(node.left, new_prefix, True)
    
p = [1,2,1]
q = [1,1,2]

p_tree = TreeNode().create_tree(p)
q_tree = TreeNode().create_tree(q)
pretty_print_binary_tree(p_tree)
pretty_print_binary_tree(q_tree)




#q1 = deque()

#print(Solution().function()))
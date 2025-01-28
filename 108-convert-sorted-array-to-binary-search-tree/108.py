# Problem Statement: Given an integer array nums where the elements are sorted
# in ascending order, convert it to a height-balanced binary search tree.

from typing import *

# inputs:
nums = [-10,-3,0,5,9]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        bst = TreeNode(nums[mid])
        l_array = nums[l:mid]
        r_array = nums[mid+1:]
        print(bst)
        print(l_array)
        print(r_array)
        while l_array:
            mid = (l + len(l_array) - 1) // 2
            bst.left = l_array[mid]
            

Solution().sortedArrayToBST(nums)
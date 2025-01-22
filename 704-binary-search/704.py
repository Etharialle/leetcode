
from typing import List

# Problem Statement:
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# inputs
nums = [-1,0,3,5,9,12]
target = 9
nums = [-1,0,3,5,9,12]
target = 2

# method
# find the middle number position of the array
# compare the target to array[mid]
# if array[mid] == target return mid
# elif array[mid] > target search left
# elif array[mid] < target search right
# else return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1


print(Solution().search(nums,target))
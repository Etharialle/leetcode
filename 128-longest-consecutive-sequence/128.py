# Problem Statement:
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

from typing import *

nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 1
        nums.sort()
        for x in nums:
            tempResult = 1
            for y in nums:
                if y == x + 1:
                    tempResult += 1
                x = y
            if tempResult > result:
                result = tempResult
        return result
    
print(Solution().longestConsecutive(nums))
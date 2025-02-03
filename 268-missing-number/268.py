

from typing import *

nums = [0,1]

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        full_list = list(range(n+1))
        lookup = dict.fromkeys(full_list, 0)
        for x in nums:
            lookup[x] += 1
        result = min(lookup, key=lookup.get)
        return result
    
print(Solution().missingNumber(nums))
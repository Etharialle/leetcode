

from typing import *

nums = [0,1]

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        full_list = list(range(n+1))
        print(full_list)
        result = [x for x in full_list if x not in nums]
        return result
    
print(Solution().missingNumber(nums))
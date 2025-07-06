# Problem Statement: Given an integer array nums, return an array answer such
# that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import *
import math
# inputs:
nums = [1,2,3,4]




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []
        # for x in range(len(nums)):
        #     product = 1
        #     tempArray = nums.copy()
        #     del tempArray[x]
        #     for y in tempArray:
        #         product *= y
        #     result.append(product)
        # return result

        prefixArray = []
        suffixArray = []
        result = []
        for x in nums:
            prefix = math.prod(nums[:x])
            print(prefix)
            suffix = math.prod(nums[x+1:])
            answer = prefix * suffix
            result.append(answer)
        result_shift = result[-1:] + result[:-1]
        return result_shift


print(Solution().productExceptSelf(nums))
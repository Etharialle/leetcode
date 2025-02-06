
from typing import *
import math

n = 0

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        remainder = 0
        if n == 1:
            return True
        if n == -1 or n == 0:
            return False
        while remainder == 0:
            if n == 3:
                return True
            remainder = n % 3
            n = n / 3
        return False

print(Solution().isPowerOfThree(n))

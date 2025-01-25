# Problem Statement: Given an integer numRows, return the first numRows of
# Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

from typing import *

numRows = 5

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        n = 0
        while n < numRows:
            if n == 0:
                result.append([1])
            elif n == 1:
                result.append([1,1])
            else:
                last_row = result[-1]
                new_row = []
                new_row.append(1)
                for x in range(len(last_row)-1):
                    new_row.append(last_row[x] + last_row[x+1])
                new_row.append(1)
                result.append(new_row)
            n += 1
        return result
    
print(Solution().generate(numRows))
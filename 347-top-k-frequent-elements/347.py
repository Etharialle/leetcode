# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# inputs
nums = [1,1,1,2,2,3]
k = 2

def topKFrequent(nums: list[int], k: int) -> list[int]:
    lookup = {}
    for i in nums:
        if i not in lookup.keys():
            lookup[i] = 1
        else:
            lookup[i] += 1
    result = []
    while k > 0:
        tempMax = max(lookup, key=lookup.get)
        result.append(tempMax)
        del lookup[tempMax]
        k -= 1
    return result

print(topKFrequent(nums, k))
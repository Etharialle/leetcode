

# inputs
nums = [1,2,3]

# Problem: Given an integer array `nums`, return `true` if any value appears at
# least twice in the array, and return `false` if every element is distinct.

# brute force: nested loop, O(n**2) time complexity

def containsDuplicate(nums: list[int]) -> bool:
    result = False
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                result = True
                return result
    return result
    
answer = containsDuplicate(nums)
print(answer)

# Dictionary aka Hashmap

def containsDuplicate_hashmap(nums: list[int]) -> bool:
    lookup = {}
    for i in range(len(nums)):
        if nums[i] in lookup.keys():
            return True
        lookup[nums[i]] = i
    return False

print("answer is:")
print(containsDuplicate_hashmap(nums))
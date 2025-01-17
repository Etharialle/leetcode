# inputs
nums = [3,2,4]
target = 6
"""
# brute force attempt
for i in range(len(nums)-1):
    for j in range(1,len(nums)):
        result = nums[i] + nums[j]
        if result == target:
            answer = [i,j]
            print(answer)
            break
"""
# use a dictionary

newHashMap = {}
for i in range(len(nums)):
    result = target - nums[i]
    if result in newHashMap.keys():
        answer = [newHashMap[result], i]
        print(answer)
        break
    newHashMap[nums[i]] = i
print(newHashMap)

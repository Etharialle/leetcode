# Given two arrays, that are sorted and distinct, find the number
# of elements in common

# inputs:
a = [1,3,7,8,10,15]
b = [0,2,3,6,7,9,10,12,15]

# output:
# result = [3,7,10,15]

result = [x for x in a if x in b]
print(result)
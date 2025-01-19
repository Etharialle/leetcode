# Given two arrays, that are sorted and distinct, find the number
# of elements in common

# inputs:
a = [1,3,7,8,10,15]
b = [0,2,3,6,7,9,10,12,15]

# output:
# result = [3,7,10,15]

result = [x for x in a if x in b]
print(result)

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right -left) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

numberOfCommonElements = 0
for x in range(len(a)):
    if binary_search(b, a[x]) == True:
        numberOfCommonElements += 1

print(numberOfCommonElements)

# inputs
nums1 = [1,2]
nums2 = [3,4]

# merge sort the two arrays
# find median odd (length of merged array // 2 + 1)
# find median if even (length of median array // 2 and length of median array //2 + 1)
def two_pointer_merge(firstArray, secondArray):
    m, n = len(firstArray), len(secondArray)
    mergedArray = []
    i, j = 0, 0

    while i < m and j < n:
        if firstArray[i] < secondArray[j]:
            mergedArray.append(firstArray[i])
            i += 1
        else:
            mergedArray.append(secondArray[j])
            j += 1
    
    mergedArray.extend(firstArray[i:])
    mergedArray.extend(secondArray[j:])
    return mergedArray

resultArray = two_pointer_merge(nums1, nums2)
medianIndex = len(resultArray) // 2
if (len(resultArray) % 2) == 0:
    medianValue = (resultArray[(len(resultArray) // 2)-1] + resultArray[(len(resultArray) // 2)]) / 2
else:
    medianValue = resultArray[medianIndex]

print(medianValue)
#return medianValue
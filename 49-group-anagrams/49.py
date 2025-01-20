# inputs
strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]

# Problem Statement: Given an array of strings strs, group the 
# anagrams together. You can return the answer in any order.
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = []

    lookup = {}
    for x in strs:
        x_list = list(x)
        x_list.sort()
        x_tuple = tuple(x_list)
        if x_tuple not in lookup:
            lookup[x_tuple] = [x]
        else:
            current_list = []
            current_list = lookup[x_tuple]
            current_list.append(x)
            lookup[x_tuple] = current_list
    for x in lookup.values():
        result.append(x)
    return result


print(groupAnagrams(strs))

def groupAnagrams_hash(strs: list[str]) -> list[list[str]]:
    result = {}
    for x in strs:
        # create an array with each letter
        count = [0] * 26
        for c in x:
            # ord(c) - ord('a') returns the array position for count zero indexed
            count[ord(c) - ord('a')] += 1
        if tuple(count) not in result:
            result[tuple(count)] = [x]
        else:
            result[tuple(count)].append(x)
    return list(result.values())

print(groupAnagrams_hash(strs))

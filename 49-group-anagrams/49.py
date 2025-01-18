# inputs
strs = ["eat","tea","tan","ate","nat","bat"]

# Problem Statement: Given an array of strings strs, group the 
# anagrams together. You can return the answer in any order.
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # create a hashmap for each string
    result = {}

    for i in range(len(strs)):
        lookup = {}
        word = strs[i]
        print(word)
        for j in range(len(word)):
            if word[j] not in lookup.keys():
                lookup[word[j]] = 1
            else:
                lookup[word[j]] += 1
        print(lookup)
        if lookup not in result.keys():
            result[lookup] = 0

groupAnagrams(strs)


# inputs
s = "anagram"
t = "nagaram"

# Problem Statement: Given two strings s and t, return true if t is an anagram
# of s, and false otherwise.



def isAnagram(s: str, t: str) -> bool:
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    if sorted_s == sorted_t:
        return True
    else:
        return False
    
print(isAnagram(s,t))

def isAnagram_hash(s: str, t: str) -> bool:
    hash_s = {}
    for char in range(len(s)):
        if s[char] not in hash_s:
            hash_s[s[char]] = 0
        else:
            hash_s[s[char]] += 1
    
    hash_t = {}
    for char in range(len(t)):
        if t[char] not in hash_t:
            hash_t[t[char]] = 0
        else:
            hash_t[t[char]] += 1
    
    if hash_s == hash_t:
        return True
    else:
        return False

print("Hash Answer:")
print(isAnagram_hash(s,t))

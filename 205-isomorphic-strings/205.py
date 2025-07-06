# Problem Statement: Given two strings s and t, determine if they are isomorphic.
# 
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.

from typing import *

s = "egg"
t = "add"

s = "foo"
t = "bar"

s = "paper"
t = "title"

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_lookup = {}
        t_lookup = {}
        s_list = list(s)
        t_list = list(t)
        for x in s_list:
            if x not in s_lookup:
                s_lookup[x] = 1
            else:
                s_lookup[x] += 1
        
        for x in t_list:
            if x not in t_lookup:
                t_lookup[x] = 1
            else:
                t_lookup[x] += 1

        s_result = list(s_lookup.values())
        t_result = list(t_lookup.values())
        if s_result == t_result:
            return True
        return False

print(Solution().isIsomorphic(s,t))
         

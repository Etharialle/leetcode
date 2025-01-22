# Problem Statement
# A phrase is a palindrome if, after converting all uppercase letters into lowercase
# letters and removing all non-alphanumeric characters, it reads the same forward
# and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

# inputs
#s = "Racecar"
s = "A man, a plan, a canal: Panama"


def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    s_list = list(s)
    s_reverse = s_list
    s_reverse.reverse()
    if s_reverse == s_list:
        return True
    return False

print(isPalindrome(s))

def isPalindrome_pointers(s: str) -> bool:
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    print(len(s))
    x = 0
    y = len(s) - 1
    while x < y:
        y = (len(s) - 1) - x
        if s[x] != s[y]:
            return False
        x += 1
    return True

print(isPalindrome_pointers(s))
# inputs
s = " "

# brute force
# 1) initialize empty list
# 2) for loop to check if character is in list already if not increment length
# 3) remove first character from string, repeat 1 and 2, then remove second character until lenth of string either 0 or less than max length found

maxLength = 0
stringLength = len(s)
while stringLength > 0:
    lookup = []
    length = 0
    for char in range(len(s)):
        if s[char] not in lookup:
            length += 1
            lookup.append(s[char])
        else:
            break
    if length > maxLength:
        maxLength = length
    s = s.replace(s[0], "", 1)
    stringLength = len(s)
    if stringLength <= maxLength:
        break

print(maxLength)
# return maxLength


# optimized using the same idea as add two numbers
"""
lookup = {}
length = 0
maxLength = 0
lastRem = 0
for index, char in enumerate(s):
    if char in lookup and lastRem <= lookup[char]:
        length = 
"""
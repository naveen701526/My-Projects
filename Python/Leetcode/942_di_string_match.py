#https://leetcode.com/problems/di-string-match/
def diStringMatch(s):
    perm = []
    low = 0
    high = len(s)
    for char in s:
        if char == 'I':
            perm.append(low)
            low += 1
        else:
            perm.append(high)
            high -= 1
    perm.append(high)
    return perm

print(diStringMatch('III'))
print(diStringMatch('IDIDI'))

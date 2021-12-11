class Solution:
def canTransform(self, start: str, end: str) -> bool:

    so , eo , sind, eind = [],[],[],[]
    for i in range(len(start)):
        if start[i] != 'X':
            so.append(start[i])
            sind.append(i)
        if end[i] != 'X':
            eo.append(end[i])
            eind.append(i)
    if so != eo:
        return False
    
    for j in range(len(so)):
        if so[j] == 'L' and eind[j]>sind[j]:
            return False
        if so[j] == 'R' and eind[j]<sind[j]:
            return False
    
    return True

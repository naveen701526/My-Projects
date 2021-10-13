# https://leetcode.com/problems/shortest-distance-to-a-character/
def shortestToChar(s, c):
    c_occur = []
    answer = []
    for i in range(len(s)):
        if s[i] == c:
            c_occur.append(i)
    for i in range(len(s)):
        near = len(s)
        for j in c_occur:
            if abs(i-j) < near:
                near = abs(i-j)
        answer.append(near)
    return answer

print(shortestToChar('loveleetcode','e'))

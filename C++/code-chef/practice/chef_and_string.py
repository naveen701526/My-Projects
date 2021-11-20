# Problem Statement ---> https://www.codechef.com/problems/XYSTR
t = int(input())
for _ in range(t):
    s = input()
    count = 0
    prevFree = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1] and prevFree == 1:
            prevFree = 0
            count += 1
        else:
            prevFree = 1
    print(count)



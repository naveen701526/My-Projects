# Problem Statement ---> https://www.codechef.com/problems/FRUITS
t = int(input())

for _ in range(t):
    n, m, k = [int(x) for x in input().split()]
    if n == m:
        print(0)
    elif n > m:
        requiredDifference = n - m
        m += min(requiredDifference, k)
        print(abs(n-m))
    else:
        requiredDifference = m - n
        n += min(requiredDifference, k)
        print(abs(n-m))

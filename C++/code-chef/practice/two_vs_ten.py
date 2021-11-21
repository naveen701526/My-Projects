# Problem Statement ---> https://www.codechef.com/problems/TWOVSTEN
t = int(input())
for _ in range(t):
    n = int(input())
    if n % 10 == 0:
        print(0)
    elif n % 10 == 5:
        print(1)
    else:
        print(-1)

# Problem Statement ---> https://www.codechef.com/problems/CHN15A
t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    array = [int(x) for x in input().split()]
    count = 0
    for ar in array:
        if (ar + k) % 7 == 0:
            count += 1
    print(count)

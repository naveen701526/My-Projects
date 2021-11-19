t = int(input())

for i in range(t):
    n = int(input())
    b = [int(x) for x in input().split()]
    flag = 0
    for i in range(1, len(b)):
        if b[i-1] % b[i]:
            flag = 1
    if flag == 1:
        print('-1')
    else:
        for i in b:
            print(i, end=" ")
    print()

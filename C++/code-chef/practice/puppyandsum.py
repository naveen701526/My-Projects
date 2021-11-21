t = int(input())


def sumFunc(sumValue):
    return sum([int(x) for x in range(1, sumValue+1)])


for _ in range(t):
    d, n = [int(x) for x in input().split()]
    sumValue = 0
    sumValue += sumFunc(n)
    # print(sumValue)
    for i in range(d-1):
        sumValue = sumFunc(sumValue)
    print(sumValue)

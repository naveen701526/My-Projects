r = int(input())
sum1, sum2 = 0, 0
lead = 0
winner = 0

for i in range(r):
    p1, p2 = [int(x) for x in input().split()]
    sum1 += p1
    sum2 += p2

    if sum1 > sum2:
        val = sum1-sum2
        if val > lead:
            lead = val
            winner = 1
    else:

        val = sum2-sum1
        if val > lead:
            lead = val
            winner = 2
print(winner, end=" ")
print(lead)

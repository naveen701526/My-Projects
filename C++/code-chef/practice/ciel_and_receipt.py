# Problem Statement ---> https://www.codechef.com/problems/CIELRCPT
t = int(input())

for i in range(t):
    number = int(input())
    count = 0
    for i in range(11, -1, -1):
        power = pow(2, i)
        while number >= power:
            number -= power
            count += 1
    print(count)

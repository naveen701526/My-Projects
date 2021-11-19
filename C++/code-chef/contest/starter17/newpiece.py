# Problem Statement ---> https://www.codechef.com/START17C/problems/NEWPIECE
# cook your dish here
t = int(input())

for i in range(t):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    if x1 == x2 and y1 == y2:
        print('0')
    elif ((x1+y1) % 2 == 0 and (x2+y2) % 2 == 0) or ((x1+y1) % 2 == 1 and (x2+y2) % 2 == 1):
        print('2')
    else:
        print('1')

# Problem Statement - -- -> https: // www.codechef.com/START17C/problems/STRADJ
t = int(input())

for i in range(t):
    n = int(input())
    string = input()
    count1 = 0
    count0 = 0
    for i in string:
        if i == '1':
            count1 += 1
        else:
            count0 += 1

    if min(count0, count1) == 0:
        print('Bob')
    elif min(count1, count0) == 1:
        print('Alice')
    else:
        if len(string) % 2:
            print('Alice')
        else:
            print('Bob')

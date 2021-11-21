# Problem Statement ---> https://www.codechef.com/problems/HEADBOB
t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    if 'I' in string:
        print('INDIAN')
    elif 'Y' not in string:
        print('NOT SURE')
    else:
        print('NOT INDIAN')

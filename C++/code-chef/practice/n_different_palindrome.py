# Problem Statment ---> https://www.codechef.com/problems/NDIFFPAL
t = int(input())


for i in range(t):
    number = int(input())

    ascii = 97
    ans = ''
    i = 0
    while number > 0:
        ans += chr(ascii+i)
        number -= 1
        i = (i+1) % 26
    print(ans)

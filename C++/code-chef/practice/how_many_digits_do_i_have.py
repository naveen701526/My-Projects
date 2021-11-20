# Problem Statement ---> https://www.codechef.com/problems/HOWMANY

# cook your dish here
num = list(input())
if len(num) == 1:
    print('1')
elif len(num) == 2:
    print('2')
elif len(num) == 3:
    print(3)
else:
    print("More than 3 digits")

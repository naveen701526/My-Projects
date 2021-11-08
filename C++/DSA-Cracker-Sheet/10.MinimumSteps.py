import math


class Solution:
    def minJumps(self, arr, n):
       # 1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9 --> input example
        if n <= 1:
            return 0
        if not arr[0]:
            return -1
        maxReach = arr[0]  # 1
        step = arr[0]  # 1
        jump = 1  # 1
        for i in range(1, n):  # 3, 5, 8, 9, 2, 6, 7, 6, 8, 9
            if i == n - 1:  # last index of array
                return jump  # 3
            # (1,4) , (4,7), (7,11), (11,13), (13,7), (7,12), (12,14), (14, 17), (17, 19)
            maxReach = max(maxReach, i + arr[i])
            step -= 1  # 0, 2, 1, 0, 8, 7, 6, 5, 4
            if step == 0:
                jump += 1  # 2, 3
                if i >= maxReach:  # 1>=4(false), 4>=13(false),
                    return -1
                step = maxReach - i  # 3, 9
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr, n)
        print(ans)
# } Driver Code Ends

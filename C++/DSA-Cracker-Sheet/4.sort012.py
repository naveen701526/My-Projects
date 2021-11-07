
class Solution:
    def sort012(self, arr, n):
        # code here
        hash = {}
        for i in arr:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        j = 0
        for i in hash:

            while hash[i] != 0:
                arr[j] = i
                hash[i] -= 1
                j += 1


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr, n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends

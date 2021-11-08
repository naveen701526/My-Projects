
class Solution:
    # Function to return the count of number of elements in union of two arrays.
    def doUnion(self, a, n, b, m):

        hash1 = {}
        hash2 = {}
        for i in a:
            if i in hash1:
                hash1[i] += 1
            else:
                hash1[i] = 1
        for i in b:
            if i in hash2:
                hash2[i] += 1
            else:
                hash2[i] = 1
        result = len(hash2)
        for i in hash1:
            if i in hash2:
                continue
            else:
                result += 1
        return result

# {
#  Driver Code Starts
# Initial Template for Python 3


# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n, m = [int(x) for x in input().strip().split()]

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.doUnion(a, n, b, m))
# } Driver Code Ends

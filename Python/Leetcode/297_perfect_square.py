class Solution:
    def numSquares(self, n: int) -> int:
        if int(sqrt(n))**2 == n: return 1
        for j in range(int(sqrt(n))+1):
            if int(sqrt(n - j*j))**2 == n - j*j: return 2
        for i in range(int(sqrt(n))+1):
            for j in range(i,int(sqrt(n))+1):
                if n-i*i-j*j > 0 and int(sqrt(n-i*i-j*j))**2 == n - i*i - j*j: return 3
        return 4

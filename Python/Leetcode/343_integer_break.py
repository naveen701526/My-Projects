class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        
        num3 = n//3
        maxv = 1
        for i in range(num3+1):
            res = n - 3*i
            if res %2 == 0:
                num2 = res//2
                maxv = max(maxv, 2**num2*3**i)
        return maxv
        
        
opt = Solution()
print(opt.integerBreak(n = 2))
print(opt.integerBreak(n = 10))

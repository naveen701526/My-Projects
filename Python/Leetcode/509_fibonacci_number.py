class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        while n >1:
            return self.fib(n-1) + self.fib(n-2)
            
            
opt = Solution()
print(opt.fib(n = 2))
print(opt.fib(n = 3))

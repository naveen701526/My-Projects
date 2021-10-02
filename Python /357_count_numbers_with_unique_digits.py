class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = [1]
        for k in range(1, n+1):
            base = available = 9
            for _ in range(k-1):
                base *= available 
                available -= 1
            ans.append(base+ans[-1])    
        return ans[-1]
        
        
opt = Solution()
print(opt.countNumbersWithUniqueDigits(n=2))
print(opt.countNumbersWithUniqueDigits(n=3))

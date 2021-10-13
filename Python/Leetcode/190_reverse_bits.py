class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in reversed(range(32)):
            res|=(n&1)<<i
            n>>=1
            
        return res
        
        
opt = Solution()
print(opt.reverseBits(11111111111111111111111111111101))

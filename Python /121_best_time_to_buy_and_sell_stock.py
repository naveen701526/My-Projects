class Solution:
    # Maximize prices[i] - prices[j], for i < j
    def maxProfit(self, prices: [int]) -> int:
        last, res = prices[0], -float('inf')
        for p in prices[1:]:
            res = max(res, p-last)
            last = min(last, p)
        return 0 if res < 0 else res
        
        
opt = Solution()
print(opt.maxProfit([7,1,5,3,6,4]))

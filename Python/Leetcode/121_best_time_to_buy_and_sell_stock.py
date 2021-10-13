class Solution:
    # Maximize prices[i] - prices[j], for i < j
    def maxProfit(self, prices: [int]) -> int:
        last, res = prices[0], -float('inf') #consider last as first value of the prices list
        #res has the lowest negative number 
        for p in prices[1:]:
            res = max(res, p-last) #take the maximum profit until
            # now by current element - price of stock
            last = min(last, p) #day at which price of stock is lowest.
            #because to earn max profit we need to buy the 
            # stock and lowest rate possible and sell it at highest rate possible.
            
        return 0 if res < 0 else res #0 if no profit made till the last day, lest give answer
        
        
opt = Solution()


print(opt.maxProfit([7,1,5,3,6,4]))

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > low:
                profit += prices[i] - low
                low = prices[i]
            else: low = prices[i]
        return profit
		

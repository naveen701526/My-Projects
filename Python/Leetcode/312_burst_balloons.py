from functools import lru_cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        @lru_cache(None)
        def dp(i, j):
            """dp(i, j) represents the maximum coins after bursting all baloons between i and j."""
            if i > j:
                return 0
            if i == j:
                return nums[i-1] * nums[i] * nums[i+1]
            return max(dp(i, k-1) + dp(k+1, j) + nums[i-1] * nums[k] * nums[j+1] for k in range(i, j+1))
        return dp(1, len(nums) - 2)

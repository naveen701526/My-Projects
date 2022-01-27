class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        sol = 0
        for i in reversed(range(32)):
            prefixs = set([x >> i for x in nums])
            sol <<= 1
            candidate = sol + 1
            for p in prefixs:
                if candidate ^ p in prefixs:
                    sol = candidate
                    break
        return sol

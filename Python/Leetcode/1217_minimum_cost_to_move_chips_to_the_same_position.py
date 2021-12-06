class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = sum(pos % 2 for pos in position)
        return min(odd, len(position) - odd)

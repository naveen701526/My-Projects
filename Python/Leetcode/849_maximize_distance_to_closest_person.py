class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, last = 0, -1
        for i, seat in enumerate(seats):
            if seat:
				# `else i` takes care of the edge case when we do not have a seat at first index
                res = max(res, (i - last) // 2 if last >= 0 else i)
                last = i
		# `len(seats) - 1 - last` takes care of the edge case when we do not have a seat at last index
        return max(res, len(seats) - 1 - last if not seats[-1] else 0)

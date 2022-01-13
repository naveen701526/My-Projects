class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = []
        cnt = 0
        for x in sorted(points, key = lambda x: x[1]):
            if res and x[0] <= res[-1][1]:
                cnt += 1
            else:
                res.append(x)
        return len(points) - cnt 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in intervals:
            if i[0] > end:
                ans.append([start, end])
                start, end = i[0], i[1]
            else:
                end = max(end, i[1])
        ans.append([start, end])
        return ans

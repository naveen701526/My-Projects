class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        max_val = timeSeries[0] + duration - 1
        anchor = timeSeries[0]
        for i in range(1, len(timeSeries)):
            if max_val < timeSeries[i]:
                res += max_val - anchor + 1  
                anchor = timeSeries[i]
                max_val = timeSeries[i] + duration - 1
                pass
            else:
                max_val = timeSeries[i] + duration - 1
        res += max_val - anchor + 1  
        return res

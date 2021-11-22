class Solution:
    def findRelativeRanks(self, score):
        ranking = {'0': 'Gold Medal', '1': 'Silver Medal', '2': 'Bronze Medal'}
        array = sorted(score, reverse=True)
        result = []
        for scr in score:
            if str(array.index(scr)) in ranking:
                result.append(ranking[str(array.index(scr))])
            else:
                result.append(str(array.index(scr)+1))
        return result


obj = Solution()
print(obj.findRelativeRanks([5, 4, 3, 2, 1]))

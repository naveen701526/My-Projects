class Solution:
    def distributeCandies(self, candyType) -> int:
        candyTypes = list(set(candyType))
        maxCandies = len(candyTypes)
        candiesAliceCanEat = len(candyType)//2
        return min(candiesAliceCanEat, maxCandies)


obj = Solution()
print(obj.distributeCandies([1,1,2,3]))
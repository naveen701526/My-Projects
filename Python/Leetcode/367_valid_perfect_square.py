class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        high = 2147483647
        low = 1
        while low <= high:
            mid = low + (high-low)//2
            square = mid*mid
            if square == num:
                return True
            elif square > num:
                high = mid - 1
            else:
                low = mid + 1
        return False


obj = Solution()
print(obj.isPerfectSquare(178))

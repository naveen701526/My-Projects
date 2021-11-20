# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

def guess(num: int) -> int:
    pick = 6
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            mid = left + (right - left)//2
            result = guess(mid)
            if result == 0:
                return mid
            elif result < 0:
                right = mid - 1
            else:
                left = mid + 1

        return -1


obj = Solution()


print(obj.guessNumber(10))

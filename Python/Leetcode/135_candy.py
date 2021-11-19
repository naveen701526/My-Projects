# Problem Statement ----> https://leetcode.com/problems/candy/


class Solution:
    def candy(self, ratings) -> int:
        n = len(ratings)
        leftArray = [1]*n
        rightArray = [1]*n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                leftArray[i] += leftArray[i-1]
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rightArray[i] += rightArray[i+1]

        sums = 0
        for i in range(n):
            if leftArray[i] > rightArray[i]:
                sums += leftArray[i]
            else:
                sums += rightArray[i]
        return sums


obj = Solution()

print(obj.candy([1, 0, 2]))
print(obj.candy([1, 2, 2]))

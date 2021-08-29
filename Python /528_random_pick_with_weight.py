# https://leetcode.com/problems/random-pick-with-weight/
import random
class Solution:

    def __init__(self, w):
        self.prefix_sum = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        random_num = self.total_sum * random.random()
        low, high = 0, len(self.prefix_sum)
        while low < high:
            mid = low + (high - low) // 2
            if random_num > self.prefix_sum[mid]:
                low = mid + 1
            else:
                high = mid
        return low
        


# Your Solution object will be instantiated and called as such:
obj = Solution([1,3,4])
param_1 = obj.pickIndex()
print(param_1)

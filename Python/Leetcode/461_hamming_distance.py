# Problem Statement --> https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xorGate = x ^ y
        count = 0
        while xorGate > 0:
            count += xorGate & 1
            xorGate = xorGate >> 1
        return count


obj = Solution()
print(obj.hammingDistance(4, 1))

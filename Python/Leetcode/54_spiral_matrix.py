# Problem Statement ---> https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix):
        top, left = 0, 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        direction = 0
        ans = []
        while top <= bottom and left <= right:
            if direction == 0:
                for i in range(left, right+1):
                    ans.append(matrix[top][i])
                top += 1
            elif direction == 1:
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            elif direction == 3:
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1
            direction = (direction + 1) % 4
        return ans

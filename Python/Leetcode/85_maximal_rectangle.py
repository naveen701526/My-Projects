class Solution:
    def maximalRectangle(self, matrix) -> int:
        def largestRectangleArea(heights):
            stack, result = [], 0
            for idx, i in enumerate(heights+[0]):
                while stack and heights[stack[-1]] > i:
                    h = heights[stack.pop()]
                    w = idx - stack[-1] - 1 if stack else idx
                    result = max(result, w * h)
                stack.append(idx)
            return result

        for r in range(0, len(matrix)):
            for c in range(len(matrix[0])):
                if(matrix[r][c] == '1'):
                    matrix[r][c] = int(matrix[r][c]) + \
                        int(matrix[r-1][c] if(r > 0) else 0)
                else:
                    matrix[r][c] = 0

        return max(largestRectangleArea(row) for row in matrix) if matrix else 0

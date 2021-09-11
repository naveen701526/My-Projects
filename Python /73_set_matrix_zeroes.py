class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        rowZero = True
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        if matrix[0][0] == 0:
            for row in range(rows):
                matrix[row][0] = 0
        if rowZero:
            for col in range(cols):
                matrix[0][col] = 0
                
        print(matrix)
                
                
opt = Solution()
opt.setZeroes([[1,1,1],[1,0,1],[1,1,1]])

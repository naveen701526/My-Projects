class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        for j in range(1,cols):#Prefix sum of the first row
            grid[0][j]+=grid[0][j-1]
        for i in range(1,rows):#Prefix sum of the first col
            grid[i][0]+=grid[i-1][0]
        for i in range(1,rows):
            for j in range(1,cols):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])#Take the min of col above curr cell and col left to curr cell and add it to curr cell value
        return grid[-1][-1]

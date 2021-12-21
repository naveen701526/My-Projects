class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        dp = []
        for i in range(rows):
            c = [0]*columns
            dp.append(c)
        for i in range(rows):
            for j in range(columns):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[rows-1][columns-1]

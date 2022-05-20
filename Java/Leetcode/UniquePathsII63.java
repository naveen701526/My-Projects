class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[][] memo = new int[m][n];
        return uniquePathsWithObstacles(obstacleGrid, m - 1,n - 1,memo);
    }
    
    public int uniquePathsWithObstacles(int[][] obstacleGrid, int m, int n, int[][] memo) {
        if(m < 0 || n < 0 || obstacleGrid[m][n] == 1){
            return 0;
        }
        if(m == 0 && n == 0){
            return 1;
        }
        if(memo[m][n] != 0){
            return memo[m][n];
        }
        return memo[m][n] = uniquePathsWithObstacles(obstacleGrid, m-1, n,memo) + uniquePathsWithObstacles(obstacleGrid, m, n-1,memo);

    }
    
}

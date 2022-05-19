class Solution {
    int[][] dp;
    public int longestIncreasingPath(int[][] matrix) {
        int ans=0;
        dp = new int[matrix.length][matrix[0].length];
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                ans = Math.max(ans,dfs(matrix,i,j,-1));
            }
        }
        return ans;
    }
    int dfs(int[][] mat,int r,int c,int pre){
        if(r<0 || c<0 || r==mat.length || c==mat[0].length || mat[r][c]<=pre)
            return 0;
        if(dp[r][c]>0) 
            return dp[r][c];
        int res = 1;
        res = Math.max(res,1+dfs(mat,r-1,c,mat[r][c]));
        res = Math.max(res,1+dfs(mat,r+1,c,mat[r][c]));
        res = Math.max(res,1+dfs(mat,r,c-1,mat[r][c]));
        res = Math.max(res,1+dfs(mat,r,c+1,mat[r][c]));
        dp[r][c] = res;
        return res;
    }
}

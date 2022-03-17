class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        
        int rows = mat.length;
        int columns = mat[0].length;
        if (rows * columns != r * c)
            return mat;
        int row_it = 0;
        int col_it = 0;
        
        int[][] ans = new int[r][c];
        for (int i = 0; i<r; i++)
        {
            for (int j = 0; j<c;j++)
            {
                ans[i][j] = mat[row_it][col_it++];
                if(col_it == columns){
                    col_it %= columns;
                    row_it++;
                }
                    
            }
        }
        return ans;
        
    }
}

class Solution {
    public int surfaceArea(int[][] grid) {
        int area = 0 ;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                //adding top and bottom area if the box tower exists
                if (grid[i][j] > 0) {
                    area += 2 ;
                }
                
                //checking left of the box tower
                if (j-1 >= 0) {
                    if (grid[i][j-1] < grid[i][j]) {
                        area += grid[i][j] - grid[i][j-1] ;
                    }
                }
                else {
                    area += grid[i][j] ;
                }
                
                //checking right of the box tower
                if (j+1 < grid[i].length) {
                    if (grid[i][j] > grid[i][j+1]) {
                        area += grid[i][j] - grid[i][j+1] ;
                    }
                }
                else {
                    area += grid[i][j] ;
                }
                
                //checking up of the box tower
                if (i-1 >= 0) {
                    if (grid[i][j] > grid[i-1][j]) {
                        area += grid[i][j] - grid[i-1][j] ;
                    }
                }
                else {
                    area += grid[i][j] ;
                }
                
                //checking down of the box tower
                if (i+1 < grid.length) {
                    if (grid[i][j] > grid[i+1][j]) {
                        area += grid[i][j] - grid[i+1][j] ;
                    }
                }
                else {
                    area += grid[i][j] ;
                }
            }
        }
        
        return area ;
    }
}

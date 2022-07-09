class Solution {
    public int islandPerimeter(int[][] grid) {
      int countblocks=0,neighbours=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==1){
                    countblocks++;
                if(i!=grid.length-1 && grid[i+1][j]==1){
                    neighbours++;
                }
                if(j!=grid[0].length-1 && grid[i][j+1]==1){
                    neighbours++;
                }}
            }
        }
        return (4*countblocks -(neighbours*2));
    }
}

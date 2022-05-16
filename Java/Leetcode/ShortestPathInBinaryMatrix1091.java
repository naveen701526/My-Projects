class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
       
        int n = grid.length;
        if(grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;
        
        int[] dx = new int[]{1, -1, 0, 0, 1, 1, -1, -1};
        int[] dy = new int[]{0, 0, 1, -1, 1, -1, -1, 1};
        
        int[][] visited = new int[n][n];
        Queue<int[]> que =  new LinkedList<>();
        que.add(new int[]{0, 0});
        visited[0][0] = 1;
        
        while(!que.isEmpty()){
            int[] temp = que.remove();
            int i = temp[0];
            int j = temp[1];
            
            for(int d = 0; d < 8; d++){
                int x = i + dx[d];
                int y = j + dy[d];
                
                if(x >= 0 && x < n && y >= 0 && y < n && visited[x][y] == 0 && grid[x][y] == 0){
                    visited[x][y] = visited[i][j] + 1;
                    que.add(new int[]{x, y});
                }
            }
            
        }
        
        return visited[n-1][n-1] != 0 ? visited[n-1][n-1] : -1;
    }
}

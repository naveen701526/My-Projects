class Solution {
    private int m;
    private int n;
    private int[][] heights;
    private int[][] visited;
    private final int[][] dirs = new int[][] { 
        { 1, 0 }, 
        {-1, 0 },
        { 0, 1 },
        { 0,-1 }
    };
    public int minimumEffortPath(int[][] heights) {
        this.heights = heights;
        this.m = heights.length;
        this.n = heights[0].length;
        if (m == 1 && n == 1) return 0;
        this.visited = new int[m][n];
        for (int[] v: visited) {
            Arrays.fill(v, Integer.MAX_VALUE);
        }
        PriorityQueue<Node> q = new PriorityQueue<>((a, b) -> a.diff - b.diff);
        q.add(new Node(0, 0, 0));
        visited[0][0] = 0;
        while (!q.isEmpty()) {
            Node c = q.poll();
            if (c.x == m - 1 && c.y == n - 1) {
                return visited[m - 1][n - 1];
            }
            if (c.diff > visited[c.x][c.y]) continue;
            for (int[] dir: dirs) {
                int x = dir[0] + c.x;
                int y = dir[1] + c.y;
                if (x < 0 || y < 0 || x >= m || y >= n) continue;
                int diff = Math.max(Math.abs(heights[c.x][c.y] - heights[x][y]), visited[c.x][c.y]) ;
                if (diff >= visited[x][y]) continue;
                visited[x][y] = diff;
                q.offer(new Node(x, y, diff));
            }
        }
        return 0;
    }
    public class Node {
        public int x;
        public int y;
        public int diff;
        public Node(int x, int y, int diff) {
            this.x = x;
            this.y = y;
            this.diff = diff;
        }
    }
}

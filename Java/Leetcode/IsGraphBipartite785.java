class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] colors = new int[n];
        
        for(int i = 0; i < n; i++) {
            if(colors[i] == 0 && !validColor(graph, colors, i, 1)) return false;
        }
        
        return true;
    }
    
    private boolean validColor(int[][] graph, int[] colors, int node, int color) {
        if(colors[node] != 0) return colors[node] == color;
        colors[node] = color;
        for(int i = 0; i < graph[node].length; i++) {
            if(!validColor(graph, colors, graph[node][i], -color))
                return false;
        }
        return true;
    }
}

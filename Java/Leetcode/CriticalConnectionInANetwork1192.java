class Solution {
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (List<Integer> c : connections){
            map.computeIfAbsent(c.get(0), o -> new ArrayList<>()).add(c.get(1));
            map.computeIfAbsent(c.get(1), o -> new ArrayList<>()).add(c.get(0));
        }

        List<List<Integer>> ans = new ArrayList<>();
        int[] order = new int[n], low = new int[n];
        dfs(0, -1, 1, map, low, order, ans);
		//order[i] -> first time we start exploring this vertex i.
		//low[i] -> the earliest vertex that vertex i can reach.

        return ans;
    }

    private int dfs(int v, int p, int time, Map<Integer, List<Integer>> map,
            int[] low, int[] order, List<List<Integer>> ans){
        order[v] = low[v] = time;
        for (int next : map.get(v)){
            if (p == next) continue; //don't go back to parent otherwise it will mess up the order
            if (order[next] > 0) low[v] = Math.min(low[v], order[next]); //this edge is a back edge
            else{
                time = dfs(next, v, time + 1, map, low, order, ans);
                low[v] = Math.min(low[v], low[next]);
                if (low[next] > order[v]) ans.add(List.of(next, v));
				//bridge only occurs when low[child] is greater than itself.
            }
        }
        return time;
    }
}

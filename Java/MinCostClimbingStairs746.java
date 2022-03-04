class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] new_cost = new int[cost.length+1];
        new_cost[new_cost.length - 2] = cost[cost.length - 1];
        
        for(int i = new_cost.length - 3; i>=0; i--)
            new_cost[i] = Math.min(cost[i]+new_cost[i+1],cost[i]+new_cost[i+2]);
        
        
        return Math.min(new_cost[0], new_cost[1]);
        
    }
}

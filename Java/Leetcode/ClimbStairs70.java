class Solution {
    public int climbStairs(int n) {
         if(n < 0)
            return 0;
        
        if(n <= 1)
            return 1;
        
        int a = 1, b = 1, c = 0;
        
        for(int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        
        return c;
    }
}
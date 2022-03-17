class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int gPointer = 0;
        int sPointer = 0;
        while(gPointer < g.length && sPointer < s.length){
            if (g[gPointer] <= s[sPointer]){
                gPointer++;
                sPointer++;
            } else{
                sPointer++;
            }
        }
        return gPointer;
    }
}

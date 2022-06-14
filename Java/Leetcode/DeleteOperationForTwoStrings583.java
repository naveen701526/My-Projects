class Solution {
    public int minDistance(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
	    if (n == 0 || m == 0)
		    return 0;
        if (n < m){
            String t = word1;
            word1 = word2;
            word2 = t;
            n = word1.length();
            m = word2.length();
        }
        int[][] dp = new int[26][];
        int[] indices = new int[26];
        int[] w = new int[26];
        int maxP = 0;
        
	    for(int idx = 0; idx < n; idx++)
            w[word1.charAt(idx)-'a']++;
        
	    for(int idx = 0; idx < 26; idx++)
            dp[idx] = new int[w[idx]];

	    for(int idx = 0; idx < n; idx++){
            int i = word1.charAt(idx)-'a';
            dp[i][w[i]-++indices[i]] = idx;
        }
        
        for (int idx = 0; idx < m; idx++)
            maxP += indices[word2.charAt(idx)-'a'];
        
        int[] list = new int[maxP];
        for (int idx = 0, p = 0; idx < m; idx++){
            int i = word2.charAt(idx)-'a';
            if (indices[i] > 0) {
                System.arraycopy(dp[i],w[i]-indices[i],list,p,indices[i]);
                p += indices[i];
            }
        }

        int[] s = new int[maxP];
        int lcs = 0;
        for (int i = 0; i < maxP; i++) {
            int num = list[i];
            int j = Arrays.binarySearch(s, 0, lcs, num);
            if(j < 0)
                j = -j-1;
            if (j == lcs)
                s[lcs++] = num;
            else
                s[j] = num;
        }
	    return n+m-2*lcs;
    }
}

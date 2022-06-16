class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        int max = -1; String sol = "";
        boolean[][] t = new boolean[n][n];
        for(int i=0; i<n; i++){
            for(int j=i, k=0; j<n; j++, k++){
                if(i == 0) t[k][j] = true;
                else if(i == 1) t[k][j] = s.charAt(j) == s.charAt(k);
                else if(s.charAt(j) == s.charAt(k) && t[k+1][j-1]){
                    t[k][j] = true;
                }
                //get the longest substring from the the t[][]
                if(t[k][j]){
                    String temp = s.substring(k, j+1);
                    if(temp.length() > max){
                        max = temp.length();
                        sol = temp;
                    }
                }
            }
        }
        return sol;
    }
}

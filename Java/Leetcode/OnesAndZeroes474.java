class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] arr = new int[m+1][n+1];
        
        for(String str : strs){
            int c0 = 0;
            int c1 = 0;
            
            for(char c : str.toCharArray()){
                if(c == '0') c0++;
                else c1++;
            }
            
            for(int i=m;i>=c0;i--){
                for(int j=n;j>=c1;j--){
                    arr[i][j] = Math.max(arr[i][j],arr[i-c0][j-c1] + 1);
                }
            }
        }
        return arr[m][n];
    }
}

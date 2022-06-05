class Solution {
    int size;
    public int totalNQueens(int n) {
        size = n;
        boolean[] bool = new boolean[n];
        int[] rowArr = new int[n];
        int ans = 0;
        for(int i = 0; i < n; ++i){
            bool[i] = true;
            rowArr[i] = 0;
            ans += fill(1, bool, rowArr, n);
            bool[i] = false;
        }
        return ans;
    }
    private int fill(int row, boolean[] bool, int[] rowArr, int n){
        if(row == n){ 
                     return 1;
        }
        int ans = 0;
        for(int i = 0; i < n; ++i){
            if(bool[i])continue;
            if(noQueenDiag(i, row, rowArr, bool)){
                bool[i] = true;
                rowArr[i] = row;
                ans += fill(row + 1,  bool, rowArr, n);
                bool[i] = false;
                rowArr[i] = -1;
            }
        }
        return ans;
    }
    private boolean noQueenDiag(int col, int row, int[] rowArr, boolean[] bool){
        return noQueenDiagL(col, row, rowArr, bool) && noQueenDiagR(col, row, rowArr, bool);
    }
    private boolean noQueenDiagL(int col, int row, int[] rowArr, boolean[] bool){
        if(row == 0 || col == 0) return true;
        if(col > 0 && bool[col-1] && (rowArr[col -1] == row -1 )) return  false;
        return noQueenDiagL(col - 1, row-1, rowArr, bool);
    }
    private boolean noQueenDiagR(int col, int row, int[] rowArr, boolean[] bool){
        if(row == 0 || col == size -1) return true;
        if(col < size-1 && bool[col + 1] && (rowArr[col +1] == row -1 )) return false;
        return noQueenDiagR(col + 1, row-1, rowArr, bool);
    }
}

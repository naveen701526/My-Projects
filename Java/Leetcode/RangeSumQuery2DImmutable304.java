class NumMatrix {
  long[][] A;
  public NumMatrix(int[][] p) {
    int m= p.length, n= p[0].length;
    A= new long[m][n];
    
    //copy array to our array to find prefix
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++) A[i][j]= p[i][j];
    }
    
    //procedure for prefix in 2d array
    for(int i=1;i<m;i++){
        for(int j=0;j<n;j++) A[i][j]+= A[i-1][j];
    }
    
    for(int i=0;i<m;i++){
        for(int j=1;j<n;j++) A[i][j]+= A[i][j-1];
    }    
  }

  //O(1) Time
  public int sumRegion(int r1, int c1, int r2, int c2) {
      long top=  (r1-1)>=0?   A[r1-1][c2]  :  0;
      long left= (c1-1)>=0?   A[r2][c1-1]  :  0;
      long diag= (r1-1)>=0 && (c1-1)>=0?  A[r1-1][c1-1]  :  0;
      return (int)( A[r2][c2]- top - left + diag );
  }
}
/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */

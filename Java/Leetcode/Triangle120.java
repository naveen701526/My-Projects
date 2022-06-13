class Solution {
    public int minimumTotal(List<List<Integer>> t) {
        if(t.size()==1)
            return t.get(0).get(0);
        int k=t.size();
        int a[]=new int[k+1];
        for(int i=k-1;i>=0;i--)
        {
            int m=t.get(i).size();
            for(int j=0;j<m;j++)
            {
                a[j]=Math.min(a[j],a[j+1])+t.get(i).get(j);
            }
        }
        return a[0];
    }
}

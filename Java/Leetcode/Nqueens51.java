public class Solution {
public List<List<String>> solveNQueens(int n) {
    List<List<String>> list=new ArrayList<List<String>>();
    dfs(new int[n],0,n,list);
    return list;
}
public void dfs(int[] pos,int step,int n,List<List<String>> list) {
    if(step==n) {
        ArrayList<String> ls=printboard(pos,n);
        list.add(new ArrayList<String>(ls));
        return;
    }
    for(int i=0;i<n;i++) {
        pos[step]=i;
        if(isvalid(pos,step)) {
            dfs(pos,step+1,n,list);
        }
    }
}
public boolean isvalid(int[] pos, int step) {
    for(int i=0;i<step;i++) {
        if(pos[i]==pos[step]||(Math.abs(pos[i]-pos[step]))==(step-i)) return false;
        
    }
    return true;
}
public ArrayList<String> printboard(int[] pos,int n) {
    ArrayList<String> ls=new ArrayList<String>();
    for(int i=0;i<n;i++) {
        StringBuilder sb=new StringBuilder();
        for(int j=0;j<n-1;j++) sb.append('.');
        sb.insert(pos[i],'Q');
        ls.add(sb.toString());
        
    }
    return ls;
}
}

class Solution {
     int n;
    List<String> l = new ArrayList<String>();
    public List<String> generateParenthesis(int n) {
        this.n = n;
        findValidCombination(0,new StringBuffer(""));
        return l;
    }
    void findValidCombination(int noOfOpenParanthesis,StringBuffer sb){
        if(noOfOpenParanthesis<0||noOfOpenParanthesis>n)return;
        if(sb.length()==2*n){
            if(noOfOpenParanthesis==0)
                l.add(sb.toString());
            return;
        }
        
        findValidCombination(noOfOpenParanthesis-1,new StringBuffer(sb).append(')'));
        findValidCombination(noOfOpenParanthesis+1,new StringBuffer(sb).append('('));
    }
}

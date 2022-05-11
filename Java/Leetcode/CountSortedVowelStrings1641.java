class Solution {
    public int countVowelStrings(int n) {
        int a=1,e=1,i=1,o=1,u=1;
        for(int index=1;index<n;index++){
            int aNew=a,eNew=a+e,iNew=a+e+i,oNew=a+e+i+o,uNew=a+e+i+o+u;
            a=aNew;
            e=eNew;
            i=iNew;
            o=oNew;
            u=uNew;
        }
        return a+e+i+o+u;
    }
}

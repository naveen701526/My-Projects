class Solution {
    public boolean backspaceCompare(String s, String t) {
        StringBuilder sb1=new StringBuilder();
        StringBuilder sb2=new StringBuilder();
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)=='#'){
                if(sb1.length()==0){
                    continue;
                }
                else{
                    sb1.deleteCharAt(sb1.length()-1);
                }
            }
            else{
                sb1.append(s.charAt(i));
            }
        }
        for(int i=0; i<t.length(); i++){
            if(t.charAt(i)=='#'){
                if(sb2.length()==0){
                    continue;
                }
                else{
                    sb2.deleteCharAt(sb2.length()-1);
                }
            }
            else{
                sb2.append(t.charAt(i));
            }
        }
        return sb1.toString().equals(sb2.toString())?true:false;
    }
}

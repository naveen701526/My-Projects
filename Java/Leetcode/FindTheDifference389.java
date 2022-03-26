class Solution {
    public char findTheDifference(String s, String t) {
         int ans=0;
        // length of t = length of s + 1
        for(int i=0;i<s.length();i++){
            ans+=t.charAt(i);
            ans-=s.charAt(i);
        }
        // last element of String t 
        ans+=t.charAt(s.length());
        
        return (char) ans;
    }
}

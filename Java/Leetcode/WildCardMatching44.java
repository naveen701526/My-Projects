public class Solution {
    public boolean isMatch(String s, String p) {
        boolean[] prev = new boolean[s.length()+1];
        boolean[] curr = new boolean[s.length()+1];
        // base case: empty pattern matches empty string
        prev[0] = true;
        for(int i=1; i <= p.length(); i++){
            // base case: pattern with single character does not match an empty string
            if(p.charAt(i-1) == '*')
                curr[0] = prev[0];
            else
                curr[0] = false;
            for(int j=1; j <= s.length(); j++){
                // match zero, one or more times
                if(p.charAt(i-1) == '*'){
                    curr[j] = prev[j-1] || prev[j] || curr[j-1];
                }
                //current character matches 
                else if(p.charAt(i-1) == '?' || p.charAt(i-1) == s.charAt(j-1)){
                    curr[j] = prev[j-1];
                }
                //current character does not match
                else{
                    curr[j] = false;
                }
            }
            prev= Arrays.copyOf(curr,curr.length);
        }
        return prev[s.length()];
    }
}

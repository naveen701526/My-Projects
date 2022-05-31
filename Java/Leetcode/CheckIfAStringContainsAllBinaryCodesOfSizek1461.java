class Solution {
    public boolean hasAllCodes(String s, int k) {
        
        HashSet<String> set = new HashSet<>();
       for(int i = 0 ; i < s.length() - k +1; ++i){
            String sub = s.substring(i,i+k);
            set.add(sub);
        }
        return (set.size() == (int)Math.pow(2,k));
    }
}

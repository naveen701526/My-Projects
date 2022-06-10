class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int size = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int j = i;
            Set<Character> setOfChar = new HashSet<>();
            for (; j < s.length(); j++) {
                if (!setOfChar.add(s.charAt(j))){
                    break;
                }
            }
            
            if ((j-i) > size) {
                size = (j-i);
            }
        }
        
        return size;
    }
}

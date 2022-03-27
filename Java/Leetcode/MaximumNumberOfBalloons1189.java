class Solution {
    public int maxNumberOfBalloons(String text) {
          HashMap<Character, Integer> map = new HashMap<>();
        for(int i=0; i<text.length(); i++) {
            char ch = text.charAt(i);
            map.put(ch, map.getOrDefault(ch,0)+1);
        }
        String s = "balon";
        int mnf = Integer.MAX_VALUE; 
            if(map.getOrDefault('o', 0)==1) {
                    return 0; 
                }
            if(map.getOrDefault('l', 0)==1) {
                    return 0; 
                }
        for(int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            if(map.get(ch)==null) {
                return 0;
            }
            int m = map.get(ch);
            if(ch == 'l' || ch == 'o') {
                mnf = Math.min(mnf, m/2);
            } else {
                mnf = Math.min(mnf, m);
            }
        }
        return mnf;
    }
}

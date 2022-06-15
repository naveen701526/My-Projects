class Solution {
    public int longestStrChain(String[] words) {
        
        Arrays.sort(words, (a, b) -> {return a.length() - b.length();});
        Map<Integer, List<Integer>> map = new HashMap<>();
        int[] nums = new int[words.length];
        int res = 1;
        
        for(int i = 0; i < words.length; ++i){
            int len = words[i].length();
            nums[i] = 1;
            map.putIfAbsent(len, new ArrayList<Integer>());
            map.get(len).add(i);
            if(map.containsKey(len - 1)){
                List<Integer> arr = map.get(len - 1);
                for(int j : arr){
                    if(isValid(words[j], words[i])){
                        nums[i] = Math.max(nums[j] + 1, nums[i]);
                        res = Math.max(nums[i], res);
                    }
                }
            }
        }
        
        return res;
        
    }
    
    private boolean isValid(String s1, String s2){
        
        int i1 = 0, i2 = 0, count = 0;
        
        while(i1 < s1.length()){
            if(s1.charAt(i1) != s2.charAt(i2)){
                if(count == 1) return false;
                ++count;
                ++i2;
                continue;
            }
            ++i1;
            ++i2;
        }
        
        return true;
        
    }
}

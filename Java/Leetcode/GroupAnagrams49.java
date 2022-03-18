class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> resList = new ArrayList<>();
        Map<String, List<String>> ltrMap = new HashMap<>();
        
        for (int i = 0; i < strs.length; i++){
            String currWord = strs[i];
            char[] currStr = strs[i].toCharArray();
            String res = getSortedStr(currStr);
            
            if (!(ltrMap.containsKey(res))){
                List<String> valList = new ArrayList<>();
                valList.add(currWord);
                ltrMap.put(res, valList);
            }
            
            else{
                List<String> valList = ltrMap.get(res);
                valList.add(currWord);
                ltrMap.put(res, valList);
            }
        }
        
       
        for (String c: ltrMap.keySet()){
            resList.add(ltrMap.get(c));
        }
        
        return resList;
        
    }
    
    
    private String getSortedStr (char[] charStr){
        Arrays.sort(charStr);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < charStr.length; i++){
            sb.append(charStr[i]);
        }
        
        return sb.toString();
    }
}
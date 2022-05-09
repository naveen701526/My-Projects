class Solution {
    
    HashMap<Integer, String> map = new HashMap<>();
    List<String> list;
    
    public List<String> letterCombinations(String digits) {
        
        map.put(2, "abc"); map.put(3, "def"); map.put(4, "ghi");
        map.put(5, "jkl"); map.put(6, "mno"); map.put(7, "pqrs");
        map.put(8, "tuv"); map.put(9, "wxyz");
        list = new ArrayList<>();
        
        solution(digits, 0, digits.length(), "");
        
        return list;
        
    }
    
    public void solution(String str, int ind, int n, String temp) {
        
        if(ind == n) {
            if(!temp.equals(""))
                list.add(new String(temp));
            return;
        }
        for(char c : map.get(Integer.parseInt(str.charAt(ind) + ""))
           .toCharArray()) {
            solution(str, ind + 1, n, temp + c);
        }
        
    }
    
}

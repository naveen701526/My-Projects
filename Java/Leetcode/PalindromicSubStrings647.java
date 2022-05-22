class Solution {
    public int countSubstrings(String s) {
        int count=0;
        Boolean res=false;
        String temp="";
        for(int i=0;i<s.length();i++){
            for(int j=i+1;j<=s.length();j++){
                temp=s.substring(i,j);
                res=isPalindrome(temp);
                if(res==true)
                    count++;
            }
        }
        return count;
    }
     public static boolean isPalindrome(String str)
     {
        int i = 0, j = str.length() - 1;
        while (i < j) {
            if (str.charAt(i) != str.charAt(j))
                return false;
 
            i++;
            j--;
        }
        return true;
    }
}

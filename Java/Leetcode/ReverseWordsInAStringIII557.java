class Solution {
    public String reverseWords(String s) {
        char[] st = s.toCharArray();
        int N = st.length;
        int start = 0,end = 0 ; // two pointers for ilterating the whole char array 
        while(end < N){
            if(st[end] == ' ') { // when we found the space reverse the array from start to end 
                ReverseString(st,start,end-1);
                start = end+1;
            }
            end++;
        }
        ReverseString(st,start,end-1);
        return new String(st);
        
    }
    private static void ReverseString(char[] st,int start , int end){
            while(start < end){
                char temp = st[start];
                st[start] = st[end];
                st[end] = temp;
                start++; end--;
            }
    }
}

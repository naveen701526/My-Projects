class Solution {
    public int removePalindromeSub(String s) {
        StringBuilder sb = new StringBuilder();
        sb.append(s);
        sb.reverse();
        return sb.toString().equals(s) ? 1 : 2;
    }
}

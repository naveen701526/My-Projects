class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        Set < Integer > visited = new HashSet < > ();
        if (s1.length() + s2.length() != s3.length()) return false;
        return helper(s1, s2, 0, 0, s3, 0, visited);
    }

    public static boolean helper(String s1, String s2, int l1, int l2, String s3, int ptr, Set < Integer > visited) {
        if (visited.contains(l1 * s3.length() + l2)) return false;
        else visited.add(l1 * s3.length() + l2);
        if (ptr >= s3.length()) return true;
        else {
            boolean status = false;
            if (l1 < s1.length() && s1.charAt(l1) == s3.charAt(ptr)) status |= helper(s1, s2, l1 + 1, l2, s3, ptr + 1, visited);
            if (l2 < s2.length() && s2.charAt(l2) == s3.charAt(ptr)) status |= helper(s1, s2, l1, l2 + 1, s3, ptr + 1, visited);
            return status;
        }
    }
}
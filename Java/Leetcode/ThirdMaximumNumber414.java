class Solution {
     public int thirdMax(int[] nums) {
        Integer max1 = null;
        Integer max2 = null;
        Integer max3 = null;
         
        for (Integer no : nums) {

            if (no.equals(max1) || no.equals(max2) || no.equals(max3)) {
                continue;
            }
            if (max1 == null || max1 < no) {
                max3 = max2;
                max2 = max1;
                max1 = no;
            } else if (max2 == null || max2 < no) {
                max3 = max2;
                max2 = no;
            } else if (max3 == null || max3 < no) {
                max3 = no;
            }
        }
        return max3 == null ? max1 : max3;
    }
}

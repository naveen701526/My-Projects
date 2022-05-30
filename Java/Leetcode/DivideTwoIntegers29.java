class Solution {
       public static int divide(int dividend, int divisor) {
        if (Integer.MIN_VALUE == dividend && divisor == -1)
            return Integer.MAX_VALUE;
        int ans = 0;
        int a = Math.abs(dividend);
        int b = Math.abs(divisor);
        while (a - b >= 0) {
            int temp = b;
            int count = 1;
            while (a - (temp << 1) >= 0) {
                temp <<= 1;
                count <<= 1;
            }
            a -= temp;
            ans += count;
        }
        return (dividend > 0) == (divisor > 0) ? ans : -ans;
    }
}

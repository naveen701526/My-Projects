class Solution {
    public int mySqrt(int x) {
        if (x < 2)
            return x;
        int lo = 2, hi = x / 2, mid;
        while (lo <= hi) {
            mid = lo + (hi - lo) / 2;
            if ((long) mid * mid <= x) {
                lo = mid + 1;
            } else
                hi = mid - 1;
        }
        return hi;
    }
}
class Solution {
    public int reverse(int x) {
        int result = 0;

        while (x != 0) {
            int lastDigit = x % 10;
            x = x / 10;
            try {
                result = Math.addExact(Math.multiplyExact(result, 10), lastDigit);
            } catch (ArithmeticException e) {
                return 0;
            }
        }

        return result;
    }
}

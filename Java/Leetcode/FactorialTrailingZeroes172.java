public class FactorialTrailingZeroes172 {
    public int trailingZeroes(int n) {
       int sum = 0;
       int count = 1;
       while((n/Math.pow(5,count))>=1){
           sum = sum + n/(int)Math.pow(5,count);
           count = count+1;
       }
       return sum;
    }
}

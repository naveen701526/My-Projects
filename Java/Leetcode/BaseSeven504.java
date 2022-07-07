class Solution {
    public String convertToBase7(int num) {
      var result = String.valueOf("");
      var temp = Math.abs(num);
      
      if(temp == 0)
        return "0";
      
      while(temp > 0) {
        result += temp % 7;
        temp /= 7;
      }
      
      result = new StringBuilder(result).reverse().toString();
      
      return num < 0 ? "-" + result : result;
    }
}


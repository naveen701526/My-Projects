class Solution {
      public String fractionToDecimal(int numerator, int denominator) {
        boolean isNegative = (numerator < 0 && denominator > 0 || numerator > 0 && denominator < 0) ? true : false;
        long numeratorL = Math.abs((long) numerator);
        long denominatorL = Math.abs((long) denominator);
        Map<Long, Integer> previousRemains = new HashMap<Long, Integer>();
        StringBuilder sb = new StringBuilder();
        long quotian = numeratorL / denominatorL;
        sb.append(quotian);
        
        numeratorL %= denominatorL;
    
        if (numeratorL != 0) {
            sb.append(".");
        }
        
        int quotianIndex = 0;
        while (numeratorL != 0) {
            numeratorL *= 10;
            quotian = Math.abs(numeratorL / denominatorL);
            if (!previousRemains.containsKey(numeratorL)) {
                sb.append(quotian);
                previousRemains.put(numeratorL, quotianIndex++);
            } else {
                int firstIndex = 1 + previousRemains.get(numeratorL) + sb.indexOf(".");
                sb.insert(firstIndex, '(');
                sb.append(")");
                break;
            }
            numeratorL %= denominatorL;
        }
        
        if (isNegative) {
            sb.insert(0, "-");
        }
        return sb.toString();
    }
}

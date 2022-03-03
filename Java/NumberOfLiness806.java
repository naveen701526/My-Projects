class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int[] result = new int[2];
        int numberOfLines = 1;
        int width = 0;
        int char_width = 0;
        for(char letter : s.toCharArray() ){
            char_width = widths[letter - 'a'];
            if(char_width + width > 100){
                width = 0;
                numberOfLines++;
            }
            width += char_width;
        }
        result[0] = numberOfLines;
        result[1] = width;
        return result;
    }
}

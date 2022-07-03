class Solution {
    public int maxRepeating(String sequence, String word) {
      int count = -1;
      String s = "";
      do
      {
        count++;
        s += word;
      }while(sequence.contains(s));
      return count;
    }
}

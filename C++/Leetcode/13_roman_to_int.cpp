class Solution {
public:
    int findValue(char m) {
  if (m == 'I') return 1;
  else if (m == 'V') return 5;
  else if (m == 'X') return 10;
  else if (m == 'L') return 50;
  else if (m == 'C') return 100;
  else if (m == 'D') return 500;
  else if (m == 'M') return 1000;
  else return 0;
}  
    
int romanToInt(string s) {
  int sum = 0;
  for (int i = 0; i < s.size(); i++) {
    int check1 = 0, check2 = 0;
    check1 = findValue(s[i]);
    check2 = findValue(s[i+1]);

    if (check1 >= check2) {
      sum += check1;
    }
    else if (check1 < check2) {
      sum += (check2 - check1);
      i++;
    }
  }
  return sum;
}
};

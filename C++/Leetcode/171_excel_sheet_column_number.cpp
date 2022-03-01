class Solution {
public:
    int titleToNumber(string columnTitle) {
        int answer = 0;
	    int power = 1;
	    for (int i = columnTitle.length() - 1; i >= 0; i--)
	    {
		    answer += ((columnTitle[i] - 'A' + 1) * (power));
            if(i!=0) power = power * 26;
	    }
	    return answer;
    }
};

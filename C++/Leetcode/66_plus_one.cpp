class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 0, digit = 0;
        
        digits.back() += 1;
        for (int i = digits.size() - 1; i >= 0; i--) {
            int sum = carry + digits[i];
            carry = sum / 10;
            digits[i] = sum % 10;
        }
        
        if (carry)
            digits.insert(digits.begin(), carry);
        
        return digits;
    }
};

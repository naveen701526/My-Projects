class Solution {
public:
    bool isPalindrome(int number) {
        if (number < 0 || !number  && number%10  ) return false;
        long long int reverse_number = 0;
        long long int temp_number = number;
        while (temp_number){
            reverse_number = reverse_number*10 + temp_number%10;
            temp_number /= 10;
        }
        
        return reverse_number == number ? true:false;
        
      


    }
};

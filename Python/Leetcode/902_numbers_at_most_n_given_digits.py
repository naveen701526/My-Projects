class Solution:
    def less_digits_than_n (self, digits, n):
        cnt = 0
        for i in range (1, len(str(n))):
            cnt += len(digits)** i
        return cnt
    
    def same_digits_than_n (self, digits, n):
        s = str(n)
        cnt = 0 
        for i in range (len(s)):
            valid_digits_counter = 0
            for d in digits:
                if d < s[i]:
                    valid_digits_counter+=1
            cnt+= valid_digits_counter * (len(digits)**(len(s)-i-1))
            if s[i] not in digits:
                break
            cnt+=1 if i==len(s)-1 else 0
        return cnt
                    
            
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        return self.less_digits_than_n(digits, n) + self.same_digits_than_n(digits,n)

class Solution:
    def maxPower(self, s: str) -> int:
        power = [1] * len(s)
        
        curr_char = s[0]
        for i in range(1, len(s)):
            if curr_char == s[i]:
                power[i] = power[i - 1] + 1
            else:
                curr_char = s[i]
        
        return max(power)

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        prev1, prev2 = 1, 1
        for i in range(2, len(s) + 1):
            if not prev1 and not prev2:
                return 0
            k1 = 1 if s[i-1] != '0' else 0
            k2 = 1 if s[i-2] == '1' or s[i-2] == '2' and ord(s[i-1]) < ord('7') else 0
            prev1, prev2 = k1 * prev1 + k2 * prev2, prev1
        return prev1

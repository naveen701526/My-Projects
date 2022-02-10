class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s[1:] + s[:-1]).find(s) != -1

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for string in t:
            if i == len(s):
                break
            if string == s[i]:
                i += 1
        if i == len(s):
            return True
        else:
            return False


obj = Solution()
print(obj.isSubsequence(s="abc", t="ahbgdc"))

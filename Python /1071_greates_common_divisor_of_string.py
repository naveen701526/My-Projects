class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        # GCD(a,b) = GCD(b,a-b) = GCD(b, a%b)
        a, b = len(str1), len(str2)
        while b:
            a, b = b, a % b
                        
        return str1[:a]
        
opt = Solution()
print(opt.gcdOfStrings('ABCABC','ABC'))

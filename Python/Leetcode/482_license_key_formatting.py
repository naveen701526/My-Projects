class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace('-', '')[::-1]
        slots = math.ceil(len(s) / k)
        start = 0 
        end = k
        res = ''
        for i in range(1, slots+1):
            if i == slots:
                res += s[start:end]
            else:
                res += f'{s[start:end]}-'
                start = end
                end = start + k
        return res[::-1]

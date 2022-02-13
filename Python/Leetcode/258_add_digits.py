class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while not ( 0 <= res <= 9):
            digits = str(res)
            value = 0
            for i in digits:
                value += int(i)
            res = value
        return res

class Solution:
    def shiftingLetters(self, s, shifts):
        ln = len(shifts)
        s = list(s)
        shift = 0
        for i in reversed(range(ln)):
            shift = (shift+shifts[i]) % 26
            s[i] = chr(((ord(s[i])-ord('a')+shift) % 26)+ord('a'))
        return "".join(s)

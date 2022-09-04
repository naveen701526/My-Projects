class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        t_ord = ord(target) - ord('a')
        for i in letters:
            l_ord = ord(i) - ord('a')
            if l_ord > t_ord:
                return i
        return letters[0] # if no chrater is gte that target then return 0 index element

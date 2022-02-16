class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(left, right, changed):            
            while left < right:
                if s[left] != s[right]:
                    if not changed:
                        return isPalindrome(left + 1, right, True) or isPalindrome(left, right - 1, True)
                    else:
                        return False
                else:
                    left += 1
                    right -= 1
            return True

        return isPalindrome(0, len(s) - 1, False)

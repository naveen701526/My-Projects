#https://leetcode.com/problems/longest-palindrome/

def longestPalindrome(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
    length_of_palindrome = 0
    odd_present = False
        
    for char in char_count:
        if char_count[char] % 2 == 0:
            length_of_palindrome += char_count[char]
        else:
            length_of_palindrome += char_count[char] - 1
            odd_present = True
                
                
                
    if odd_present:
        length_of_palindrome += 1
            
    return length_of_palindrome
    
    
print(longestPalindrome("abccccdd"))
print(longestPalindrome("a"))
print(longestPalindrome("bb"))
print(longestPalindrome("ccc"))

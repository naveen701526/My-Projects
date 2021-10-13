# https://leetcode.com/problems/keyboard-row/
class Solution:
    def check_row(self, word, row):
        for char in word:
            if char in row:
                continue
            else:
                return False
        return True
    def findWords(self, words: [str]) -> [str]:
        row_1 = "qwertyuiopQWERTYUIOP"
        row_2 = "asdfghjklASDFGHJKL"
        row_3 = "zxcvbnmZXCVBNM"
        output = []
        for word in words:
            
            if word[0] in row_1: #check if first letter is in row_1
                val = self.check_row(word, row_1) #check if entire word is in row_1
                if val:
                    output.append(word) 
            elif word[0] in row_2: #check if first letter is in row_2
                
                val = self.check_row(word, row_2) #check if entire word is in row_2
                if val:
                    output.append(word)
            elif word[0] in row_3: #check if first letter is in row_3
                
                val = self.check_row(word, row_3) #check if entire word is in row_3
                if val:
                    output.append(word)
        return output #gives the words which either belong to row_1 or row_2 or row_3
        
opt = Solution()
print(opt.findWords(["qwertyuiopQWERTYUIOP"]))
print(opt.findWords(words = ["Hello","Alaska","Dad","Peace"]))

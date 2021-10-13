class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        string = '11'
        for i in range(3,n+1):
            temp = ''
            string = string + '&'
            c = 1
            for j in range(1,len(string)):
                if string[j] != string[j-1]:
                    temp = temp + str(c)
                    temp = temp + string[j - 1]
                    c = 1
                else:
                    c+=1
            string = temp
        return string
    
    
opt = Solution()
print(opt.countAndSay(4))

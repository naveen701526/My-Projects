class Solution:
    
    def ncr(self, n, r):
        nr,dr = 1, 1
        up,down = n, 1
        for i in range(1,r+1):
            nr *= up
            dr *= down
            up -= 1
            down += 1
        """
            7c5
            
            7*6*5*4*3
            ---------
            1*2*3*4*5
        """
        return nr//dr
    
    
    def uniquePaths(self, m: int, n: int) -> int:
        #linear time -> O(minimum(m, n)) space = O(1)
        return self.ncr(n+m-2, min(n-1, m-1))
        
        
opt = Solution()
print(opt.uniquePaths(m = 3, n = 7))

class Solution(object):
    def numTrees(self, n):
	
        if n <= 1:
            return 1
        
        output = 0
        
        #AA#>> For r<=n as root, we can put x<r in left and x>r in right subtrees
        for j in range(1+(n-1)//2):      
            output += 2*self.numTrees(j)*self.numTrees(n-1-j) 
        
        #AA#>> If n is even, middle case is double counted 
        if n%2:
            red = self.numTrees(n//2)
            output -= red*red
        
        return output
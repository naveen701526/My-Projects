class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        sieve = [0 for i in range(n)]
        ans = 0
        for i in range(2,n):
            if sieve[i]==0:
                ans+=1
                j = i
                k = 2
                while j<n:
                    sieve[j]=1
                    j=i*k
                    k+=1
        return ans
        
        
opt = Solution()
print(opt.countPrimes(10))

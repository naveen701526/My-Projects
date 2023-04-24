class Solution(object):
    def maxArea(self, h):
        l=0
        r=len(h)-1
        ar=0
        while(l<r):
            ar=max(ar,(r-l)*min(h[l], h[r]))
            if(h[l]<h[r]):
                l=l+1
            else:
                r=r-1
        return ar

op=Solution()
print(op.maxArea([1,8,6,2,5,4,8,3,7]))
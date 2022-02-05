class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[]
        value = 1
        
        for j in range(rowIndex+1):
            res.append(value)
            value=value * (rowIndex-j)//(j+1)
            
        return res

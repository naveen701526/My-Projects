class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            arr = [1] * (i+1)
            
            if i > 1:
                for j in range(1,len(arr)-1):
                    arr[j] = res[i-1][j-1] + res[i-1][j]
            
            res.append(arr)
            
        return res

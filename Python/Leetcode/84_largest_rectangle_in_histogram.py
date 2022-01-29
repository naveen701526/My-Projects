class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def bt_solver(arr):
            if len(arr)==0:
                return -1
            if len(arr)==1:
                return arr[0]
            if len(arr)==2:
                if min(arr):
                    return 2*min(arr)
                return max(arr)
            
            x = min(arr)
            cur_max = x*len(arr)
            prev = 0
            for i in range(len(arr)):
                if arr[i]==x:
                    cur_val = bt_solver(arr[prev:i])
                    if cur_val>cur_max:
                        cur_max = cur_val
                    prev = i+1
            
            cur_val = bt_solver(arr[prev:])
            if cur_val>cur_max:
                    cur_max = cur_val
                
            return cur_max
        
        return bt_solver(heights)

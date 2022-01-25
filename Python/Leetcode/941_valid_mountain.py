class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        increased = decreased = False
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                if decreased:
                    return False
                increased = True
            elif arr[i] < arr[i-1]:
                if not increased:
                    return False
                decreased = True
            else:
                return False
            
        return decreased

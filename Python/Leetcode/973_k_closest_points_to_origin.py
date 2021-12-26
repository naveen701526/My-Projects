class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def partition(points, l, r, pivot):
            pivot_sum = points[pivot][0]**2+points[pivot][1]**2
            points[pivot], points[r] = points[r], points[pivot]
            s = l
            for f in range(l, r):
                f_sum = points[f][0]**2+points[f][1]**2
                if f_sum < pivot_sum:
                    points[f], points[s] = points[s], points[f]
                    s += 1
            points[s], points[r] = points[r], points[s]
            return s
        
        def quickSelect(points, l, r):
            pivot = random.randint(l, r)
            mid = partition(points, l, r, pivot)
            if mid == k-1:
                return points[0:mid+1]
            elif mid > k-1:
                return quickSelect(points, l, mid-1)
            else:
                return quickSelect(points, mid+1, r)
            
        return quickSelect(points, 0, len(points)-1)

from collections import defaultdict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pick=defaultdict(int)
        drop=defaultdict(int)
        arr=set()
        for psngr,pck,drp in trips:
            pick[pck]+=psngr
            drop[drp]+=psngr
            arr.update((pck,drp))
        arr=sorted(arr)
        for k in arr:
            capacity-=pick[k]
            capacity+=drop[k]
            if capacity<0:
                return False
        return True

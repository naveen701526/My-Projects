class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        map1 = collections.Counter(nums)
        map2 = {}
        
        for i in nums:
            # print(map1)
            if map1[i] == 0:
                continue
            elif i in map2 and map2[i] > 0:
                map2[i] = map2[i] - 1
                map1[i] = map1[i] - 1
                map2[i+1] = map2.get(i+1,0) + 1
            elif map1[i] > 0 and map1[i+1] > 0 and map1[i+2] > 0:
                map1[i] = map1[i] - 1
                map1[i+1] = map1[i+1] - 1
                map1[i+2] = map1[i+2] - 1
                map2[i+3] = map2.get(i+3,0)+1
                # print("inside ",map1,map2)
            else:
                # print("false",map1,map2,i)
                return False
            # print("aft",map1,map2)
        return True

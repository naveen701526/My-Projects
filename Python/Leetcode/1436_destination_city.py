#https://leetcode.com/problems/destination-city/
class Solution:
    def destCity(self, paths):
        placecount = {}
        for path in paths:
            placecount[path[0]] = placecount.get(path[0], 0) + 1
            placecount[path[1]] = placecount.get(path[1], 0)
            
        for place in placecount:
            if placecount[place] == 0:
                return place
        
destination = Solution()
print(destination.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))

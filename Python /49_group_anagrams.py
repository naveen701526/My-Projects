class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            hashmap["".join(sorted(i))].append(i)
            
        arr = []
        for j in hashmap:
            arr.append(hashmap[j])
        
        return arr

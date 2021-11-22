class Solution:
    def numSpecialEquivGroups(self, words):
        hset = set()
        for i in range(len(words)):
            even = [0]*26
            odd = [0]*26
            for j in range(len(words[i])):
                if j % 2 == 0:
                    even[ord(words[i][j])-ord('a')] += 1
                else:
                    odd[ord(words[i][j])-ord('a')] += 1
            hset.add("".join([str(even[i]) for i in range(len(even))]) +
                     "".join([str(odd[i]) for i in range(len(odd))]))
        return len(hset)

class Solution:
    def wordSubsets(self, words1, words2):
        d = {}
        for i in words2:
            d2 = {}
            for j in i:
                if(j in d2.keys()):
                    d2[j] = d2[j]+1
                else:
                    d2[j] = 1
            for k in d2.keys():
                if(k in d.keys() and d2[k] > d[k]) or (k not in d.keys()):
                    d[k] = d2[k]
        l3 = []
        for i in words1:
            d2 = {}
            for j in i:
                if(j in d2.keys()):
                    d2[j] = d2[j]+1
                else:
                    d2[j] = 1
            f = 0
            for k in d.keys():
                if(k in d2.keys() and d2[k] < d[k]) or (k not in d2.keys()):
                    f = 1
                    break
            if(f == 0):
                l3.append(i)
        return l3

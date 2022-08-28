class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:        
        c=0
        l=len(s)
        if len(goal)!=l: # len of s and goal shall be same 
            return False
        set_s=set()
        set_g=set()
        for i in range(l):
            if s[i]!=goal[i]:
                set_s.add(goal[i])
                set_g.add(s[i])
                c+=1
        if (c>2) | (set_s!=set_g): # check for more than 2 mismatches
            return False
        if (c==0) & (l==len(set(s))):  # if there is no mismatch, check if there are repeated characters in s, repeated characters can be used for swapping
            return False
        return True

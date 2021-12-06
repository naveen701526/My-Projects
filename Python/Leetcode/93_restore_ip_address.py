class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        
        def helper(candidates,listy,recentInt,intsLeft):
            if len(candidates)==0:
                if intsLeft == 0:
                    ans.append(listy)
                return
            
            if int(recentInt+candidates[0])<=255 and intsLeft<len(candidates) and (recentInt == '' or str(int(recentInt+candidates[0]))==recentInt+candidates[0]):
                helper(candidates[1:],listy+candidates[0], recentInt+candidates[0],intsLeft)
                if intsLeft > 0 :
                    helper(candidates[1:],listy+candidates[0]+".",'',intsLeft-1)
        
        helper(s,'','',3)
        
        return ans

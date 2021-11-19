# Problem Statement ----> https://leetcode.com/problems/truncate-sentence/
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ansArray = s.split()
        return ' '.join(ansArray[:k])


obj = Solution()
print(obj.truncateSentence(s="Hello how are you Contestant", k=4))

# Problem Statement ---> https://leetcode.com/problems/count-items-matching-a-rule/
class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        ans = 0
        if ruleKey.lower() == 'color':
            for item in items:
                if item[1].lower() == ruleValue.lower():
                    ans += 1
        elif ruleKey.lower() == 'type':
            for item in items:
                if item[0].lower() == ruleValue.lower():
                    ans += 1
        elif ruleKey.lower() == 'name':
            for item in items:
                if item[2].lower() == ruleValue.lower():
                    ans += 1
        return ans

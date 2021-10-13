class Solution:
    def funcHelper(self, base, combinations):
        if len(base) == 1:
            combinations.add(base[0])
        for i in range(1, len(base), 2):
            sub = '('+''.join(base[i-1:i+2])+')'
            self.funcHelper(base[:i-1]+[sub]+base[i+2:], combinations)
        
    def diffWaysToCompute(self, input: str) -> [int]:
        operator_positions = [
            i for i,c in enumerate(input)
            if c in "*+-"]
        base = []
        prev = 0
        for p in operator_positions:
            base.append(input[prev:p])
            base.append(input[p])
            prev = p+1
        base.append(input[prev:])
        
        combinations = set()
        self.funcHelper(base, combinations)
        return [eval(c) for c in combinations]
        
        
opt = Solution()
print(opt.diffWaysToCompute("2-1-1"))

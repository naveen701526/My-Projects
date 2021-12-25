class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        lastOp = None
        curNum = 0
        for ch in s:
            if ch == ' ': continue
            if ch.isdigit():
                curNum = curNum * 10 + int(ch)
                continue
            if not lastOp or lastOp == '+':
                nums.append(curNum)
            elif lastOp == '-':
                nums.append(-curNum)
            elif lastOp == '*':
                nums.append(nums.pop() * curNum)
            elif lastOp == '/':
                nums.append(int(nums.pop() / curNum))
            curNum = 0
            lastOp = ch
            
        # Identical code performed on the last number we encounter
        if not lastOp or lastOp == '+':
            nums.append(curNum)
        elif lastOp == '-':
            nums.append(-curNum)
        elif lastOp == '*':
            nums.append(nums.pop() * curNum)
        elif lastOp == '/':
            nums.append(int(nums.pop() / curNum))
            
        return sum(nums)

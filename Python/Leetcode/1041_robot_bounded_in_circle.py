class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        while True:
            for do in instructions:
                if do == 'G':
                    x += directions[i][0]
                    y += directions[i][1]
                elif do == 'R':
                    i = (i + 1) % 4
                else:
                    i = (i - 1) % 4
                    
            if i == 0:
                if x == 0 and y == 0: return True
                return False

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        squares = []
        curSquare = 1
        for i in range(1, n + 1):
            if i == curSquare * curSquare:
                squares.append(i)
                curSquare += 1
                dp[i] = True
            else:
                for square in squares:
                    if not dp[i - square]:
                        dp[i] = True
                        break
        return dp[n]

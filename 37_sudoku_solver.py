class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board, 0, 0)
        return board
    
    def solve(self, board, x, y):
        if y == 9:
            x += 1
            y = 0

        if x == 9:
            return True
        
        if board[x][y] == '.':
            for ps in range(1, 10):
                ps = str(ps)
                if self.is_valid(board, x, y, ps):
                    board[x][y] = ps
                    flag = self.solve(board, x, y + 1)
                    if flag:
                        return flag
                    board[x][y] = '.'
        else:
            return self.solve(board, x, y + 1)

    def is_valid(self, board, x, y, ps):
        for i in range(0, 9):
            if board[x][i] == ps or board[i][y] == ps:
                return False
        
        xcor = x //3 * 3
        ycor = y //3 * 3
        for j in range(0, 3):
            for k in range(0, 3):
                if board[xcor + j][ycor + k] == ps:
                    return False
        
        return True

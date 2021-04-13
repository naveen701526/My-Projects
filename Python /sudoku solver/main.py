def find_next_empty(puzzle):
    pass


def solve_sudoku(puzzle):
    ''' solve sudoku using backtracking!
    the puzzle parameter will be a list of lists, 
    where each inner list is row of the sudoku puzzle
    return whether a solution exists.
    this mutates puzzle to be the solution(if the solution exists. '''

    # choose a block in puzzle to place the value
    row, col = find_next_empty(puzzle)

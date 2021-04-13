def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that 's not filled yet ---> rep with -1return row, col tuple
    # (or (none, none) if there is none)

    # we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # if no spaces in the puzzle are empty (-1)


def solve_sudoku(puzzle):
    ''' solve sudoku using backtracking!
    the puzzle parameter will be a list of lists, 
    where each inner list is row of the sudoku puzzle
    return whether a solution exists.
    this mutates puzzle to be the solution(if the solution exists. '''

    # choose a block in puzzle to place the value
    row, col = find_next_empty(puzzle)

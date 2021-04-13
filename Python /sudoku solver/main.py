def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that 's not filled yet ---> rep with -1return row, col tuple
    # (or (none, none) if there is none)

    # we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # if no spaces in the puzzle are empty (-1)


def is_valid(puzzle, guess, row, col):
    '''figures out whether the guess at the row/col of the puzzle is a valid guess returns true if is valid, false other wise'''

    # let's start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # now the column
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # and then the square
    # we need to get where the 3x3 square starts
    # and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3  # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    col_start = (col // 3) * 3

    # we are using 0-8 for our indices
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # if we get to this statement then the checks pass
    return True


def solve_sudoku(puzzle):
    ''' solve sudoku using backtracking!
    the puzzle parameter will be a list of lists, 
    where each inner list is row of the sudoku puzzle
    return whether a solution exists.
    this mutates puzzle to be the solution(if the solution exists. '''

    # choose a block in puzzle to place the value
    row, col = find_next_empty(puzzle)

    # if there's no where left, then we're done because we only allowed

    if row is None:
        return True

    # if there is a place to put a number, then make a guess between a number 1 to 9
    for guess in range(1, 10):  # range(1,10) is 1,2,3,...9
        # check if it is a valid guess
        if is_valid(puzzle, guess, row, col):
            # if this guess is valid then make it final
            # and add it in your final answer
            puzzle[row][col] = guess

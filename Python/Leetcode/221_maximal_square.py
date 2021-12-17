class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr = 0  # current length of the square at (i, j)
                flag = True  # indicates if there still exists a valid square
                while flag:
                    for k in range(curr+1):
                        # check outer border of elements for '1's.
                        """
                        eg curr = 2, ie a valid 2x2 square exists
                        'O' is valid, check 'X':
                        X X X
                        X O O
                        X O O
                        """
                        if i < curr or j < curr or \
                                matrix[i-curr][j-k] == '0' or \
                                matrix[i-k][j-curr] == '0':
                            flag = False
                            break
                    curr += flag
                if curr > result:  # new maximum length of square obtained
                    result = curr
        return result*result  # area = length x length

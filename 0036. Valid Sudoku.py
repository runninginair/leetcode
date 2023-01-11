''' 36. Valid Sudoku
Medium      6951      819      Add to List      Share

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:

Input: board = [["5","3",".", ".","7",".", ".",".","."],
                ["6",".",".", "1","9","5", ".",".","."],
                [".","9","8", ".",".",".", ".","6","."],
                ["8",".",".", ".","6",".", ".",".","3"],
                ["4",".",".", "8",".","3", ".",".","1"],
                ["7",".",".", ".","2",".", ".",".","6"],
                [".","6",".", ".",".",".", "2","8","."],
                [".",".",".", "4","1","9", ".",".","5"],
                [".",".",".", ".","8",".", ".","7","9"]]
Output: true
Example 2:

Input: board = [["8","3",".", ".","7",".", ".",".","."],
                ["6",".",".", "1","9","5", ".",".","."],
                [".","9","8", ".",".",".", ".","6","."],
                ["8",".",".", ".","6",".", ".",".","3"],
                ["4",".",".", "8",".","3", ".",".","1"],
                ["7",".",".", ".","2",".", ".",".","6"],
                [".","6",".", ".",".",".", "2","8","."],
                [".",".",".", "4","1","9", ".",".","5"],
                [".",".",".", ".","8",".", ".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:        board.length == 9
                    board[i].length == 9
                    board[i][j] is a digit 1-9 or '.'.
Accepted:       927,869
Submissions:    1,628,251
'''

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        def isValid_1to9(block: List) -> bool:
            memo = [n for n in range(10)]
            for cha in block:
                if cha != '.':
                    num = int(cha)
                    if memo[num] != 0: memo[num] = 0
                    else: return False
            return True
        ### check 3 X 3 box:
        for m in [0, 3, 6]:
            for k in [0, 3, 6]:
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[i + m][j + k])
                if not isValid_1to9(box): return False
        ### check each row:
        for i in range(9):
            if not isValid_1to9(board[i]): return False
            
        ### check each column:
        for i in range(9):
            column = [board[j][i] for j in range(9)]
            if not isValid_1to9(column): return False

        return True

class Solution_v0:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValidSudoku(self, board) -> bool:        

        def verifyRow():
            for r in range(9):
                memo = [0 for _ in range(10)]
                for ch in board[r]:
                    if ch == '.': continue
                    else:
                        d = int(ch)
                        if memo[d] == 1: return False
                        else: memo[d] = 1
            return True

        def verifyCol():
            for i in range(9):
                memo = [0 for _ in range(10)]
                for c in range(9):
                    if board[c][i] == '.': continue
                    else:
                        d = int(board[c][i])
                        if memo[d] == 1: return False
                        else: memo[d] = 1
            return True

        def verifyBox():
            for p in [0, 3, 6]:
                for q in [0, 3, 6]:
                    memo = [0 for _ in range(10)]
                    for i in range(3):
                        for j in range(3):
                            if board[i+p][j+q] == '.': continue
                            else:
                                d = int(board[i+p][j+q])
                                if memo[d] == 1: return False
                                else: memo[d] = 1
            return True

        return verifyRow() and verifyCol() and verifyBox()


def main():
    sol = Solution()
    sol = Solution_v0()

    board = [["5","3",".", ".","7",".", ".",".","."],
             ["6",".",".", "1","9","5", ".",".","."],
             [".","9","8", ".",".",".", ".","6","."],
             ["8",".",".", ".","6",".", ".",".","3"],
             ["4",".",".", "8",".","3", ".",".","1"],
             ["7",".",".", ".","2",".", ".",".","6"],
             [".","6",".", ".",".",".", "2","8","."],
             [".",".",".", "4","1","9", ".",".","5"],
             [".",".",".", ".","8",".", ".","7","9"]]   ### Output: True    
    print(sol.isValidSudoku(board))

    board = [[".",".","4", ".",".",".", "6","3","."],
             [".",".",".", ".",".",".", ".",".","."],
             ["5",".",".", ".",".",".", ".","9","."],
             [".",".",".", "5","6",".", ".",".","."],
             ["4",".","3", ".",".",".", ".",".","1"],
             [".",".",".", "7",".",".", ".",".","."],
             [".",".",".", "5",".",".", ".",".","."],
             [".",".",".", ".",".",".", ".",".","."],
             [".",".",".", ".",".",".", ".",".","."]]   ### Output: False
    print(sol.isValidSudoku(board))

    board = [["8","3",".", ".","7",".", ".",".","."],
             ["6",".",".", "1","9","5", ".",".","."],
             [".","9","8", ".",".",".", ".","6","."],
             ["8",".",".", ".","6",".", ".",".","3"],
             ["4",".",".", "8",".","3", ".",".","1"],
             ["7",".",".", ".","2",".", ".",".","6"],
             [".","6",".", ".",".",".", "2","8","."],
             [".",".",".", "4","1","9", ".",".","5"],
             [".",".",".", ".","8",".", ".","7","9"]]   ### Output: False
    print(sol.isValidSudoku(board))

main()

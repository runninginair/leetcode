''' 37. Sudoku Solver
Hard    7K    188     Companies

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.


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
       Output: [["5","3","4","6","7","8","9","1","2"],
                ["6","7","2","1","9","5","3","4","8"],
                ["1","9","8","3","4","2","5","6","7"],
                ["8","5","9","7","6","1","4","2","3"],
                ["4","2","6","8","5","3","7","9","1"],
                ["7","1","3","9","2","4","8","5","6"],
                ["9","6","1","5","3","7","2","8","4"],
                ["2","8","7","4","1","9","6","3","5"],
                ["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


Constraints:    board.length == 9
                board[i].length == 9
                board[i][j] is a digit or '.'.
                It is guaranteed that the input board has only one solution.
Accepted:       422.1K
Submissions:    740.7K
Acceptance Rate:57.0%
'''

from typing import List


class Solution:     ### Some Test NOT passed.
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.counter, map = 0, {}
        def generateMap(x: int, y: int) -> None:
            maybe = set([n for n in range(1, 10)])
            for i in range(9):  # Check rows
                if i == x: continue
                if board[i][y] != "." and int(board[i][y]) in maybe:
                    maybe.remove(int(board[i][y]))
                    if len(maybe) == 1:
                        board[x][y] = str(maybe.pop())
                        self.counter -= 1
                        return

            for j in range(9):  # Check culums
                if j == y: continue
                if board[x][j] != "." and int(board[x][j]) in maybe:
                    maybe.remove(int(board[x][j]))
                    if len(maybe) == 1:
                        board[x][y] = str(maybe.pop())
                        self.counter -= 1
                        return

            for i in range(x // 3 * 3, (x // 3 + 1) * 3):   ### Check box
                for j in range(y // 3 * 3, (y // 3 + 1) * 3):
                    if i == x and j == y: continue
                    if board[i][j] != "." and int(board[i][j]) in maybe:
                        maybe.remove(int(board[i][j]))
                        if len(maybe) == 1:
                            board[x][y] = str(maybe.pop())
                            self.counter -= 1
                            return                        

            map.update({(x + 1) * 10 + (y + 1): maybe})
            # print("MapUpdated:", x, y, ":", map[(x + 1) * 10 + (y + 1)])

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": self.counter += 1

        # while self.counter > 0:
        if  self.counter > 0:

            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".": generateMap(i, j)

        # print(self.counter)
        for k in map: print(k, map[k])

        return



def main():
    sol = Solution()

    # board = [["5","3",".", ".","7",".", ".",".","."],
    #          ["6",".",".", "1","9","5", ".",".","."],
    #          [".","9","8", ".",".",".", ".","6","."],
    #          ["8",".",".", ".","6",".", ".",".","3"],
    #          ["4",".",".", "8",".","3", ".",".","1"],
    #          ["7",".",".", ".","2",".", ".",".","6"],
    #          [".","6",".", ".",".",".", "2","8","."],
    #          [".",".",".", "4","1","9", ".",".","5"],
    #          [".",".",".", ".","8",".", ".","7","9"]]
    # sol.solveSudoku(board)
    # print("-----------------------------")
    # for eachLine in board: print(eachLine)

    board = [[".",".","9", "7","4","8", ".",".","."],
             ["7",".",".", ".",".",".", ".",".","."],
             [".","2",".", "1",".","9", ".",".","."],
             [".",".","7", ".",".",".", "2","4","."],
             [".","6","4", ".","1",".", "5","9","."],
             [".","9","8", ".",".",".", "3",".","."],
             [".",".",".", "8",".","3", ".","2","."],
             [".",".",".", ".",".",".", ".",".","6"],
             [".",".",".", "2","7","5", "9",".","."]]
    sol.solveSudoku(board)
    print("-----------------------------")
    for eachLine in board: print(eachLine)             

main()

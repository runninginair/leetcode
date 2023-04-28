''' 6322. Check Knight Tour Configuration
    2596. Check Knight Tour Configuration

Medium      14      3       Companies

There is a knight on an n x n chessboard. In a valid configuration, the knight
starts at the top-left cell of the board and visits every cell on the board
exactly once.

You are given an n x n integer matrix grid consisting of distinct integers from
the range [0, n * n - 1] where grid[row][col] indicates that the cell (row, col)
is the grid[row][col]-th cell that the knight visited. The moves are 0-indexed.

Return true if grid represents a valid configuration of the knight's movements
or false otherwise.

Note that a valid knight move consists of moving two squares vertically and one
square horizontally, or two squares horizontally and one square vertically.

The figure below illustrates all the possible eight moves of a knight from some
cell.


Example 1:
Input: grid = [[0,  11, 16,  5, 20],
               [17,  4, 19, 10, 15],
               [12,  1,  8, 21,  6],
               [ 3, 18, 23, 14,  9],
               [24, 13,  2,  7, 22]]
Output: true
Explanation: The above diagram represents the grid. It can be shown that it is
             a valid configuration.

Example 2:
Input: grid = [[0, 3, 6],
               [5, 8, 1],
               [2, 7, 4]]
Output: false
Explanation: The above diagram represents the grid. The 8th move of the knight
             is not valid considering its position after the 7th move.
 

Constraints:        n == grid.length == grid[i].length
                    3 <= n <= 7
                    0 <= grid[row][col] < n * n
                    All integers in grid are unique.
Accepted:           8.2K
Submissions:        13.7K
Acceptance Rate:    59.9%
'''

from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0: return False
        def isValid(start, end) -> bool:
            [x1, y1], [x2, y2] = start, end
            if abs(x1 - x2) == 1 and abs(y1 - y2) == 2: return True
            if abs(x1 - x2) == 2 and abs(y1 - y2) == 1: return True
            return False

        n = len(grid)
        que = []
        for i in range(n):
            for j in range(n):
                que.append([grid[i][j], [i, j]])
        que.sort()
        # print(que)
        for i in range(1, len(que)):
            if not isValid(que[i][1], que[i - 1][1]): return False

        return True

def main():
    sol = Solution()

    grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
    # Output: true
    print(sol.checkValidGrid(grid))

    grid = [[0,3,6],[5,8,1],[2,7,4]]
    # Output: false
    print(sol.checkValidGrid(grid))

    grid = [[24, 11, 22, 17,  4],
            [21, 16,  5, 12,  9],
            [ 6, 23, 10,  3, 18],
            [15, 20,  1,  8, 13],
            [ 0,  7, 14, 19,  2]]
    # Output: false
    print(sol.checkValidGrid(grid))

main()

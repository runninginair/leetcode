''' 130. Surrounded Regions
Medium      5802       1350     Add to List     Share
Given an m x n matrix board containing 'X' and 'O', capture all regions that
are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.


Example 1:

Input: board = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]]

Output: [["X","X","X","X"],
         ["X","X","X","X"],
         ["X","X","X","X"],
         ["X","O","X","X"]]

Explanation: Notice that an 'O' should not be flipped if:
    - It is on the border, or
    - It is adjacent to an 'O' that should not be flipped.
    The bottom 'O' is on the border, so it is not flipped.
    The other three 'O' form a surrounded region, so they are flipped.

Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:    m == board.length
                n == board[i].length
                1 <= m, n <= 200
                board[i][j] is 'X' or 'O'.
Accepted:       468,715
Submissions:    1,315,418
'''

class Solution:
    # def solve(self, board: List[List[str]]) -> None:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        if m < 3 or n < 3:
            return board

        memo = [[False for _ in range(n)] for _ in range(m)]
                 
        def dfs(x: int, y: int):
            stack = []
            stack.append([x, y])
            while stack:
                t = stack.pop(-1)
                if t[0] > 0 and board[t[0] - 1][t[1]] == 'O' and not memo[t[0]-1][t[1]]:
                    stack.append([t[0]-1, t[1]])
                    memo[t[0]-1][t[1]] = True
                if t[0] < m - 1 and board[t[0] + 1][t[1]] == 'O' and not memo[t[0] + 1][t[1]]:
                    stack.append([t[0]+1, t[1]])
                    memo[t[0]+1][t[1]] = True                  
                if t[1] > 0 and board[t[0]][t[1] - 1] == 'O' and not memo[t[0]][t[1]-1]:
                    stack.append([t[0], t[1]-1])
                    memo[t[0]][t[1]-1] = True
                if t[1] < n - 1 and board[t[0]][t[1]+1] == 'O' and not memo[t[0]][t[1]+1]:
                    stack.append([t[0], t[1]+1])
                    memo[t[0]][t[1]+1] = True

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 and i or j == n - 1:
                    if board[i][j] == 'O':
                        dfs(i, j)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if memo[i][j]:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

        print("memo:", memo)

def main():
    sol = Solution()
    # board = [["X","X","X","X"],
    #          ["X","O","O","X"],
    #          ["X","X","O","X"],
    #          ["X","O","X","X"]]
    # sol.solve(board)
    # print(board)

    board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
    sol.solve(board)
    print(board)

main()

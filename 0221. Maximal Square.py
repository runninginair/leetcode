''' 221. Maximal Square
Medium      8135    176     Add to List     Share
Given an m x n binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.


Example 1:
Input: matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]     Output: 4

Example 2:
Input: matrix = [["0","1"],
                 ["1","0"]]                 Output: 1

Example 3:
Input: matrix = [["0"]]                     Output: 0
 

Constraints:    m == matrix.length
                n == matrix[i].length
                1 <= m, n <= 300
                matrix[i][j] is '0' or '1'.
Accepted:       542,694
Submissions:    1,221,182
'''

class Solution:
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    def maximalSquare(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        def bfs(x, y): ## Search Direction to right and down.
            length = 1
            for i in range(1, min(m-x, n-y)):
                if x < m - i + 1 and y < n - i + 1 and matrix[x + i][y + i] == '1':
                    for j in range(i):
                        if matrix[x + i][y + j] == '0' or matrix[x + j][y + i] == '0': 
                            return length
                else:
                    return length
                length += 1
            return length

        maxLength = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    maxLength = max(maxLength, 1)   
                    maxLength = max(maxLength, bfs(i, j))

        return pow(maxLength, 2)


class Solution_dp:
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    def maximalSquare(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        maxLength = 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                    maxLength = max(maxLength, dp[i+1][j+1])
        return maxLength * maxLength


def main():
    sol = Solution()
    sol = Solution_dp()

    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]     # Output: 4
    print(sol.maximalSquare(matrix))

    matrix = [["1","1","1","1","0"],
              ["1","1","1","1","0"],
              ["1","1","1","1","1"],
              ["1","1","1","1","1"],
              ["0","0","1","1","1"]]
    print(sol.maximalSquare(matrix))

main()


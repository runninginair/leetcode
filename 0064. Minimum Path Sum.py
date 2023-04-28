''' 64. Minimum Path Sum

Medium      9.8K       126         Companies

Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


Example 1:      1   |   3   |   1
            ------------------------
                1   |   5   |   1
            ------------------------
                4   |   2   |   2
                
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:        m == grid.length
                    n == grid[i].length
                    1 <= m, n <= 200
                    0 <= grid[i][j] <= 100
Accepted:           868.9K
Submissions:        1.4M
Acceptance Rate:    61.2%
'''

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 or n == 1: return sum([sum(grid[i]) for i in range(m)])
        for i in range(1, n): grid[0][i] += grid[0][i - 1]
        for i in range(1, m): grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]) 
        return grid[m - 1][n - 1]

class Solution_v2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, n): grid[0][i] += grid[0][i - 1]
        for i in range(1, m): grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]) 
        return grid[m - 1][n - 1]


def main():
    sol = Solution()

    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(sol.minPathSum(grid))     # Output: 7

    grid = [[1,2,3],[4,5,6]]
    print(sol.minPathSum(grid))     # Output: 12

    grid = [[1,2,3,4,5,6]]
    print(sol.minPathSum(grid))     # Output: 21

    grid = [[1],[2],[3],[4],[5],[6]]
    print(sol.minPathSum(grid))     # Output: 21


if __name__ == "__main__":
    main()

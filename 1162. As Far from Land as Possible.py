''' 1162. As Far from Land as Possible

Medium      2.5K      72        Companies

Given an n x n grid containing only values 0 and 1, where 0 represents water
and 1 represents land, find a water cell such that its distance to the nearest
land cell is maximized, and return the distance.
If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance:
the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.


Example 1:

Input: grid = [[1, 0, 1],
               [0, 0, 0],
               [1, 0, 1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:
Input: grid = [[1, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 

Constraints:        n == grid.length
                    n == grid[i].length
                    1 <= n <= 100
                    grid[i][j] is 0 or 1
Accepted:           85K
Submissions:        174.8K
Acceptance Rate:    48.6%

'''

import math
from typing import List


class Solution:     ### My DP solution  T: O(N^ 2)  M: O(N^2)  N=len(grid)
    def maxDistance(self, grid: List[List[int]]) -> int:
        cnt0, cnt1, N = 0, 0, len(grid)
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1: cnt1 += 1
                if grid[i][j] == 0: cnt0 += 1
        if cnt0 == 0 or cnt1 == 0: return -1        

        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp[0][0] = 0 if grid[0][0] == 1 else math.inf

        for i in range(1, N):
            dp[i][0] = 0 if grid[i][0] == 1 else dp[i - 1][0] + 1
            dp[0][i] = 0 if grid[0][i] == 1 else dp[0][i - 1] + 1
        for i in range(1, N):
            for j in range(1, N):
                dp[i][j] = 0 if grid[i][j] == 1 else min(dp[i - 1][j], dp[i][j - 1]) + 1

        res = dp[N - 1][N - 1]
        for i in range(N-2, -1, -1):
            if dp[i][N - 1] != 0:
                dp[i][N - 1] = min(dp[i][N - 1], dp[i + 1][N - 1] + 1)
                res = max(res, dp[i][N - 1])
            if dp[N - 1][i] != 0:
                dp[N - 1][i] = min(dp[N - 1][i], dp[N - 1][i + 1] + 1)
                res = max(res, dp[N - 1][i])
        for i in range(N - 2, -1, -1):
            for j in range(N - 2, -1, -1):
                dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1, dp[i][j + 1] + 1)
                res = max(res, dp[i][j])
        return res

def main():
    sol = Solution()

    grid = [[1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]]
    print(sol.maxDistance(grid))    ### Expect output: 2
    
    grid = [[1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    print(sol.maxDistance(grid))    ### Expect output: 4

    grid = [[0, 0, 1, 1, 1],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 1]]    
    print(sol.maxDistance(grid))    ### Expect output: 2


if __name__ == "__main__":
    main()

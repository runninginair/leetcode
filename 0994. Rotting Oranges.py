''' 994. Rotting Oranges

Medium      9.9K      335       Companies

You are given an m x n grid where each cell can have one of three values:

 * 0 representing an empty cell,
 * 1 representing a fresh orange, or
 * 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a
fresh orange. If this is impossible, return -1.


Example 1:

    [[2,1,1],       [[2,2,1],      [[2,2,2],       [[2,2,2],       [[2,2,2],
     [1,1,0],   =>   [2,1,0],  =>   [2,2,0],  =>    [2,2,0],  =>    [2,2,0],     
     [0,1,1]]        [0,1,1]]       [0,1,1]]        [0,2,1]]        [0,2,2]]

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4


Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten,
because rotting only happens 4-directionally.


Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:        m == grid.length
                    n == grid[i].length
                    1 <= m, n <= 10
                    grid[i][j] is 0, 1, or 2.
Accepted:           574.7K
Submissions:        1.1M
Acceptance Rate:    52.9%
'''

from typing import List


class Solution:       # T: O(m * n)     M: O(m * n)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        freshCnt, rottenQue = 0, []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: freshCnt += 1
                elif grid[r][c] == 2: rottenQue.append([r, c])
        if freshCnt == 0: return 0
        if not rottenQue: return -1

        sec = 0
        while rottenQue:
            next = []
            while rottenQue:
                next.append(rottenQue.pop())
            for x, y in next:
                for i, j in [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]:
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        rottenQue.append([i, j])
                        freshCnt -= 1
            sec += 1
            if freshCnt == 0: return sec
        return -1


def main():
    sol = Solution()

    grid = [[2,1,1],[1,1,0],[0,1,1]]    # Output: 4
    print(sol.orangesRotting(grid))

    grid = [[2,1,1],[0,1,1],[1,0,1]]    # Output: -1
    print(sol.orangesRotting(grid))

    grid = [[0,2]]                      # Output: 0
    print(sol.orangesRotting(grid))

if __name__ == "__main__":
    main()

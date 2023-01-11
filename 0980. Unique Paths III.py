''' 980. Unique Paths III

Hard    3.5K    149     Companies

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending
square, that walk over every non-obstacle square exactly once.


Example 1:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:
Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Constraints:        m == grid.length
                    n == grid[i].length
                    1 <= m, n <= 20
                    1 <= m * n <= 20
                    -1 <= grid[i][j] <= 2
                    There is exactly one starting cell and one ending cell.
Accepted:           132.6K
Submissions:        166.3K
Acceptance Rate:    79.7%
'''

from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ### First round scan to find start(== 1), termi(== 2), path(== 0)
        m, n, self.ans = len(grid), len(grid[0]), 0
        start, termi, path = [-1, -1], [-1, -1], 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: path += 1
                elif grid[i][j] == 1: start[0], start[1] = i, j
                elif grid[i][j] == 2: termi[0], termi[1] = i, j

        ### DFS brute force to find the ans
        def dfs(curr: List[int], trace: List[List[int]]) -> None:
            if curr == termi:          
                if len(trace) == path: self.ans += 1
                return
            trace.append(curr)
            for offx, offy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                x, y = curr[0] + offx, curr[1] + offy
                if (0 <= x < m and 0 <= y < n and (grid[x][y] == 0 or grid[x][y] == 2) 
                    and [x, y] not in trace): dfs([x, y], trace)
            trace.remove(curr)

        dfs(start, [])

        return self.ans

class Solution_v2:      ### LeetCode ID: warrenruud
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = range(len(grid)), range(len(grid[0]))

        zeros = sum(row.count(0) for row in grid)       # count the zeros to ensure all cells visited
        start = tuple((r,c) for r in M for c in N       # find start in grid
                           if grid[r][c] == 1)[0]
        self.ans = 0

        def dfs(row, col, zeros):
            grid[row][col] = 3                          # change 0 to 3 to avoid returning

            for dr, dc in ((-1,0),(0,-1),(1,0),(0,1)):  # explore the grid recursively
                R, C = row+dr, col+dc
                if R in M and C in N:
                    if grid[R][C] == 0: dfs(R, C, zeros - 1)
                    if grid[R][C] == 2 and zeros == 0: self.ans += 1

            grid[row][col] = 0                          # change back
            return

        dfs(*start, zeros)
        return self.ans


def main():
    sol = Solution()
    sol = Solution_v2()

    grid = [[1, 0, 0, 0], 
            [0, 0, 0, 0],
            [0, 0, 2, -1]]     # Output: 2
    print(sol.uniquePathsIII(grid))

    grid = [[1, 0, 0],
            [0, 0, 2]]     # Output: 1
    print(sol.uniquePathsIII(grid))

    grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]  # Output: 4
    print(sol.uniquePathsIII(grid))

    grid = [[0,1],[2,0]]    # Output: 0
    print(sol.uniquePathsIII(grid))


if __name__ == "__main__":
    main()

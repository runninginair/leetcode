''' 0934. Shortest Bridge

Medium      4.2K       165         Companies

You are given an n x n binary matrix grid where 1 represents land and 0
represents water.

An island is a 4-directionally connected group of 1's not connected to any
other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.


Example 1:
Input: grid = [[0, 1],
               [1, 0]]
Output: 1

Example 2:
Input: grid = [[0, 1, 0],
               [0, 0, 0],
               [0, 0, 1]]
Output: 2

Example 3:
Input: grid = [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 0, 1, 0, 1],
               [1, 0, 0, 0, 1],
               [1, 1, 1, 1, 1]]
Output: 1
 
Constraints:        n == grid.length == grid[i].length
                    2 <= n <= 100
                    grid[i][j] is either 0 or 1.
                    There are exactly two islands in grid.
Accepted:           145.1K
Submissions:        259.2K
Acceptance Rate:    56.0%
'''

from typing import List
import heapq, math

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Mark Land1's cells as -1 
        def markLand1(u: int, v: int) -> None:
            grid[u][v], q = -1, [[u, v]]
            while q:
                i, j = q.pop()
                for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = -1
                        q.append([x, y])

        def bfs(u: int, v: int) -> int:
            q, grid[u][v] = [[0, u, v]], 2
            while q:
                d, i, j = heapq.heappop(q)
                for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1:
                            heapq.heappush(q, [d, x, y])
                            grid[x][y] = 2
                        elif grid[x][y] == 0:
                            heapq.heappush(q, [d + 1, x, y])
                            grid[x][y] = 2
                        elif grid[x][y] == -1:
                            return d

        land1NotFound = True
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if land1NotFound:
                        markLand1(i, j)
                        land1NotFound = False
                    else:
                        return bfs(i, j)
                    
        ### Safe guard in case there are not two islands
        return -1
    

def main():
    sol = Solution()

    grid = [[0, 1],
            [1, 0]]                         # Output: 1
    print(sol.shortestBridge(grid))

    grid = [[0, 1, 0],
            [0, 0, 0],
            [0, 0, 1]]                      # Output: 2
    print(sol.shortestBridge(grid))

    grid = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]                # Output: 1
    print(sol.shortestBridge(grid))

    grid = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 1]]          # Output: 2
    print(sol.shortestBridge(grid))


if __name__ == "__main__":
    main()
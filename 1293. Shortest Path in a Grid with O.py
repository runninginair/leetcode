''' 1293. Shortest Path in a Grid with Obstacles Elimination
Hard        3060        54      Add to List     Share
You are given an m x n integer matrix grid where each cell is either 0 (empty)
or 1 (obstacle). You can move up, down, left, or right from and to an empty
cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to
the lower right corner (m - 1, n - 1) given that you can eliminate at most k
obstacles. If it is not possible to find such walk return -1.


Example 1:
Input: grid = [[0,0,0],
               [1,1,0],
               [0,0,0],
               [0,1,1],
               [0,0,0]], k = 1      Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6.
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2:
Input: grid = [[0,1,1],
               [1,1,1],
               [1,0,0]], k = 1      Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
 

Constraints:    m == grid.length
                n == grid[i].length
                1 <= m, n <= 40
                1 <= k <= m * n
                grid[i][j] is either 0 or 1.
                grid[0][0] == grid[m - 1][n - 1] == 0
Accepted:       136,929
Submissions:    310,426

'''

class Solution:     # Brute farce (Backtrack)
    def shortestPath(self, grid, k: int) -> int:
        m, n = len(grid), len(grid[0])
        best = m + n - 2
        self.min_steps = float('inf')
        grid[0][0] = -1
        
        def backtrack(x, y, k, cur):
            if k < 0:
                return
            elif x == m - 1 and y == n - 1:
                self.min_steps = min(self.min_steps, cur)
                if self.min_steps == best: return
                return 
            
            ### To right
            if y < n - 1 and grid[x][y + 1] >= 0:
                cost = grid[x][y + 1]
                grid[x][y + 1] = -1
                backtrack(x, y + 1, k - cost, cur + 1)
                grid[x][y + 1] = cost  

            ### To down
            if x < m - 1 and grid[x + 1][y] >= 0:
                cost = grid[x + 1][y]
                grid[x + 1][y] = -1
                backtrack(x + 1, y, k - cost, cur + 1)
                grid[x + 1][y] = cost
            
            ### To left
            if x > 0 and grid[x - 1][y] >= 0:
                cost = grid[x - 1][y]
                grid[x - 1][y] = -1
                backtrack(x - 1, y, k - cost, cur + 1)
                grid[x - 1][y] = cost
            ### To up
            if y > 0 and grid[x][y - 1] >= 0:
                cost = grid[x][y - 1]
                grid[x][y - 1] = -1
                backtrack(x, y - 1, k - cost, cur + 1)
                grid[x][y - 1] = cost

        backtrack(0, 0, k, 0)
        
        return self.min_steps if self.min_steps != float('inf') else -1

def main():
    sol = Solution()
    grid, k = [[0,1,1], [1,1,1], [1,0,0]], 1      # Output: -1
    print(sol.shortestPath(grid, k))

    grid, k = [[0,0,0], [1,1,0], [0,0,0], [0,1,1], [0,0,0]], 1      # Output: 6
    print(sol.shortestPath(grid, k))

main()

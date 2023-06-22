''' 2328. Number of Increasing Paths in a Grid

Hard    805     21      Companies

You are given an m x n integer matrix grid, where you can move from a cell to 
any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can 
start from any cell and end at any cell. Since the answer may be very large, 
return it modulo 10^9 + 7.

Two paths are considered different if they do not have exactly the same 
sequence of visited cells.


Example 1:

Input: grid = [[1, 1],
               [3, 4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.


Example 2:

Input: grid = [[1],
               [2]]
Output: 3
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -> 2].
The total number of paths is 2 + 1 = 3.
 

Constraints:        m == grid.length
                    n == grid[i].length
                    1 <= m, n <= 1000
                    1 <= m * n <= 10^5
                    1 <= grid[i][j] <= 10^5
Accepted:           19.7K
Submissions:        40K
Acceptance Rate:    49.2%
'''

from typing import List


class Solution:     # My Solution passed. 
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0
        arr, trace = [], [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                arr.append([grid[i][j], i, j])
        arr.sort(reverse=True)

        for v, i, j in arr:
            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= x < m and 0 <= y < n and v < grid[x][y]:
                    trace[i][j] += trace[x][y]
            ans += trace[i][j]
        return ans % 1000000007

def main():
    sol = Solution()
    
    grid = [[1, 1],
            [3, 4]]  # Output: 8
    print(sol.countPaths(grid))

    grid = [[1],
            [2]]     # Output: 3
    print(sol.countPaths(grid))

    grid = [[1, 3, 4],
            [2, 5, 7]]     # Output: 22
    print(sol.countPaths(grid))

    grid = [[12469,18741,68716,30594,65029,44019,92944,84784,92781,5655,43120,81333,54113,88220,23446,6129,2904,48677,20506,79604,82841,3938,46511,60870,10825,31759,78612,19776,43160,86915,74498,38366,28228,23687,40729,42613,61154,22726,51028,45603,53586,44657,97573,61067,27187,4619,6135,24668,69634,24564,30255,51939,67573,87012,4106,76312,28737,7704,35798]]
    # Output: 148
    print(sol.countPaths(grid))


if __name__ == "__main__":
    main()

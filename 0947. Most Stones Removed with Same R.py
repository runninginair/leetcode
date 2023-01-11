''' 947. Most Stones Removed with Same Row or Column
Medium      3475      549      Add to List     Share

On a 2D plane, we place n stones at some integer coordinate points.
Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as
another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the
location of the ith stone, return the largest possible number of stones that
can be removed.


Example 1:

Input: stones = [[0,0], [0,1], [1,0], [1,2], [2,1], [2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

Example 3:
Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

Constraints:    1 <= stones.length <= 1000
                0 <= xi, yi <= 10^4
                No two stones are at the same coordinate point.
Accepted:       134,052
Submissions:    232,205

'''

from typing import List


class Solution:
    ''' 56 / 68 test cases passed.      Status: Time Limit Exceeded '''
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        m = n = counter = 0
        for stone in stones:
            m, n = max(m, stone[0]), max(n, stone[1])
        self.grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for stone in stones:
            self.grid[stone[0]][stone[1]] = 1

        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                self.grid[x][y] = -1
                for col in range(n + 1):
                    if self.grid[x][col] == 1:
                        self.grid[x][col] = -1
                        stack.append((x, col))
                for row in range(m + 1):
                    if self.grid[row][y] == 1:
                        self.grid[row][y] = -1
                        stack.append((row, y))

        for i in range(m + 1):
            for j in range(n + 1):
                if self.grid[i][j] == 1:
                    counter += 1
                    dfs(i, j)
        return N - counter
                    
class UnionFind(object):
    def __init__(self):
        self.parents = {}
        self.count = 0
    
    def make_set(self, x):
        self.parents[x] = x
        self.count += 1
        
    def find(self, x):
        if x not in self.parents:
            self.make_set(x)
            return x
        elif self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        if x_set != y_set:
            self.parents[x_set] = y_set
            self.count -= 1

class Solution_v2(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        uf = UnionFind()
        
        for x, y in stones:
            print(x, y, ~y)
            uf.union(x, ~y)
        
        return n - uf.count


def main():
    sol = Solution_v2()
    stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    print(sol.removeStones(stones))     # Output: 3

    # stones = [[0,0]]
    # print(sol.removeStones(stones))     # Output: 0

    # stones = [[0,1],[1,0],[1,1]]
    # print(sol.removeStones(stones))     # Output: 2


main()

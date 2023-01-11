''' 1706. Where Will the Ball Fall
Medium      1290        92      Add to List     Share
You have a 2-D grid of size m x n representing a box, and you have n balls.
The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell
that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the
bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the
bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get
stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V"
shaped pattern between two boards or if a board redirects the ball into either
wall of the box.

Return an array answer of size n where answer[i] is the column that the ball
falls out of at the bottom after dropping the ball from the ith column at the top,
or -1 if the ball gets stuck in the box.


Example 1:
Input: grid = [ [ 1, 1, 1,-1,-1],
                [ 1, 1, 1,-1,-1],
                [-1,-1,-1, 1, 1],
                [ 1, 1, 1, 1,-1],
                [-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.

Example 2:
Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.

Example 3:
Input: grid = [ [ 1, 1, 1, 1, 1, 1],
                [-1,-1,-1,-1,-1,-1],
                [ 1, 1, 1, 1, 1, 1],
                [-1,-1,-1,-1,-1,-1]]
Output: [0,1,2,3,4,-1]
 

Constraints:        m == grid.length
                    n == grid[i].length
                    1 <= m, n <= 100
                    grid[i][j] is 1 or -1.
Accepted:       55,014
Submissions:    83,561
'''

from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [ x for x in range(0, n + 1)]
        for i in range(m):
            grid[i] = [1] + grid[i] + [-1]

        for k in range(1, n + 1):
            for i in range(m):
                if res[k] == -1: break
                p = res[k]
                if grid[i][p] == 1 and grid[i][p + 1] == 1: res[k] += 1
                elif grid[i][p] == -1 and grid[i][p - 1] == -1: res[k] -= 1
                else: res[k] = -1
        # print("RES:", res)
        # print("# 1 -- res id:", id(res))
        for i in range(len(res)):
            # print(id(res[i]), end="\t")
            if res[i] != -1: res[i] -= 1
        # print("----- # 1st for loop ------")
        # print("RES:", res)

        ### CAUTION: Following NOT works
        # print("# 1 -- res id:", id(res))
        for r in res:
            #print(id(r), end="\t")
            if r != -1: r -= 1
        # print("----- # 2nd for loop ------")
        # print("RES:", res)
        return res[1:]


def main():
    sol = Solution()
    grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
    print(sol.findBall(grid))   # Expect Output: [1,-1,-1,-1,-1]

main()

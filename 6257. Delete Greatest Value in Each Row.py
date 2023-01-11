''' 6257. Delete Greatest Value in Each Row

Weekly Contest 323      Problem # 1
User Accepted:5948      User Tried:6270     Total Accepted:6012     Total Submissions:6941
Difficulty:Easy

You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.

 

Example 1:      1 | 2 | 4          1 | 2           1
               -----------  ==>   -------  ==>    ---
                3 | 3 | 1          3 | 1           1


Input: grid = [[1,2,4],[3,3,1]]
Output: 8
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.
Example 2:


Input: grid = [[10]]
Output: 10
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 10 from the first row. We add 10 to the answer.
The final answer = 10.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 100

'''

from typing import List


class Solution:     ### My solution, Passed
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        if m == 1:
            for g in grid: ans += sum(g)
            return ans
        for i in range(m):
            grid[i].sort()
        for j in range(n):
            largest = grid[0][j]
            for i in range(m):
                largest = max(largest, grid[i][j])
            ans += largest
        return ans


class Solution_v1:      ### LeetCode ID: 	numb3r5
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()
        res = 0
        for i in zip(*grid):
            res += max(i)
        return res

class Solution_v2:      ### LeetCode ID: 	xiaowuc1
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ret = 0
        while len(grid[0]):
            i = 0
            cand = 0
            while i < len(grid):
                j = 0
                now = 0
                while j < len(grid[i]):
                    if grid[i][j] > grid[i][now]:
                        now = j
                    j += 1
                cand = max(cand, grid[i][now])
                grid[i].pop(now)
                i += 1
            ret += cand
        return ret
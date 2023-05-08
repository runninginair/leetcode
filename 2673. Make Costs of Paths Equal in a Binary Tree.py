''' 2673. Make Costs of Paths Equal in a Binary Tree

Medium      174     2      Companies

You are given an integer n representing the number of nodes in a perfect binary
tree consisting of nodes numbered from 1 to n. The root of the tree is node 1
and each node i in the tree has two children where the left child is the node
2 * i and the right child is 2 * i + 1.

Each node in the tree also has a cost represented by a given 0-indexed integer
array cost of size n where cost[i] is the cost of node i + 1. You are allowed
to increment the cost of any node by 1 any number of times.

Return the minimum number of increments you need to make the cost of paths from
the root to each leaf node equal.

Note:

A perfect binary tree is a tree where each node, except the leaf nodes, has
exactly 2 children. The cost of a path is the sum of costs of nodes in the path.
 

Example 1:               1(1) 
                         /   \
                     5(2)     (3)2
                     /   \    /  \
                 2(4)  3(5)  (6)3 (7)1

Input: n = 7, cost = [1,5,2,2,3,3,1]
Output: 6
Explanation: We can do the following increments:
- Increase the cost of node 4 one time.
- Increase the cost of node 3 three times.
- Increase the cost of node 7 two times.
Each path from the root to a leaf will have a total cost of 9.
The total increments we did is 1 + 3 + 2 = 6.
It can be shown that this is the minimum answer we can achieve.


Example 2:               5(1) 
                         /   \
                     3(2)     (3)3

Input: n = 3, cost = [5,3,3]
Output: 0
Explanation: The two paths already have equal total costs, so no increments
are needed.
 

Constraints:        3 <= n <= 10^5
                    n + 1 is a power of 2
                    cost.length == n
                    1 <= cost[i] <= 10^4
Accepted:           5.5K
Submissions:        9.9K
Acceptance Rate:    55.9%
'''

import math
from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans, level = 0, int(math.log2(n + 1))
        for i in range(level, 1, -1):
            for j in range(2 ** (i - 1) - 1, 2 ** i - 1, 2):
                if cost[j] < cost[j + 1]:
                    ans += cost[j + 1] - cost[j]
                    cost[j] = cost[j + 1]
                else:
                    ans += cost[j] - cost[j + 1]
                    cost[j + 1] = cost[j]
                cost[j >> 1] += cost[j]
        return ans


class Solution_v2:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans, level = 0, int(math.log2(n + 1))
        for i in range(level, 1, -1):
            for j in range(2 ** (i - 1) - 1, 2 ** i - 1, 2):
                ans += abs(cost[j] - cost[j + 1])
                cost[j >> 1] += max(cost[j], cost[j + 1])
        return ans


class Solution_v3:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        for i in range(n // 2 - 1, -1, -1):
            l, r = i * 2 + 1, i * 2 + 2
            res += abs(cost[l] - cost[r])
            cost[i] += max(cost[l], cost[r])
            # print(i, l, r, res, cost)
        return res

def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()

    n, cost = 7, [1,5,2,2,3,3,1]   # Output: 6
    print(sol.minIncrements(n, cost))

    n, cost = 15, [1,5,2,2,3,3,1,8,7,6,5,4,3,2,1]   # Output: 15
    # print(sol.minIncrements(n, cost))


if __name__ == "__main__":
    main()

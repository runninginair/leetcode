''' 279. Perfect Squares
Medium      7799       340      Add to List     Share

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer;
in other words, it is the product of some integer with itself.
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.


Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 
Constraints:    1 <= n <= 10^4
Accepted:       582,800
Submissions:    1,118,453
'''

import collections
from math import sqrt


class Solution_v1:  ### DP solution     T: O(n*n^1/2)  M: O(n)
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        # dp[0] = 0   # Base Case
        
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if square > target: break
                dp[target] = min(dp[target], 1 + dp[target - square])
                # print("Target:", target, "\tdp:", dp)

        return dp[n]


class Solution_v2:
    def numSquares(self, n: int) -> int:
        q1 = [0]
        q2 = []
        level = 0
        visited = [False] * (n+1)
        while True:
            level += 1
            for v in q1:
                i = 0
                while True:
                    i += 1
                    t = v + i * i
                    if t == n: return level
                    if t > n: break
                    if visited[t]: continue
                    q2.append(t)
                    visited[t] = True
            q1 = q2
            q2 = []                
        return 0


class Solution_v3:
    def numSquares(self, n: int) -> int:
        queue = collections.deque([(0, 0)])
        visited = set()
        while queue:
            i, step = queue.popleft()
            step += 1
            for j in range(1, n + 1):
                k = i + j * j
                if k > n:
                    break
                if k == n:
                    return step
                if k not in visited:
                    visited.add(k)
                    queue.append((k, step))


class Solution_v4(object):  ### More BFS    in this problem, BFS is faster than DP.
    def numSquares(self, n):
        que = set()
        que.add(n)
        cnt = 0
        while que:
            tmp = set()
            cnt += 1
            for q in que:
                i = 1
                while i * i <= q:
                    v = q - i * i
                    if v == 0: return cnt
                    tmp.add(v)
                    i += 1
            que = tmp


class Solution_v5():        ### Math solution   T:O(n)  M:O(1)
    def numSquares(self, n: int) -> int:
        # Reduction by factor of 4
        while n % 4 == 0: n //= 4
        # Quick response for n = 8k + 7
        if n % 8 == 7: return 4
        # Check whether n = a^2 + b^2
        for a in range(int(sqrt(n)) + 1):
            b = int(sqrt(n - a * a))
            if (a * a + b * b) == n :
                return (a > 0) + (b > 0)
        # n = a^2 + b^2 + c^2
        return 3


def main():
    sol = Solution_v1()
    sol = Solution_v2()
    sol = Solution_v3()
    sol = Solution_v4()
    sol = Solution_v5()


    S, N = 12, 14
    # S, N = 1, 100
    for n in range(S, N):
        print(sol.numSquares(n))

main()

''' 790. Domino and Tromino Tiling
Medium      1.8K      654       Companies

You have two types of tiles: a 2 x 1 domino shape and a tromino shape.
You may rotate these shapes.
    ---------       ---------
    | X - X |       | X - X |
    ---------       ----| | |
                        | X |
                        -----
Given an integer n, return the number of ways to tile an 2 x n board.
Since the answer may be very large, return it modulo 10^9 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different
if and only if there are two 4-directionally adjacent cells on the board such
that exactly one of the tilings has both squares occupied by a tile.


Example 1:
Input: n = 3
Output: 5
Explanation: The five different ways are show above.

    X Y Z   X X Z   X Y Y   X Y Y   X X Y
    X Y Z   Y Y Z   X Z Z   X X Y   X Y Y

Example 2:
Input: n = 1
Output: 1


Constraints:        1 <= n <= 1000
Accepted:           57.5K
Submissions:        117.9K
Acceptance Rate:    48.8%
'''

class Solution:
    def numTilings(self, n: int) -> int:
        dp, kMod = [[0, 0] for _ in range(n + 1)], 1000000007
        dp[0][0] = dp[1][0] = 1
        for i in range(2, n + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 1][1] * 2) % kMod
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][1]) % kMod
        return dp[n][0]

class Solution_v2:
    def numTilings(self, n: int) -> int:
        if n < 3: return n
        dp, kMod = [0 for _ in range(n + 1)], 1000000007
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n + 1): dp[i] = (2 * dp[i - 1] + dp[i - 3]) % kMod
        return dp[n]

class Solution_v3:
    def numTilings(self, n: int) -> int:
        if n < 3: return n
        dp, k, kMod = [1, 1, 2, 0], 0, 1000000007
        for i in range(3, n + 1): 
            k = i % 4
            dp[k] = (2 * dp[k - 1] + dp[k - 3]) % kMod
        return dp[k]

def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()

    for n in range(1, 10): print(sol.numTilings(n))


if __name__ == "__main__":
    main()
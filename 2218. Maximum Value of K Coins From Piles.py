''' 2218. Maximum Value of K Coins From Piles

Hard        1.9K        35          Companies

There are n piles of coins on a table. Each pile consists of a positive number
of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it
to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the
composition of the i-th pile from top to bottom, and a positive integer k,
return the maximum total value of coins you can have in your wallet if you
choose exactly k coins optimally.


Example 1:  [   ]  [   ]    |   [   ]  [   ]    |   [   ]  [   ]       
           {[ 1 ]}{[ 7 ]}   |   [ 1 ] {[ 7 ]}   |  {[ 1 ]} [ 7 ]   
            [100]  [ 8 ]    |   [100] {[ 8 ]}   |  {[100]} [ 8 ]   
            [ 3 ]  [ 9 ]    |   [ 3 ]  [ 9 ]    |   [ 3 ]  [ 9 ]    
                            |                   |
             answer = 8     |    answer = 15    |   answer = 101

Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101
Explanation:
The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.


Example 2:

Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
Output: 706
Explanation:
The maximum total can be obtained if we choose all coins from the last pile.
 

Constraints:        n == piles.length
                    1 <= n <= 1000
                    1 <= piles[i][j] <= 10^5
                    1 <= k <= sum(piles[i].length) <= 2000
Accepted:           53.6K
Submissions:        86.2K
Acceptance Rate:    62.2%
'''

from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(len(piles) + 1)]
        # for d in dp: print(d)
        for i in range(1, len(piles) + 1):
            for j in range(1, k + 1):
                cur = 0
                for x in range(min(len(piles[i - 1]), j)):
                    cur += piles[i - 1][x]
                    dp[i][j] = max(dp[i][j], cur + dp[i - 1][j - x - 1])
                    # print("-------------")
                    # for d in dp: print(d)
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                # print("=============")
                # for d in dp: print(d)
        return dp[len(piles)][k]


class Solution_v1:  # NeetCode Backtracking Solution  # 77/122 testcases passed
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        # i: index of the i-th pile; coins: num of left coins we gonna collect.
        def dfs(i: int, coins: int):
            if i == n: return 0
            ans = dfs (i + 1, coins)
            curr = 0
            for j in range(min(len(piles[i]), coins)):
                curr += piles[i][j]
                ans = max(ans, curr + dfs(i + 1, coins - j - 1))
            return ans
        return dfs(0, k)


class Solution_v1_2:  ### NeetCode Backtracking Solution + DP cashing.
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[-1] * (k + 1) for _ in range(n)]
        # i: index of the i-th pile; coins: num of left coins we gonna collect.
        def dfs(i: int, coins: int):
            if i == n: return 0
            if dp[i][coins] != -1:
                return dp[i][coins]
            dp[i][coins] = dfs (i + 1, coins)
            curr = 0
            for j in range(min(len(piles[i]), coins)):
                curr += piles[i][j]
                dp[i][coins] = \
                    max(dp[i][coins], curr + dfs(i + 1, coins - j - 1))
            return dp[i][coins]
        return dfs(0, k)


def main():
    sol = Solution()
    sol = Solution_v1()
    sol = Solution_v1_2()

    piles, k = [[1,100,3],[7,8,9]], 2  
    print(sol.maxValueOfCoins(piles, k))    # Output: 101

    piles, k = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], 7
    print(sol.maxValueOfCoins(piles, k))    # Output: 706


if __name__ == "__main__":
    main()
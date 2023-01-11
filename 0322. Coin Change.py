''' 322. Coin Change
Medium      14456      324      Add to List     Share

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:    1 <= coins.length <= 12
                1 <= coins[i] <= 231 - 1
                0 <= amount <= 104
Accepted:       1,241,544
Submissions:    2,990,608
'''

import math
from typing import List


class Solution:     # Bottom Up DP (Tabulation)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        print(dp)

        for coin in coins:
            for i in range(coin, amount+1):
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    print(dp)

        return -1 if dp[-1] == math.inf else dp[-1]


def main():
    sol = Solution()
    coins, amount = [1,2,5], 11   # Output: 3
    print(sol.coinChange(coins, amount))

main()

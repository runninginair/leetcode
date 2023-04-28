''' 0983. Minimum Cost For Tickets

Medium      5.7K       95       Companies

You have planned some train traveling one year in advance.
The days of the year in which you will travel are given as an integer array days.
Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

 * a 1-day pass is sold for costs[0] dollars,
 * a 7-day pass is sold for costs[1] dollars, and
 * a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.

 * For example, if we get a 7-day pass on day 2, then we can travel for 7 days:
 2, 3, 4, 5, 6, 7, and 8.
 
Return the minimum number of dollars you need to travel every day in the given
list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your
travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.


Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your
travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
 

Constraints:        1 <= days.length <= 365
                    1 <= days[i] <= 365
                    days is in strictly increasing order.
                    costs.length == 3
                    1 <= costs[i] <= 1000
Accepted:           189.1K
Submissions:        294.1K
Acceptance Rate:    64.3%
'''


from typing import List


class Solution:  # NOT Correct!!!
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        c1, c7, c30 = costs[0], costs[1], costs[2]
        dp = [[days[0], c1], [days[0], c7], [days[0], c30],]
        print("#0", dp)
        for i in range(1, len(days)):
            pre = min(dp[0][1], dp[1][1], dp[2][1])
            dp[0][0], dp[0][1] = days[i], pre + c1
            if days[i] - dp[1][0] > 6:
                dp[1][0] = days[i]
                dp[1][1] = pre + c7
            if days[i] - dp[2][0] > 29:
                dp[2][0] = days[i]
                dp[2][1] = pre + c30
            print("#", i, dp)

        return min(dp[0][1], dp[1][1], dp[2][1])

# https://www.youtube.com/watch?v=4pY1bsBpIY4

class Solution_v1:  # Solution from Youtuber: Neetcode.    T:O(38 * n) => O(n)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            return dp[i]

        return dfs(0)

class Solution_v2:  # Solution from Youtuber: Neetcode. Iteration version.
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        for i in range(len(days)-1, -1, -1):
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                # print("day =", d, "  cost =", c)
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp.get(j, 0))
        return dp[0]


def main():
    sol = Solution()
    sol = Solution_v1()
    sol = Solution_v2()

    # days, costs = [1,4,6,7,8,20], [2,7,15]
    # print(sol.mincostTickets(days, costs))  # Output: 11

    # days, costs = [1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]
    # print(sol.mincostTickets(days, costs))  # Output: 17

    # index:       0  1  2  3   4   5   6   7   8   9   10
    days, costs = [4, 5, 9, 11, 14, 16, 17, 19, 21, 22, 24], [1, 4, 18]
    # for d, c in zip([1, 7, 30], costs): print("day =", d, "  cost =", c)
    print(sol.mincostTickets(days, costs))  # Output: 10


if __name__ == "__main__":
    main()

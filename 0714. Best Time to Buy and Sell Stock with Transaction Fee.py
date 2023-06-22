''' 0714. Best Time to Buy and Sell Stock with Transaction Fee

Medium      5.5K       141        Companies

You are given an array prices where prices[i] is the price of a given stock on 
the i-th day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions 
as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).


Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.


Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 

Constraints:        1 <= prices.length <= 5 * 10^4
                    1 <= prices[i] < 5 * 10^4
                    0 <= fee < 5 * 10^4
Accepted:           241.2K
Submissions:        365.9K
Acceptance Rate:    65.9%
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        his, ans = [], 0
        for i in range(len(prices)):
            if not his: his = [prices[i]]
            elif prices[i] < his[-1]:
                if len(his) == 1: his[0] = prices[i]
                else:
                    ans += his[1] - his[0] - fee
                    if prices[i] + fee <= his[1]: his = [prices[i]]
                    else: his = [his[1] - fee]
            elif prices[i] > his[-1]:
                if len(his) == 1:
                    if prices[i] > his[0] + fee: his.append(prices[i])
                else: his[-1] = prices[i]

        if len(his) > 1: ans += his[1] - his[0] - fee
        return ans

class Solution_v2:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = sale = income = 0
        for p in prices:
            if buy == 0: buy = p
            elif p < sale or p < buy:
                if sale == 0: buy = p
                else:
                    income += sale - buy - fee
                    if p + fee <= sale: buy = p
                    else: buy = sale - fee
                    sale = 0
            elif p > buy:
                if sale == 0:
                    if p > buy + fee:
                        sale = p
                elif p > sale:
                    sale = p
        if sale != 0: income += sale - buy - fee
        return income


def main():
    sol = Solution()
    sol = Solution_v2()

    prices, fee = [1,3,2,8,4,9], 2     # Output: 8
    print(sol.maxProfit(prices, fee))

    prices, fee = [1,3,7,5,10,3], 3    # Output: 6
    print(sol.maxProfit(prices, fee))

    prices, fee = [9,8,7,1,2], 3       # Output: 0
    print(sol.maxProfit(prices, fee))


if __name__ == "__main__":
    main()
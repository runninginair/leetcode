'''
0123. Best Time to Buy and Sell Stock III
'''

from cmath import e
from tempfile import tempdir


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices) -> int:
        n = len(prices) - 1
        p1, lo, hi = self.getMaxProfit(prices, 0, n)
        p2 = self.getMaxProfit(prices, 0, lo)[0]
        p3 = self.getMaxProfit(prices, hi, n)[0]
        return p1 + max(p2, p3)
        
    def getMaxProfit(self, price_list, start, end):
        maxIncome, lo, hi , temp = 0, start, start, -1
        minPrice = price_list[lo]
        for i in range(start, end+1): 
            if price_list[i] < minPrice:
                minPrice = price_list[i]
                temp = i
            if price_list[i] - minPrice > maxIncome:
                maxIncome = price_list[i] - minPrice
                hi = i
                lo = temp
        print("maxIncome =", maxIncome, "  Low =", lo, "  High =", hi)
        return maxIncome, lo, hi

def main():
    s =Solution()
    
    prices = [3,3,5,0,0,3,1,4]  # output:6
    print(s.maxProfit(prices))

    prices = [1,2,3,4,5] # Output: 4
    print(s.maxProfit(prices))

    prices = [7,6,4,3,1] # Output: 0
    print(s.maxProfit(prices))

    prices = [2,4,1] # Output: 2
    print(s.maxProfit(prices))

    prices = [6,1,3,2,4,7] # Output: 7
    print(s.maxProfit(prices))


main()


'''
Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
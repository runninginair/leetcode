''' 2517. Maximum Tastiness of Candy Basket
    6271. Maximum Tastiness of Candy Basket

Medium      134     5       Companies

You are given an array of positive integers price where price[i] denotes the
price of the ith candy and a positive integer k.

The store sells baskets of k distinct candies. The tastiness of a candy basket
is the smallest absolute difference of the prices of any two candies in the
basket.

Return the maximum tastiness of a candy basket.


Example 1:
Input: price = [13, 5, 1, 8, 21, 2], k = 3
Output: 8
Explanation: Choose the candies with the prices [13, 5, 21].
The tastiness of the candy basket is:
    min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
It can be proven that 8 is the maximum tastiness that can be achieved.

Example 2:
Input: price = [1, 3, 1], k = 2
Output: 2
Explanation: Choose the candies with the prices [1, 3].
The tastiness of the candy basket is: min(|1 - 3|) = min(2) = 2.
It can be proven that 2 is the maximum tastiness that can be achieved.

Example 3:
Input: price = [7, 7, 7, 7], k = 2
Output: 0
Explanation: Choosing any two distinct candies from the candies we have will
result in a tastiness of 0.
 

Constraints:    1 <= price.length <= 10^5
                1 <= price[i] <= 10^9
                2 <= k <= price.length
Accepted:           3.5K
Submissions:        5.8K
Acceptance Rate:    59.4%

'''

from typing import List


class Solution:     ### LeetCode ID: jinal2211
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        ### lo: minimum possible is 0
        ### hi: maximum it can be (max-min of price)
        n, lo, hi = len(price), 0, price[-1] - price[0]
        print(price, '\n', "  n =", n, "  k =", k, "  lo =", lo, "  hi =",hi, "\n")

        def check(mid: int) -> bool:
            if price[-1] - price[0] < mid: return False
            count, pre = 1, price[0]
            ### starting from 0-th index we will go to next element which is greater than price[0] + hi
            # ... and will increase count. doing that till we reach to the end.
            print("# 1   :", "  mid =", mid, "  count =", count, "  pre =", pre)
            for i in range(1, n):
                ### here pre store prev element which we have used.
                if price[i] - pre >= mid:
                    print("# 2. 1:", "  mid =", mid, "  count =", count, "  pre =", pre, "   price[i] =", price[i])
                    pre = price[i]
                    count += 1
                    print("# 2. 2:", "  mid =", mid, "  count =", count, "  pre =", pre, "   price[i] =", price[i])
            ### checking if we have more than k elements or not.
            print("# 3.  :", "  mid =", mid, "  count =", count, "  pre =", pre, end= "\n")
            return count >= k

        while hi - lo > 1:
            ### mid: calculating mid
            mid = (lo + hi) >> 1
            print("  while 0:  mid =", mid)
            if check(mid):
                ### we can have more elements than k with mid (in terms of absolute difference)
                lo = mid
                print("  while if:  mid = lo = ", mid, end= "\n\n")

            else:
                ### not possible to have k elements with mid
                hi = mid - 1
                print("  while else:  hi = mid - 1 =", hi, end= "\n\n")


        ### returning answer (first we will check greater because we need maximum)
        return hi if check(hi) else lo

class Solution_v2:     ### YouTuber ID: Larry   T: O(n*log n + n*logR) M:O(n)
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def good(target):
            candy, last = 0, -10 ** 9
            for x in price:
                if x - last >= target:
                    candy += 1
                    last = x
            return candy >= k
        
        left, right = 0, 10 ** 9

        while left < right:
            mid = (left + right + 1) >> 1
            if good(mid): left = mid
            else: right = mid - 1

        return left


def main():
    # sol = Solution()
    sol = Solution_v2()

    price, k = [7, 9, 11, 13, 15, 18, 21], 4    # Output: 4
    print(sol.maximumTastiness(price, k))

    price, k = [13, 5, 1, 8, 21, 2], 3  # Output: 8
    print(sol.maximumTastiness(price, k))

    price, k = [1, 3, 1], 2  # Output: 2
    print(sol.maximumTastiness(price, k))

    price, k = [7, 7, 7, 7], 2    # Output: 0
    print(sol.maximumTastiness(price, k))

    price, k = [7, 9, 11, 13, 15, 18, 21], 5    # Output: 3
    print(sol.maximumTastiness(price, k))

    price, k = [10, 10, 10, 10, 10, 10, 12], 3  # Output: 0
    print(sol.maximumTastiness(price, k))


main()     
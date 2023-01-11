''' 6266. Smallest Value After Replacing With Sum of Prime Factors
User Accepted:421
User Tried:630
Total Accepted:422
Total Submissions:854
Difficulty:Medium

You are given a positive integer n.

Continuously replace n with the sum of its prime factors.

Note that if a prime factor divides n multiple times, it should be included in
the sum as many times as it divides n.

Return the smallest value n will take on.

Example 1:
Input: n = 15
Output: 5
Explanation: Initially, n = 15.
15 = 3 * 5, so replace n with 3 + 5 = 8.
8 = 2 * 2 * 2, so replace n with 2 + 2 + 2 = 6.
6 = 2 * 3, so replace n with 2 + 3 = 5.
5 is the smallest value n will take on.

Example 2:
Input: n = 3
Output: 3
Explanation: Initially, n = 3.
3 is the smallest value n will take on.
 
Constraints:        2 <= n <= 10^5
'''

from typing import List


class Solution:     # My Brute Force Solution, Time Limit Exceeded
    def smallestValue(self, n: int) -> int:
        
        def getPrimeFactor(num: int) -> int:
            for i in range(2, (num >> 1) + 1):
                if num % i == 0: return i
            return num

        def getPrimeFactorList(num: int) -> List[int]:
            ans = []
            while getPrimeFactor(num) != num:
                ans.append(getPrimeFactor(num))
                num //= ans[-1]
            ans.append(num)
            return ans

        while len(getPrimeFactorList(n)) > 1:
            n = sum(getPrimeFactorList(n))

        return n

class Solution_v2:      ### LeetCode ID: Alpha_690163
    def smallestValue(self, n: int) -> int:
        k = n
        if n <= 4: return n

        def isPrime(n: int) -> bool:
            for i in range(2, int(n ** (0.5)) + 1):
                if n % i == 0: return False
            return True

        while True:
            sum = 0
            for i in range(2, (n >> 1) + 1):
                if isPrime(i):
                    while n % i == 0:
                        sum += i
                        n //= i
            if n == 1: sum -= 1
            sum += n
            if n == sum:
                k = sum
                break
            else:
                n = k = sum
        return k


def main():
    sol = Solution()
    sol = Solution_v2()

    print(sol.smallestValue(15))        # output: 5
    print(sol.smallestValue(3))         # output: 3


main()

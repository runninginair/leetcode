''' 2523. Closest Prime Numbers in Range

Medium      33      8       Companies

Given two positive integers left and right,
find the two integers num1 and num2 such that:

 * left <= nums1 < nums2 <= right .
 * nums1 and nums2 are both prime numbers.
 * nums2 - nums1 is the minimum amongst all other pairs satisfying the above
   conditions.

Return the positive integer array ans = [nums1, nums2]. If there are multiple
pairs satisfying these conditions, return the one with the minimum nums1 value
or [-1, -1] if such numbers do not exist.

A number greater than 1 is called prime if it is only divisible by 1 and itself.


Example 1:
Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the
conditions cannot be satisfied.
 

Constraints:        1 <= left <= right <= 10^6

Accepted:           5.2K
Submissions:        16.2K
Acceptance Rate:    31.8%
'''
import math
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left < 3 and right > 2: return [2, 3]
        lis = []
        def isPrime(num: int) -> bool:
            for i in range(2, int(num ** 0.5) + 1): 
                if num % i == 0: return False
            return True
        start = left if left & 1 else left + 1
        for i in range(start, right + 1, 2):
            if isPrime(i):
                lis.append(i)
                if len(lis) > 1 and lis[-1] - lis[-2] == 2: return [lis[-2], lis[-1]]
        if len(lis) < 2: return [-1, -1]
        gap = math.inf
        res = [-1, -1]
        for i in range(1, len(lis)):
            diff = lis[i] - lis[i - 1]
            if diff == 2: return [lis[i - 1], lis[i]]
            if diff < gap:
                gap = diff
                res[0], res[1] = lis[i - 1], lis[i]
        return res



def main():
    sol = Solution()

    left, right = 10, 19            # Output: [11, 13]
    print(sol.closestPrimes(left, right))

    left, right = 4, 6              # Output: [-1, -1]
    print(sol.closestPrimes(left, right))

    left, right = 111, 198          # Output: [137, 139]
    print(sol.closestPrimes(left, right))

    left, right = 1, 100000          # Output: [2, 3]
    print(sol.closestPrimes(left, right))

main()

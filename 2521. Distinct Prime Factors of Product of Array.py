''' 2521. Distinct Prime Factors of Product of Array

Medium      48      4       Companies

Given an array of positive integers nums, return the number of distinct prime
factors in the product of the elements of nums.

Note that:

 * A number greater than 1 is called prime if it is divisible by only 1 and itself.
 * An integer val1 is a factor of another integer val2 if val2 / val1 is an integer.
 

Example 1:
Input: nums = [2,4,3,7,10,6]
Output: 4
Explanation:
The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7.
There are 4 distinct prime factors so we return 4.

Example 2:
Input: nums = [2,4,8,16]
Output: 1
Explanation:
The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = 210.
There is 1 distinct prime factor so we return 1.

Constraints:        1 <= nums.length <= 104
                    2 <= nums[i] <= 1000

Accepted:           7.7K
Submissions:        17.2K
Acceptance Rate:    44.4%
'''
from typing import List

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def getFactor(num: int) -> List[int]:
            if num == 1: return [1]
            res = []
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0: res.append(i)
                while num % i == 0: num //= i
                if num == 1 or i > num: break
            if num != 1: res.append(num)
            return res
        lis = []
        for num in nums: lis += getFactor(num)
        return len(set(lis))

class Solution_v2:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()
        def getFactor(num: int) -> None:
            if num == 1: res.add(1)
            else:
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0: res.add(i)
                    while num % i == 0: num //= i
                    if num == 1 or i > num: break
                if num != 1: res.add(num)
        for num in nums: getFactor(num)
        return len(res)

class Solution_v3:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()
        def getFactor(num: int) -> None:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0: res.add(i)
                while num % i == 0: num //= i
                if num == 1: break
            if num != 1: res.add(num)
        for num in nums: getFactor(num)
        return len(res)

def main():
    sol = Solution()
    sol = Solution_v3()

    nums = [2, 4, 3, 7, 10, 6]    # 4
    # nums = [8]     
    print(sol.distinctPrimeFactors(nums))

main()

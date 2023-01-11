''' 446. Arithmetic Slices II - Subsequence

Day of 11/26/2022

Hard    1593    93      Add to List     Share

Given an integer array nums, return the number of all the arithmetic
subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic
sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some
elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.


Example 1:
Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

Example 2:
Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.
 

Constraints:        1  <= nums.length <= 1000
                    -2^31 <= nums[i] <= 2^31 - 1
Accepted:       49,066
Submissions:    120,562
'''

from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [defaultdict(int) for _ in range(N)]
        ans = 0
     
        for i in range(1, N):
            for j in range(i):
                diff = nums[i] - nums[j]
                ans += dp[j][diff]
                dp[i][diff] += dp[j][diff] + 1
                # print("i =", i, " j =", j, " |  Diff =", diff,"  dp[j][dif]:",dp[j][diff], " dp[i][diif]:",dp[i][diff], " ans:",ans)
                print(f"{i=} {j=} {diff=}   {dp[j][diff]=} {dp[i][diff]=} {ans=}")

        for ele_dp in dp: print(ele_dp)
        return ans

def main():
    sol = Solution()
    # nums = [2,4,6,8,10] # Output: 7
    # print(sol.numberOfArithmeticSlices(nums))

    # nums = [7,7,7,7,7]  # Output: 16
    # print(sol.numberOfArithmeticSlices(nums))

    # nums = [2,4,6,7,8,7,10,7,7] # Output: 7
    # print(sol.numberOfArithmeticSlices(nums))

    # nums = [2,6,7,10,8] # Output: 2
    # print(sol.numberOfArithmeticSlices(nums))  

    # nums = [5,10,15,20] # Output: 3
    # print(sol.numberOfArithmeticSlices(nums))  

    nums = [1,3,5,7,9] # Output: 3
    print(sol.numberOfArithmeticSlices(nums))  

main()

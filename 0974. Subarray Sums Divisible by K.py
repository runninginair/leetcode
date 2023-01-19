''' 974. Subarray Sums Divisible by K

Medium      4K      158        Companies

Given an integer array nums and an integer k, return the number of non-empty
subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.


Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0
 

Constraints:        1 <= nums.length <= 3 * 10^4
                    -10^4 <= nums[i] <= 10^4
                    2 <= k <= 10^4
Accepted:           133.6K
Submissions:        249.2K
Acceptance Rate:    53.6%
'''

from typing import List

class Solution:     ### Brute Force  T: O(n^3)  TLE  38 / 73 testcases passed
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n, ans = len(nums), 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if sum(nums[i:j]) % k == 0: ans += 1
        return ans

class Solution_v1:     ### Brute Force  T: O(n^2)   TLE  66 / 73 testcases passed
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n, ans = len(nums), 0
        for i in range(n):
            prefixSum = 0
            for j in range(i, n):
                prefixSum += nums[j]
                if prefixSum % k == 0: ans += 1
        return ans

class Solution_v5:      ### Cache + DP solution T: O(n) M: O(n + k)
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n, prefixSum = len(nums), 0
        cache, dp = {}, [0] * n
        cache[0] = 0
        for i, num in enumerate(nums):
            prefixSum += num
            rem = prefixSum % k
            if rem in cache:
                cache[rem] += 1
                dp[i] = cache[rem]
            else: cache[rem] = 0
        return sum(dp)

class Solution_v5_2:      ### Cache + DP solution T: O(n) M: O(k)
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans, prefixSum, cache = 0, 0, {}
        cache[0] = 0
        for i, num in enumerate(nums):
            prefixSum += num
            rem = prefixSum % k
            if rem in cache:
                cache[rem] += 1
                nums[i] = cache[rem]
            else: nums[i] = cache[rem] = 0
            ans += nums[i]
        return ans


def main():
    sol = Solution()
    sol = Solution_v1()
    sol = Solution_v5()
    sol = Solution_v5_2()

    nums, k = [4,5,0,-2,-3,1], 5        # Output: 7
    print(sol.subarraysDivByK(nums, k))

    nums, k = [5], 9                    # Output: 0
    print(sol.subarraysDivByK(nums, k))

    nums, k = [-1, 2, 9], 2             # Output: 2
    print(sol.subarraysDivByK(nums, k))


if __name__ == "__main__":
    main()

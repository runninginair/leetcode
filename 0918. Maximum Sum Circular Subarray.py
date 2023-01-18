''' 918. Maximum Sum Circular Subarray

Medium      4.1K      184       Companies

Given a circular integer array nums of length n, return the maximum possible
sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the
array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the
previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once.
Formally, for a subarray nums[i], nums[i + 1], ..., nums[j],
there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.


Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 

Constraints:            n == nums.length
                        1 <= n <= 3 * 10^4
                        -3 * 10^4 <= nums[i] <= 3 * 10^4
Accepted:           148.5K
Submissions:        385K
Acceptance Rate:    38.6%

'''

import math
from typing import List

class Solution_v0:  ### Brute Force O(n^2)    LTE -> 96 / 111 testcases passed
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        res, n = nums[0], len(nums)
        nums += nums
        for j in range(n):
            sum = 0
            for i in range(j, n + j):
                sum += nums[i]
                if nums[i] > sum: sum = nums[i]
                res = max(res, sum)
        return res

class Solution:     ### YouTuber: Timothy Chang     T: O(n)
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ### Case 1: find the max sum of subarray in nums:
        res, n, sum  = nums[0], len(nums), -math.inf
        for i in range(n):
            sum += nums[i]
            sum = max(sum, nums[i])
            res = max(res, sum)

        ### Case 2: find the circular one
        dp = [0] * n * 2
        for i in range(n): dp[n + i] += dp[n + i - 1] + nums[i]
        for i in range(1, n): dp[n + i] = max(dp[n + i], dp[n + i - 1])
        dp[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1): dp[i] += dp[i + 1] + nums[i]
        for i in range(n - 2, -1, -1): dp[i] = max(dp[i], dp[i + 1])

        for i in range(1, n - 1): res = max(res, dp[1 + i] + dp[n + i - 1])
        return res


''' Official Java Solution
class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        final int n = nums.length;
        final int[] rightMax = new int[n];
        rightMax[n - 1] = nums[n - 1];
        for (int suffixSum = nums[n - 1], i = n - 2; i >= 0; --i) {
            suffixSum += nums[i];
            rightMax[i] = Math.max(rightMax[i + 1], suffixSum);
        }
        int maxSum = nums[0];
        int specialSum = nums[0];
        for (int i = 0, prefixSum = 0, curMax = 0; i < n; ++i) {
            curMax = Math.max(curMax, 0) + nums[i];
            // This is Kadane's algorithm.
            maxSum = Math.max(maxSum, curMax);
            prefixSum += nums[i];
            if (i + 1 < n) {
                specialSum = Math.max(specialSum, prefixSum + rightMax[i + 1]);
            }
        }
        return Math.max(maxSum, specialSum);  
    }
}

'''
class Solution_official:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        rightMax = [0] * n
        rightMax[n - 1] = suffixSum = nums[n - 1]
        for i in range(n - 2, -1 , -1):
            suffixSum += nums[i]
            rightMax[i] = max(rightMax[i + 1], suffixSum)

        maxSum = specialSum = nums[0]
        prefixSum = curMax = 0
        for i in range(n):      ### This is Kadane's algorithm.
            curMax = max(curMax, 0) + nums[i]
            maxSum = max(maxSum, curMax)
            prefixSum += nums[i]
            if i + 1 < n: specialSum = max(specialSum, prefixSum + rightMax[i + 1])
        return max(maxSum, specialSum)

class Solution_official_withPrintTrace:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        rightMax = [0] * n
        rightMax[n - 1] = suffixSum = nums[n - 1]
        print("# 1:", rightMax, suffixSum)
        for i in range(n - 2, -1 , -1):
            suffixSum += nums[i]
            rightMax[i] = max(rightMax[i + 1], suffixSum)
        print("# 2:", rightMax, suffixSum)

        maxSum = specialSum = nums[0]
        prefixSum = curMax = 0
        for i in range(n):
            curMax = max(curMax, 0) + nums[i]
            ### This is Kadane's algorithm.
            maxSum = max(maxSum, curMax)
            prefixSum += nums[i]
            if i + 1 < n: specialSum = max(specialSum, prefixSum + rightMax[i + 1])
            print("# 3:", " nums[i] =", nums[i], " curMax =", curMax, " maxSum =", maxSum, " prefixSum =", prefixSum, " specialSum =", specialSum)
        
        return max(maxSum, specialSum)

def main():
    sol = Solution_v0()
    sol = Solution()
    sol = Solution_official()
    # sol = Solution_official_withPrintTrace()

    nums = [1,-2,3,-2]  # Output: 3
    print(sol.maxSubarraySumCircular(nums))

    nums = [5,-3,5]     # Output: 10
    print(sol.maxSubarraySumCircular(nums))

    nums = [-3,-2,-3]   # Output: -2
    print(sol.maxSubarraySumCircular(nums))

    nums = [2,2,2,-1,10,10]   # Output: 26
    print(sol.maxSubarraySumCircular(nums))

main()
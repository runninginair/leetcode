''' 1498. Number of Subsequences That Satisfy the Given Sum Condition

Medium      2.4K      214       Companies

You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the
minimum and maximum element on it is less or equal to target.
Since the answer may be too large, return it modulo 109 + 7.


Example 1:
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)


Example 2:
Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition.
(nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]


Example 3:
Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy
the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
 

Constraints:        1 <= nums.length <= 10^5
                    1 <= nums[i] <= 10^6
                    1 <= target <= 10*6
Accepted:           55.9K
Submissions:        137.7K
Acceptance Rate:    40.6%
'''

from typing import List


class Solution:     # My Solution 
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0] * 2 > target:
            return 0
        n, offset = len(nums), 0
        l, r, half = 0, n - 1, target >> 1
        while nums[r] > target or nums[r] + nums[0] > target: r -= 1
        mid = r

        while nums[mid] > half: mid -= 1
        for i in range(r, mid, -1):
            while nums[l] + nums[i] <= target:
                l += 1
            offset += 2 ** (i - l)
        return (2 ** (r + 1) - 1 - offset) % 1000000007

class Solution_NeetCode:     # NeetCode Two Pointer Solution
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, mod, r  = 0, 10**9 + 7, len(nums) - 1
        for l, num in enumerate(nums):
            while num + nums[r] > target and l <= r:
                r -= 1
            if l <= r:
                ans += 2 ** (r - l)
                ans %= mod
            else: break
        return ans

class Solution_NeetCode_Me:     # NeetCode Two Pointer Solution
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, mod = 0, 10**9 + 7
        r = len(nums) - 1
        for l, num in enumerate(nums):
            if num * 2 > target: break
            while num + nums[r] > target and l < r: r -= 1
            ans += 2 ** (r - l)
            ans %= mod
        return ans

def main():
    sol = Solution()
    sol = Solution_NeetCode()

    #   0  1  2  3  4  5  6  7  8  9  10 11 12
    #  [1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 7, 8, 10, 12, 14]      Target = 12
    #                                       r
    #                              mid
    nums = [1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 7, 8, 10, 12, 14]
    target = 12   # Output: 7127
    print(sol.numSubseq(nums, target))

    nums = [3, 5, 6, 7]
    target = 9    # Output: 4
    print(sol.numSubseq(nums, target))

    nums = [3, 3, 6, 8]
    target = 10   # Output: 6
    print(sol.numSubseq(nums, target))

    nums = [2, 3, 3, 4, 6, 7]
    target = 12   # Output: 61
    print(sol.numSubseq(nums, target))


if __name__ == "__main__":
    main()

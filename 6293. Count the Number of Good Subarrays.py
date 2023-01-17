''' 6293. Count the Number of Good Subarrays

User Accepted:1
User Tried:3
Total Accepted:1
Total Submissions:3
Difficulty:Medium

Given an integer array nums and an integer k, return the number of good
subarrays of nums.

A subarray arr is good if it there are at least k pairs of indices (i, j)
such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.

Example 2:
Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
 

Constraints:    1 <= nums.length <= 10^5
                1 <= nums[i], k <= 10^9

'''

from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans, cnt = 0, {}
        l = r = cur =0
        while r < len(nums):
            if nums[r] in cnt:
                cnt[nums[r]] += 1
                cur += cnt[nums[r]] - 1
                if cur >= k: ans += 1
            else: cnt[nums[r]] = 1

            r += 1

        # while cur >= k:
        #     l -= 1
        #     cnt[nums[l]] -= 1
        return ans



def main():
    sol = Solution()

    # nums, k = [1,1,1,1,1], 10      # Output: 1
    # print(sol.countGood(nums, k))

    nums, k = [3,1,4,3,2,2,4], 2   # Output: 4
    print(sol.countGood(nums, k))


main()

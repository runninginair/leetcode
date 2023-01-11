''' 220. Contains Duplicate III
Hard    273     4       Add to List     Share

You are given an integer array nums and two integers indexDiff and valueDiff.
Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.


Example 1:
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

Example 2:
Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.
 

Constraints:    2 <= nums.length <= 10^5
                -10^9 <= nums[i] <= 10^9
                1 <= indexDiff <= nums.length
                0 <= valueDiff <= 10^9
Accepted:       219,532
Submissions:    1,001,299
'''

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        N = len(nums)
        memo = [[0, 0] for _ in range(N)]
        for i in range(N):
            memo[i] = [nums[i], i]
        print(memo)
        memo.sort(key = lambda x: x[1], reverse = True)
        print(memo)        
        memo.sort(key = lambda x: x[0])
        print(memo)

        p1, p2 = 0, 1
        
        while p2 < N:
            if memo[p2][0] - memo[p1][0] <= valueDiff:
                if abs(memo[p2][1] - memo[p1][1]) <= indexDiff: return True
                p2 += 1
            else:
                p1 += 1
                if p2 == p1: p2 += 1
        return False


def main():
    sol = Solution()
    nums, indexDiff, valueDiff = [8,7,15,1,6,1,9,15], 1, 3  # Expect: True
    print(sol.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))

main()

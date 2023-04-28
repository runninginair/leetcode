''' 2444. Count Subarrays With Fixed Bounds

Hard        616        11        Companies

You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.


Example 1:
Input: nums = [1, 3, 5, 2, 7, 5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Example 2:
Input: nums = [1, 1, 1, 1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

Constraints:        2 <= nums.length <= 10^5
                    1 <= nums[i], minK, maxK <= 10^6
Accepted:           12.1K
Submissions:        27K
Acceptance Rate:    44.9%
'''

from typing import List

class Solution:     ### Optimal Solution T: O(n)    M: O(1)
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res, preIndex, minBound, maxBound = 0, -1,  -1, -1
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK: preIndex = i
            if nums[i] == minK: minBound = i
            if nums[i] == maxK: maxBound = i
            res += max(0, min(minBound, maxBound) - preIndex)
        return res

def main():
    sol = Solution()

    nums, minK, maxK = [1, 3, 5, 2, 7, 5], 1, 5                     # Output: 2
    print(sol.countSubarrays(nums, minK, maxK))

    nums, minK, maxK = [1, 1, 1, 1], 1, 1                           # Output: 10
    print(sol.countSubarrays(nums, minK, maxK))

    nums, minK, maxK = [35054, 398719, 945315, 945315, 820417, 945315, 
                        35054, 945315, 171832, 945315, 35054, 109750,
                        790964, 441974, 552913], 35054, 945315      # Output: 81
    print(sol.countSubarrays(nums, minK, maxK))

    nums, minK, maxK = [1, 1, 3, 5, 5, 2, 1, 7, 5], 1, 5            # Output: 11
    print(sol.countSubarrays(nums, minK, maxK))
'''
            # 1            1, 3, 5              ---Atom substring
            # 2         1, 1, 3, 5
            # 3            1, 3, 5, 5
            # 4            1, 3, 5, 5, 2
            # 5            1, 3, 5, 5, 2, 1
            # 6         1, 1, 3, 5, 5
            # 7         1, 1, 3, 5, 5, 2
            # 8         1, 1, 3, 5, 5, 2, 1
            # 9                     5, 2, 1     ---Atom substring
            # 10                 5, 5, 2, 1
            # 11              3, 5, 5, 2, 1
            #              1, 3, 5, 5, 2, 1     ## Duplicated
            #           1, 1, 3, 5, 5, 2, 1     ## Duplicated
'''

''' Java Sliding window solution

class Solution {
    public long countSubarrays(int[] A, int minK, int maxK) {
        long res = 0, jbad = -1, jmin = -1, jmax = -1, n = A.length;
        for (int i = 0; i < n; ++i) {
            if (A[i] < minK || A[i] > maxK) jbad = i;
            if (A[i] == minK) jmin = i;
            if (A[i] == maxK) jmax = i;
            res += Math.max(0L, Math.min(jmin, jmax) - jbad);
        }
        return res;
    }
}

'''


if __name__ == "__main__":
    main()

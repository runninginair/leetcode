''' 523. Continuous Subarray Sum
Medium      2787       329      Add to List     Share
Given an integer array nums and an integer k, return true if nums has a continuous subarray
of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k.
0 is always a multiple of k.


Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:    1 <= nums.length <= 105
                0 <= nums[i] <= 109
                0 <= sum(nums[i]) <= 231 - 1
                1 <= k <= 231 - 1
'''

class Solution:
    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    def checkSubarraySum(self, nums, k: int) -> bool:
        n = len(nums)
        if n == 1: return False
        total = 0
        dic = {}
        zero_index = -1
        for i in range(n):
            if nums[i] % k ==  0:
                if zero_index >= 0 and i - zero_index == 1: return True
                else: zero_index = i
            
            total += nums[i]
            mod = total % k
            if mod == 0:
                if i > 0:
                    return True
                else:
                    continue
            else:
                if mod not in dic:
                    dic[mod] = i
                else:
                    if i - dic[mod] > 1:
                        return True
                    else:
                        dic[mod] = i
        return False

def main():
    sol = Solution()

    nums, k = [23,2,4,6,7], 6
    print(sol.checkSubarraySum(nums, k))

    nums, k = [23,2,6,4,7], 13
    print(sol.checkSubarraySum(nums, k))

    nums, k = [23,2,4,6,6], 7
    print(sol.checkSubarraySum(nums, k))

    nums, k = [5,0,0,0], 3
    print(sol.checkSubarraySum(nums, k))

main()

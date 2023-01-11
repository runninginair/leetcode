''' 209. Minimum Size Subarray Sum
Medium      8041    223     Add to List     Share
Given an array of positive integers nums and a positive integer target, return
the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
of which the sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

 

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:    1 <= target <= 10^9
                1 <= nums.length <= 10^5
                1 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another
solution of which the time complexity is O(n log(n)).

Accepted:       615,659
Submissions:    1,386,938
'''

class Solution:
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    def minSubArrayLen(self, target: int, nums) -> int:
        if sum(nums) < target:
            return 0
        
        p1, p2 = -1, 0
        # nums = [0].extend(nums)
        res = float('inf')
        temp = nums[0]
        while p1 < len(nums) - 1 and p2 < len(nums):
            if temp < target:
                p2 += 1
                if p2 >= len(nums):
                    break
                temp += nums[p2]
            else:  # temp >= target
                if p1 == p2: return 1
                p1 += 1
                temp -= nums[p1]
                res = min(res, p2 - p1 + 1)
        return res


def main():
    sol = Solution()
    target, nums = 7, [2,3,1,2,4,3]
    print(sol.minSubArrayLen(target, nums))

    target, nums = 11, [1,2,3,4,5]
    print(sol.minSubArrayLen(target, nums))


main()

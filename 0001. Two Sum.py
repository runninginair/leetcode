''' 1. Two Sum
Easy    39578    1278    Add to List    Share

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:    2 <= nums.length <= 104
                -109 <= nums[i] <= 109
                -109 <= target <= 109
                Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

Accepted:       8,162,857
Submissions:    16,635,835
'''

from typing import List

class Solution_v0:      # Breute force      T: O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        for i in range(N - 1):
            for j in range(i + 1, N):
                if nums[i] + nums[j] == target: return [i, j]
        return [-1, -1]

class Solution_v1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N, dic = len(nums), {}
        for i in range(N):
            dic[nums[i]] = i

        for i in range(N):
            diff = target - nums[i]
            if target - nums[i] in dic:
                if i != dic[diff]:
                    return [i, dic[diff]]
        return [-1, -1]

class Solution_v2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}    # Store the nums to the dictionary/map/hash-table
        for i, num in enumerate(nums):
            # Since the dic cann't have two element with a same key. so, we swap the key:value pair.
            dic.update({num: i})
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dic and dic[diff] != i:
                return [i, dic.get(diff)]
        return [-1, -1]

class Solution_v3:      # Optimal Solution  T: O(n)     M: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dic: return [dic[diff], i]
            dic.update({num: i})
        return [-1, -1]


def main():
    sol = Solution_v0()
    sol = Solution_v1()
    sol = Solution_v2()
    sol = Solution_v3()

    nums, target = [2, 7, 11, 15], 9    # Output: [0,1]
    print(sol.twoSum(nums, target))

    nums, target = [3,2,4], 6       # Output: [1,2]
    print(sol.twoSum(nums, target))

    nums, target = [3,3], 6     # Output: [0,1]
    print(sol.twoSum(nums, target))

main()

''' 34. Find First and Last Position of Element in Sorted Array
Medium      14000       345     Add to List     Share
Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:    0 <= nums.length <= 105
                -109 <= nums[i] <= 109
                nums is a non-decreasing array.
                -109 <= target <= 109
Accepted:       1,322,343
Submissions:    3,193,930
'''

from gettext import find


class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    def searchRange(self, nums, target: int):
        n = len(nums)
        lo, hi, key = 0, n-1, -1
        while (lo < hi):
            mid = (lo + hi) // 2
            print("# 0:", mid)
            if nums[mid] == target:
                key = mid
                print("# 1:", key)
                break
            elif nums[mid] < target:
                lo = mid + 1
                print("# 2:", lo)
            else:
                hi = mid - 1
                print("# 3:", hi)
            print("----  ", lo, hi, key, end="\n\n")
        if key == -1:
            print("key =", key)
            return [-1, -1]
        # return [key, key]

        def findLeft(start, end):
            left = -1
            while start < end:
                left = (start + end) // 2
                if nums[left] < target: start = left + 1
                else: end = left - 1
            return left
        
        def findRight(start, end):
            right = -1
            while start < end:
                right = (start + end) // 2
                if nums[right] > target: end = right - 1
                else: start = right + 1
            return right            
                    
        return findLeft(0, key), findRight(key, n-1)


def main():
    sol = Solution()
                #   0, 1  2  3  4  5
    nums, target = [5, 7, 7, 8, 8, 10], 8   # Output: [3,4]
    print(sol.searchRange(nums, target))

main()

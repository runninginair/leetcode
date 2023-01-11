''' 377. Combination Sum IV
Medium      5287      544       Add to List     Share
Given an array of distinct integers nums and a target integer target, return
the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.


Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0

Constraints:    1 <= nums.length <= 200
                1 <= nums[i] <= 1000
                All the elements of nums are unique.
                1 <= target <= 1000

Follow up:  What if negative numbers are allowed in the given array? 
            How does it change the problem?
            What limitation we need to add to the question to allow negative numbers?

Accepted:       333,870
Submissions:    640,852

'''

from typing import List


class Solution:     ### Brute Force O((n*target) ^ 2)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.res = []

        def dfs(nums, target, curr):
            if sum(curr) >= target:
                print(curr)
                if sum(curr) == target:
                    if curr not in self.res:
                        self.res.append(curr.copy())
                return

            for n in nums:
                curr.append(n)
                dfs(nums, target, curr)
                curr.pop()

        dfs(nums, target, [])
        
        return len(self.res)

class Solution_v2:  ### DP solution O(n * target)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # O(n * target) n = len(nums)
        dp = {0:1}
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)
        return dp[target]    

def main():
    sol = Solution()
    sol = Solution_v2()

    # nums, target = [1, 2, 3], 4  # Output: 7
    # print(sol.combinationSum4(nums, target))

    nums, target = [1, 50], 200  # Output: ?
    print(sol.combinationSum4(nums, target))


main()

'''
LeetCode 15. 3Sum

15. 3Sum
Medium  21218   1973    Add to List     Share
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.


Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.


Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
Accepted:       2,243,008
Submissions:    7,001,476

'''

# brute force
class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        if n < 3: return res

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range( j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        res.append(temp)

        if not res: return []
        ans = []
        ans.append(res[0])
        for i in range(len(res)):
            if res[i][0] == ans[-1][0] and res[i][1] == ans[-1][1] and res[i][2] == ans[-1][2]:
                continue
            else:
                ans.append([res[i][0], res[i][1], res[i][2]])

        return ans


def main():
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))

    nums = [0, 1, 1]    
    print(sol.threeSum(nums))

    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(sol.threeSum(nums))

main()

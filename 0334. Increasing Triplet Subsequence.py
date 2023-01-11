''' 334. Increasing Triplet Subsequence
Medium      4471    226     Add to List     Share
Given an integer array nums, return true if there exists a triple of indices
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.


Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:    1 <= nums.length <= 5 * 105
                -231 <= nums[i] <= 231 - 1
 
Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
Accepted:       299,609
Submissions:    718,642

'''
import math

class Solution:
    def increasingTriplet(self, nums) -> bool:
        n = len(nums)
        if n < 3: return False
        q = [nums[0]]
        flag = math.inf

        for i in range(1, n):
            print("q =", q, "  flag =", flag, "  i =", i)
            if nums[i] > flag:
                return True
            if nums[i] > q[0]:
                if len(q) == 1:
                    q.append(nums[i])
                else:   # len(q) is 2:
                    if nums[i] > q[-1]:
                        return True
                    else:
                        q[-1] = nums[i]
                flag = min(nums[i], flag)

            elif nums[i] == q[0]:
                continue
            else:   #  nums[i] < hp[0]:
                q = [nums[i]]
                
        return False


def main():
    sol = Solution()
    nums = [20,100,10,12,5,13]
    print(sol.increasingTriplet(nums))


main()
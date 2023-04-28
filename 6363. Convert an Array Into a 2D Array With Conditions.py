''' 6363. Convert an Array Into a 2D Array With Conditions

User Accepted:1027
User Tried:1064
Total Accepted:1027
Total Submissions:1093
Difficulty:Medium
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

 

Example 1:

Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
Example 2:

Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= nums.length
Python3	
1
class Solution:
2
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

'''
# class Solution:
#     def fuc(self):
#         return -1

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = cnt0 = cnt1 = 0
        for c in s:
            if c == '0':
                if cnt1 == 0:
                    cnt0 += 1
                else:
                    res = max(res, 2 * min(cnt0, cnt1))
                    cnt0, cnt1 = 1, 0

            else:
                cnt1 += 1
                res = max(res, 2 * min(cnt0, cnt1))
        return res



def main():
    sol = Solution()

    # print(sol.fuc())
    s = "01000111"  # Output: 6
    print(sol.findTheLongestBalancedSubstring(s))

    s = "00111" # Output: 4
    print(sol.findTheLongestBalancedSubstring(s))

    s = "111"   # Output: 0
    print(sol.findTheLongestBalancedSubstring(s))

    s = "101"   # Output: 0
    print(sol.findTheLongestBalancedSubstring(s))

main()
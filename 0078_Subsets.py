''' 78. Subsets
Medium      12283       176     Add to List     Share
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:    1 <= nums.length <= 10
                -10 <= nums[i] <= 10
All the numbers of nums are unique.
Accepted:       1,264,464
Submissions:    1,717,686

'''

import copy

class Solution:
    def subsets(self, nums):
        n = len(nums)
        res = [[], [nums[0]]]
        if n == 1: return res
               
        for i in range(1, n):
            temp = copy.copy(res)
            print("1==============")            
            print("Temp =", temp, "\tRes =", res)
            print(       id(temp),        id(res))

            for j in range(len(res)):
                res[j].append(nums[i])
            print("2==============")
            print("Temp =", temp, "\tRes =", res)
            print(       id(temp),        id(res))

            res.extend(temp)
            print("3==============")
            print("Temp =", temp, "\tRes =", res)
            print(       id(temp),        id(res))
        
        return res

class Solution_v2:
    def subsets(self, nums):
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res.append(res[i]+[n])
        return res


def main():
    sol = Solution()
    # print(sol.subsets([1]))
    print(sol.subsets([1, 2]))
    ### solution 1 not work, due to,
    ### https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/amp/
    
    sol = Solution_v2()
    # print(sol.subsets([1]))
    print(sol.subsets([1, 2]))


main()

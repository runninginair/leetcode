''' 0046. Permutations
Medium      13019      220      Add to List     Share
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.


Example 1:
Input: nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

Example 2:
Input: nums = [0, 1]
Output: [[0, 1], [1, 0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:    1 <= nums.length <= 6
                -10 <= nums[i] <= 10
                All the integers of nums are unique.

Accepted:       1,358,094
Submissions:    1,826,268
'''

class Solution:     # Hyohou Lee's Solution
    def permutation(self, list):
        result = []
        self.helper(list, [], result)
        return result

    def helper(self, list, partial, result):
        if not list:
            return result.append(partial)
        # n = 1
        # print(" #", n, result)
        # n += 1
        for i in range(len(list)):
            self.helper(list[:i] + list[i+1:], partial + [list[i]], result)
        # print(" #", n, result)

class Solution_v2:  # Backtracking Algo     Time: O(n!)
    def permutation(self, nums):
        len_nums = len(nums)
        results = []

        def helper(nums, temp_res = []):
            if len(temp_res) == len_nums:   # Base Case
                # print(" WE ARE HERE:", temp_res)
                # print(" WE ARE HERE:", temp_res[:])
                results.append(temp_res[:])
                # print(" WE ARE HERE:", results)
            for num in nums:
                # print(" |-----> num =", num)
                temp = nums[:]
                # print(" # 1:", temp)
                temp_res.append(num)
                # print(" # 2:", temp_res)                
                temp.remove(num)
                # print(" # 3:", temp)
                helper(temp)            # WHY THIS helper() only one perameter ???
                temp.append(num)
                # print(" # 4:", temp)
                temp_res.remove(num)
                # print(" # 5:", temp_res)

        helper(nums)    
        return results

# V3 - https://www.youtube.com/watch?v=xqidNhvwKzI
class Solution_v3:  # Backtracking Algo     Time: O(n!)
    def permutation(self, nums):
        res = []
        self.dfs(res, nums, 0)   # Here 0 is the start (index 0) element we begin
        return res

    def dfs(self, res, nums, index):
        if index >= len(nums):                              # Base Case
            ans = []
            for i in range(len(nums)):
                ans.append(nums[i])
            res.append(ans)
            return

        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.dfs(res, nums, index + 1)
            nums[i], nums[index] = nums[index], nums[i]

def main():
    # sol = Solution()
    # sol = Solution_v2()
    sol = Solution_v3()


    print(sol.permutation([1]))
    print(sol.permutation([0, 1]))
    print(sol.permutation([1, 2, 3]))    
    # print(sol.permutation([1, 2, 3, 4]))    
    # print(sol.permutation([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    main()



'''
Backtracking recipe

void Backtrack(result, args)
    if (GOAL REACHED)
        add solution to result
        return
    
    for (int i = 0; i < NB_CHOICES; i ++)
        if (CHOICES[i] is valid)
            make choices[i]
            Backtrack(result, args)
            undo choices[i]

===========================================
// Backtrack 模板 【-等-价-于-> Topdown DFS】

Backtrack()
    1. Base Case
    2. For each possibility p
        a. Memorize current state   // 记录
        b. Backtrack(next_state)    // 递归
        c. Restore current state    // 回溯
'''
''' 491. Non-decreasing Subsequences

Medium      2.2K    176     Companies

Given an integer array nums, return all the different possible non-decreasing
subsequences of the given array with at least two elements.
You may return the answer in any order.


Example 1:
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:
Input: nums = [4,4,3,2,1]
Output: [[4,4]]
 

Constraints:        1 <= nums.length <= 15
                    -100 <= nums[i] <= 100
Accepted:           102.4K
Submissions:        186K
Acceptance Rate:    55.1%
'''


from typing import List


class Solution:     ### Solution Passed     T: O（2^n）
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n, res = len(nums), []
        if n < 2: return []
        def dfs(nums, curr) -> None:
            if len(curr) > 1 and curr not in res: res.append(curr.copy())
            for i, num in enumerate(nums[1:]):
                if num >= curr[-1]:
                    curr.append(num)
                    dfs(nums[i + 1:], curr)
                    curr.remove(num)
        for i in range(n - 1): dfs(nums[i:], [nums[i]])
        return res

class Solution_v2:     ### Solution Passed     T: O（2^n）
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums: List[int], curr: List[int]) -> None:
            if len(curr) > 1 and curr not in res: res.append(curr.copy())
            for i, num in enumerate(nums):
                if num >= curr[-1]:
                    curr.append(num)
                    dfs(nums[i + 1:], curr)
                    curr.remove(num)
        for i in range(len(nums) - 1): dfs(nums[i + 1:], [nums[i]])
        return res

class Solution_v2_2:     ### Solution Passed     T: O（2^n）
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(nums: List[int], curr: List[int]) -> None:
            if len(curr) > 1 : res.add(tuple(curr))
            for i, num in enumerate(nums):
                if num >= curr[-1]:
                    curr.append(num)
                    dfs(nums[i + 1:], curr)
                    curr.remove(num)
        for i in range(len(nums) - 1): dfs(nums[i + 1:], [nums[i]])
        return list(res)

class Solution_v3:  ### BackTrack
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # Use set to store different subsequences to avoid duplicates
        res = set()
        
        def BT(i, subsequence):
            nonlocal res
            
            # As long as there are at least two elements, we add it to our result.
            # Note that the subsequence is non-decreasing since we checked it while building.
            if len(subsequence) > 1: res.add(tuple(subsequence))
            
            # There are no more elements left to pick (no more state to generate), just return.
            if i == len(nums): return

            # Check to make sure the subsequence is non-decreasing if we want to pick the current element. 
            if not subsequence or nums[i] >= subsequence[-1]: BT(i+1, subsequence + [nums[i]])
                                                    # Note that this line is the same as:
                                                    # subsequence.append(nums[i])   #change the current state to its neighboring state
                                                    # BT(i+1, subsequence)          #backtrack(state)
                                                    # subsequence.pop()             #restore the state (backtrack)
            # Do not pick the current element.
            BT(i + 1, subsequence)
        
        BT(0, [])
        return res

class Solution_v4:     ### BackTrack
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        perm = []
        def dfs(i, prev):
            if i == len(nums):
                if len(perm) >= 2: res.add(tuple(perm))
                return
            dfs(i+1, prev)
            if nums[i] >= prev:
                perm.append(nums[i])
                dfs(i + 1, nums[i])
                perm.pop()
        
        dfs(0, float("-inf"))
        return list(res)

def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v2_2()
    sol = Solution_v3()
    sol = Solution_v4()

    nums = [0]          # Output: []
    print(sol.findSubsequences(nums))

    nums = [4,6,7,7]    # Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
    print(sol.findSubsequences(nums))

    nums = [4,4,3,2,1]  # Output: [[4,4]]
    print(sol.findSubsequences(nums))

if __name__ == "__main__":
    main()

''' 2389. Longest Subsequence With Limited Sum
Easy    399     51      Add to List     Share

You are given an integer array nums of length n, and an integer array queries
of length m.

Return an array answer of length m where answer[i] is the maximum size of a
subsequence that you can take from nums such that the sum of its elements is
less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.


Example 1:
Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven
    that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven
    that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven
    that 4 is the maximum size of such a subsequence, so answer[2] = 4.

Example 2:
Input: nums = [2,3,4,5], queries = [1]
Output: [0]
Explanation: The empty subsequence is the only subsequence that has a sum less
than or equal to 1, so answer[0] = 0.
 

Constraints:    n == nums.length
                m == queries.length
                1 <= n, m <= 1000
                1 <= nums[i], queries[i] <= 10^6
Accepted:       26,627
Submissions:    41,292

'''

from typing import List


class Solution:
    '''
    Runtime: 158 ms, faster than 86.46% of Python3 online.
    Memory Usage: 14.2 MB, less than 41.12% of Python3 online.
    '''
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        nums.sort()
        ans = [0 for _ in range(m)]
        for i in range(1, n): nums[i] += nums[i - 1]
        nums.append(float('inf'))

        q_i = [[0,0] for _ in range(m)]
        for i, num in enumerate(queries): q_i[i] = [num, i]
        q_i.sort()

        ptr = 0
        for query in q_i:
            while ptr < n + 1 and nums[ptr] <= query[0]:
                ptr += 1
            ans[query[1]] = ptr
        return ans

class Solution_v2:
    ''' Runtime: 107 ms, faster than 95.44% of Python3 online.
        Memory Usage: 14.1 MB, less than 81.47% of Python3
    '''
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ### T: O(n + m) * log(n + m)  M: O(n + m)
        n, m = len(nums), len(queries)
        nums.sort()
        for i in range(1, n): nums[i] += nums[i - 1]

        ans, ptr = [0 for _ in range(m)], 0
        queries_indexes = [[query, i]  for i, query in enumerate(queries)]
        queries_indexes.sort()

        for query in queries_indexes:
            while ptr < n and nums[ptr] <= query[0]: ptr += 1
            ans[query[1]] = ptr            
        return ans

class Solution_v3:  # LeetCode ID: shantilal3377
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)

        def getRes(sum: int) -> int:
            res = count = 0
            for i in range(n):
                if res + nums[i] <= sum:
                    res += nums[i]
                    count += 1
                else: return count
            return count

        res = [0 for _ in range(m)]
        nums.sort()
        for i in range(m): res[i] = getRes(queries[i])
        return res

def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()


    nums, queries = [4,5,2,1],  [3,10,21]
    print(sol.answerQueries(nums, queries)) # Output: [2,3,4]

    nums, queries = [2,3,4,5], [1]
    print(sol.answerQueries(nums, queries)) # Output: [0]

    nums, queries = [624082], [972985,564269,607119,693641,787608,46517,500857,140097]
    print(sol.answerQueries(nums, queries)) # Output: [1,0,0,1,1,0,0,0]


main()

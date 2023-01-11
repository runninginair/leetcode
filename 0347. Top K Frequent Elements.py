''' 347. Top K Frequent Elements
Medium      11727       431        Add to List      Share

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:    1 <= nums.length <= 10^5
                -104 <= nums[i] <= 10^4
                k is in the range [1, the number of unique elements in the array].
                It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Accepted:       1,220,180
Submissions:    1,883,161
'''

from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap Solution
        dic = {}
        for n in nums:
            if n in dic: dic[n] += 1
            else: dic[n] = 1

        h = []
        for key in dic:
            h.append([dic[key], key])

        res = heapq.nlargest(k, h)
        return [res[i][1] for i in range(k)]


def main():
    sol = Solution()
    nums, k = [1,1,1,2,2,3], 2     # Output: [1,2]
    print(sol.topKFrequent(nums, k))

    nums, k = [7,7,7,7,7,8,8,5], 2     # Output: [7,8]
    print(sol.topKFrequent(nums, k))

main()
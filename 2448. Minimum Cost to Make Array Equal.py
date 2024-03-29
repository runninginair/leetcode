''' 2448. Minimum Cost to Make Array Equal

Hard        714         11          Companies

You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.

 

Example 1:

Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.


Example 2:

Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.
 

Constraints:        n == nums.length == cost.length
                    1 <= n <= 10^5
                    1 <= nums[i], cost[i] <= 10^6
Accepted:           16K
Submissions:        42.5K
Acceptance Rate:    37.6%

'''

import math
from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)
        if min_num == max_num: return 0

        def getOffSet(key: int) -> int:
            res = 0
            for i in range(len(nums)):
                res += abs(nums[i] - key) * cost[i]
            return res
        
        mid = (min_num + max_num) >> 1
        while min_num < max_num:
            if getOffSet(mid) < getOffSet(mid + 1):
                max_num = mid
            else:
                min_num = mid + 1
            mid = (min_num + max_num) >> 1
        return getOffSet(mid)

def main():
    sol = Solution()

    nums, cost = [1,3,5,2], [2,3,1,14]     # Output: 8
    print(sol.minCost(nums, cost))

    nums, cost = [2,2,2,2,2], [4,2,8,1,3]  # Output: 0
    print(sol.minCost(nums, cost))


if __name__ == "__main__":
    main()
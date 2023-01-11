''' 6285. Maximal Score After Applying K Operations

User Accepted:675
User Tried:798
Total Accepted:682
Total Submissions:872
Difficulty:Medium

You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.

 

Example 1:

Input: nums = [10,10,10,10,10], k = 5
Output: 50
Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.
Example 2:

Input: nums = [1,10,3,3,3], k = 3
Output: 17
Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
The final score is 10 + 4 + 3 = 17.
 

Constraints:
1 <= nums.length, k <= 10^5
1 <= nums[i] <= 10^9
'''

import heapq
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        hp = [-num for num in nums]
        heapq.heapify(hp)
        while k > 0:
            temp = heapq.heappop(hp)
            ans -= temp
            temp //= 3
            heapq.heappush(hp, temp)
            k -= 1
        return ans



def main():
    sol = Solution()
    # sol = Solution_v2()

    nums, k = [10,10,10,10,10], 5      # Output: 50
    print(sol.maxKelements(nums, k))

    nums, k = [1,10,3,3,3], 3      # Output: 17
    print(sol.maxKelements(nums, k))


if __name__ == "__main__": main()
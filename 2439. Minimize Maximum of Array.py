''' 2439. Minimize Maximum of Array

Medium      674     127       Companies

You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

 * Choose an integer i such that 1 <= i < n and nums[i] > 0.
 * Decrease nums[i] by 1.
 * Increase nums[i - 1] by 1.

Return the minimum possible value of the maximum integer of nums after
performing any number of operations.


Example 1:
Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number
cannot be less than 5. Therefore, we return 5.

Example 2:
Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return
10.
 

Constraints:        n == nums.length
                    2 <= n <= 10^5
                    0 <= nums[i] <= 10^9
Accepted:           17.8K
Submissions:        44.7K
Acceptance Rate:    39.9%
'''


from typing import List


class Solution: ### NOT Correct.
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = total = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] >= res:
                total += nums[i]
                cnt += 1
            else:
                ave =  -(-total // cnt)
                res = max(res, ave)
                if ave * cnt > total:
                    total = nums[i] + ave - 1
                    cnt = 2
                else:
                    total = nums[i]
                    cnt = 1
            print(total, cnt, res)
        res = max(res, -(-total // cnt))
        return res


class Solution_v0:  ### Binary Search Approch.
    def minimizeArrayValue(self, nums: List[int]) -> int:
        left, right = nums[0], max(nums)
        while left < right:
            x = left + right >> 1
            buffer, flag = 0, True
            for num in nums:
                if num <= x:
                    buffer += (x - num)
                else:
                    buffer -= (num - x)
                    if buffer < 0:
                        flag = False
                        break
            if flag: right = x
            else: left = x + 1
        return left


class Solution_v1:  ### Greedy Approch.
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = cur = 0
        for i, num in enumerate(nums):
            cur += num
            val = -(-cur // (i + 1))
            ans = max(ans, val)
        return ans



def main():
    sol = Solution()
    sol = Solution_v0()
    sol = Solution_v1()


    nums = [13,13,20,0,8,9,9]               # Expect output: 16
    print(sol.minimizeArrayValue(nums))

    nums = [6,9,3,8,14]                     # Expect output: 8
    print(sol.minimizeArrayValue(nums))

    nums = [4,7,2,2,9,19,16,0,3,15]         # Expect output: 9
    print(sol.minimizeArrayValue(nums))


if __name__ == "__main__":
    main()

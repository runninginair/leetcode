''' 2527. Find Xor-Beauty of Array

Medium      141     34      Companies

You are given a 0-indexed integer array nums.

The effective value of three indices i, j, and k is defined as
((nums[i] | nums[j]) & nums[k]).

The xor-beauty of the array is the XORing of the effective values of all
the possible triplets of indices (i, j, k) where 0 <= i, j, k < n.

Return the xor-beauty of nums.

Note that:

val1 | val2 is bitwise OR of val1 and val2.
val1 & val2 is bitwise AND of val1 and val2.
 

Example 1:

Input: nums = [1,4]
Output: 5
Explanation: 
The triplets and their corresponding effective values are listed below:
- (0,0,0) with effective value ((1 | 1) & 1) = 1
- (0,0,1) with effective value ((1 | 1) & 4) = 0
- (0,1,0) with effective value ((1 | 4) & 1) = 1
- (0,1,1) with effective value ((1 | 4) & 4) = 4
- (1,0,0) with effective value ((4 | 1) & 1) = 1
- (1,0,1) with effective value ((4 | 1) & 4) = 4
- (1,1,0) with effective value ((4 | 4) & 1) = 0
- (1,1,1) with effective value ((4 | 4) & 4) = 4 
Xor-beauty of array will be bitwise XOR of all beauties = 1 ^ 0 ^ 1 ^ 4 ^ 1 ^ 4 ^ 0 ^ 4 = 5.
Example 2:

Input: nums = [15,45,20,2,34,35,5,44,32,30]
Output: 34
Explanation: The xor-beauty of the given array is 34.
 

Constraints:        1 <= nums.length <= 10^5
                    1 <= nums[i] <= 10^9
Accepted:           10.3K
Submissions:        15.4K
Acceptance Rate:    67.1%

'''


from typing import List


class Solution:     ### Time Limit Exceeded     29 / 32 testcases passed
    def xorBeauty(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    ans ^= ((nums[i] | nums[j]) & nums[k])
        return ans


class Solution_v1:     ### T: O(n)
    def xorBeauty(self, nums: List[int]) -> int:
        ans = 0
        for num in nums: ans ^= num
        return ans

from functools import reduce
from operator import xor

class Solution_v0:      ### LeetCode ID: xil899
    ''' Intuition

Many of you may get accepted during contest by guessing the answer
(the bitwise XOR of all num in nums). Here we provide a formal proof.

Key Observations:

Fully utilize the symmetry between i, j, k.
a ^ a = 0 (the property of bitwise XOR).

Proof:

First, note that by symmetry of i and j, we know that the value of

((nums[i] | nums[j]) & nums[k]) and ((nums[j] | nums[i]) & nums[k]) are equal.

Which then implies that for a pair of (i, j) where i != j, the bitwise XOR of

((nums[i] | nums[j]) & nums[k]) and ((nums[j] | nums[i]) & nums[k]) is 0.

Thus, we only need to deal with the triplets (i, j, k) where i == j.


Now we only need to consider the triplets (i, j, k) where i == j, so that

((nums[i] | nums[j]) & nums[k]) = ((nums[i] | nums[i]) & nums[k]) = nums[i] & nums[k].

By symmetry of i and k, we know that the value of nums[i] & nums[k] and nums[k] & nums[i] are equal.

Which then implies that for a pair of (i, k) where i != k, the bitwise XOR of nums[i] & nums[k] and nums[k] & nums[i] is 0.

Thus, we only need to deal with the case of i == k.


Therefore, we only need to consider the triplets (i, j, k) where i == j == k, and the final answer reduces to the bitwise XOR of ((nums[i] | nums[j]) & nums[k]) = ((nums[i] | nums[i]) & nums[i]) = nums[i].

Complexity:         Time complexity:    O(N)
                    Space complexity:   O(1)

    '''
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(xor, nums)  

def main():
    sol = Solution()
    sol = Solution_v0()
    sol = Solution_v1()

    nums = [1,4]    # Output: 5
    print(sol.xorBeauty(nums))

    nums = [15,45,20,2,34,35,5,44,32,30]    # Output: 34
    print(sol.xorBeauty(nums))

    # a = 1 ^ 0 ^ 1 ^ 4 ^ 1 ^ 4 ^ 0 ^ 4
    # print(a)

if __name__ == "__main__":
    main()

'''
LeetCode 454

454. 4Sum II
Medium      4101    120     Add to List     Share
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:
Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
Accepted:       270,557
Submissions:    472,301
'''

from itertools import count


class Solution:
    # def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        n = len(nums1)
        res = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0: 
                            res += 1
        return res

class Solution2:
    def fourSumCount(self, A, B, C, D) -> int:
        count = 0
        dic = dict()
        
        for a in A:
            for b in B:
                if a + b in dic:
                    dic[a + b] += 1
                else:
                    dic[a + b] = 1
        
        for c in C:
            for d in D:
                t = -(c + d)
                if t in dic:
                    count += dic[t]

        return count

def main():
    sol = Solution()
    sol = Solution2()

    n1 = [ 0,  1, -1]
    n2 = [-1,  1,  0]
    n3 = [ 0,  0,  1]
    n4 = [-1,  1,  1]
    print(sol.fourSumCount(n1, n2, n3, n4))     # Output: 17

    n1 = [ -1, -1]
    n2 = [  1,  1]
    n3 = [  0,  0]
    n4 = [  0,  0]
    print(sol.fourSumCount(n1, n2, n3, n4))     # Output: 16

    n1 = [ 1,  2]
    n2 = [-2, -1]
    n3 = [-1,  2]
    n4 = [ 0,  2]
    print(sol.fourSumCount(n1, n2, n3, n4))     # Output: 2

    n1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    n2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    n3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    n4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(sol.fourSumCount(n1, n2, n3, n4))     # Output: 130321


main()

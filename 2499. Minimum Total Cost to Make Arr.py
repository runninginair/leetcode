''' 2499. Minimum Total Cost to Make Arrays Unequal
Hard    97     4    Companies

You are given two 0-indexed integer arrays nums1 and nums2, of equal length n.

In one operation, you can swap the values of any two indices of nums1. The cost
of this operation is the sum of the indices.

Find the minimum total cost of performing the given operation any number of times
such that nums1[i] != nums2[i] for all 0 <= i <= n - 1 after performing all the operations.

Return the minimum total cost such that nums1 and nums2 satisfy the above condition.
In case it is not possible, return -1.


Example 1:

Input: nums1 = [1,2,3,4,5], nums2 = [1,2,3,4,5]
Output: 10
Explanation: 
One of the ways we can perform the operations is:
- Swap values at indices 0 and 3, incurring cost = 0 + 3 = 3. Now, nums1 = [4,2,3,1,5]
- Swap values at indices 1 and 2, incurring cost = 1 + 2 = 3. Now, nums1 = [4,3,2,1,5].
- Swap values at indices 0 and 4, incurring cost = 0 + 4 = 4. Now, nums1 =[5,3,2,1,4].
We can see that for each index i, nums1[i] != nums2[i]. The cost required here is 10.
Note that there are other ways to swap values, but it can be proven that it is not
possible to obtain a cost less than 10.

Example 2:

Input: nums1 = [2,2,2,1,3], nums2 = [1,2,2,3,3]
Output: 10
Explanation: 
One of the ways we can perform the operations is:
- Swap values at indices 2 and 3, incurring cost = 2 + 3 = 5. Now, nums1 = [2,2,1,2,3].
- Swap values at indices 1 and 4, incurring cost = 1 + 4 = 5. Now, nums1 = [2,3,1,2,2].
The total cost needed here is 10, which is the minimum possible.

Example 3:

Input: nums1 = [1,2,2], nums2 = [1,2,2]
Output: -1
Explanation: 
It can be shown that it is not possible to satisfy the given conditions irrespective of
the number of operations we perform.
Hence, we return -1.
 

Constraints:        n == nums1.length == nums2.length
                    1 <= n <= 105
                    1 <= nums1[i], nums2[i] <= n
Accepted:           1.7K
Submissions:        4K
Acceptance Rate:    42.0%
'''

from typing import Counter, List

class Solution: ### My Solution
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n, sameTrace = len(nums1), []
        alpa1 = alpa2 = '_'
        dic1, dic2 = {}, {}
        for i in range(n):
            if nums1[i] in dic1: 
                dic1[nums1[i]] += 1
                if dic1[nums1[i]] > (n >> 1):
                    alpa1 = nums1[i]

            else: dic1[nums1[i]] = 1

            if nums2[i] in dic2:
                dic2[nums2[i]] += 1
                if dic2[nums2[i]] > (n >> 1):
                    alpa2 = nums1[i]

            else: dic2[nums2[i]] = 1

            if nums1[i] == nums2[i]: sameTrace.append(i)
        if alpa1 != '_' and alpa1 == alpa2: return -1
        else: 
            
            return sum(sameTrace), sameTrace


class Solution_v1:  ### LeetCode ID: IamVaibhave53  C++ Time complexity: O(n)  Space complexity: O(n)
    ''' Approach
    1. Lets call an index bad is nums1[index] = nums2[index]. Imagine this, 
        you collect all "bad indexes" in the 0th index. The cost to move this
        index to the 0th index is the index of the element.
    
    2. Now, you can use these collected indexes and distribute them to the
        desired positions. (note that we don't have to add any extra cost here,
        we can assume that once an element has come to position 0, it is free to move)

    3. The only thing to care is the case where the maximum occuring element
        occurs more than half the values. In this case we need to collect more
        indexes even though they aren't "bad".
    
    4. We want to collect indexes which contribute less cost, i.e which occur
        earlier (smallest index) as well as taking care that the value doesn't
        equal to the max occuring element (worsening our situation) and also
        ensuring that nums2[index] != max occurent element
    '''
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n, freq = len(nums1), {}
        ans = maxFrequency = maxFrequencyValue = toSwap = 0

        for i in range(n):
            if nums1[i] == nums2[i]:
                toSwap += 1
                ans += i

                if nums1[i] in freq: freq[nums1[i]] += 1
                else: freq[nums1[i]] = 1

                if freq[nums1[i]] > maxFrequency:
                    maxFrequencyValue = nums1[i]
                    maxFrequency = freq[nums1[i]]
        # print(ans, maxFrequency, maxFrequencyValue, toSwap)
        for i in range(n):
            if (maxFrequency > (toSwap >> 1) and nums1[i] != nums2[i] and
                nums1[i] != maxFrequencyValue and nums2[i] != maxFrequencyValue):
                ans += i
                toSwap += 1
        # print(ans, maxFrequency, maxFrequencyValue, toSwap)
        if maxFrequency > (toSwap >> 1): return -1

        return ans


class Solution_v2:  ### LeetCode ID: koder_786  Time complexity: O(n)   Space complexity: O(n)
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        z = Counter(nums1)
        z1 = Counter(nums2)
        for i in z:
            if(z[i] >= n // 2 + 1 and z1[i] >= n // 2 + 1):
                return -1
        z = Counter([])
        ans = 0
        for i in range(n):
            if(nums1[i] == nums2[i]):
                z[nums2[i]] += 1
                ans += i

        l = z.most_common(len(z))
        a = 0
        for i in range(1,len(l)):
            a += l[i][1]
        if(l and a >= l[0][1]):
            return ans
        x = 0
        if l:
            x = l[0][1] - a
        for i in range(n):
            if(z[nums1[i]] == 0 and x):
                if(ans):
                    ans += i
                    x -= 1
        return ans

def main():
    sol = Solution()
    sol = Solution_v1()
    # sol = Solution_v2()

    # nums1, nums2 = [1,2,3,4,5], [1,2,3,4,5]         # Output: 10
    # print(sol.minimumTotalCost(nums1, nums2))

    # nums1, nums2 = [2,2,2,1,3], [1,2,2,3,3]         # Output: 10
    # print(sol.minimumTotalCost(nums1, nums2))

    # nums1, nums2 = [1,2,2], [1,2,2]                 # Output: -1
    # print(sol.minimumTotalCost(nums1, nums2))

    # nums1, nums2 = [1,2,6,2,9], [1,2,9,2,6]         # Output: 6
    # print(sol.minimumTotalCost(nums1, nums2))

    # nums1, nums2 = [1,2,6,3,9], [1,2,9,3,6]         # Output: 4
    # print(sol.minimumTotalCost(nums1, nums2))    

    nums1, nums2 = [2,1,2,6,2,9], [2,1,2,9,2,6]         # Output: 15
    print(sol.minimumTotalCost(nums1, nums2))

main()

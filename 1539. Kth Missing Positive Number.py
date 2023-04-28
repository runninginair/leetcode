''' 1539. Kth Missing Positive Number

Easy        4.1K        287         Companies

Given an array arr of positive integers sorted in a strictly increasing order,
and an integer k.

Return the k-th positive integer that is missing from this array.


Example 1:
Input: arr = [2, 3, 4, 7, 11], k = 5
Output: 9
Explanation: The missing positive integers are [1, 5, 6, 8, 9, 10, 12, 13, ...].
The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5, 6, 7, ...].
The 2nd missing positive integer is 6.
 

Constraints:        1 <= arr.length <= 1000
                    1 <= arr[i] <= 1000
                    1 <= k <= 1000
                    arr[i] < arr[j] for 1 <= i < j <= arr.length

Follow up:          Could you solve this problem in less than O(n) complexity?

Accepted:           239.3K
Submissions:        418.3K
Acceptance Rate:    57.2%
'''

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cur, cntMiss, missed = 1, 0, 0
        for a in arr: 
            if a > cur:
                cntMiss += a - cur
                if cntMiss >= k:
                    return cur - 1 - missed + k
                missed = cntMiss
                cur = a
            cur += 1
        return cur - 1 - cntMiss + k


def main():
    sol = Solution()

    arr, k = [2, 3, 4, 7, 11], 5   # Output: 9

    print(sol.findKthPositive(arr, k))

    arr, k = [1, 2, 3, 4], 2      # Output: 6
    print(sol.findKthPositive(arr, k))

    arr, k = [15], 6      # Output: 6
    print(sol.findKthPositive(arr, k))

    arr, k = [2, 15], 6      # Output: 7
    print(sol.findKthPositive(arr, k))

    arr, k = [2, 4, 6, 15], 6      # Output: 9
    print(sol.findKthPositive(arr, k))

if __name__ == "__main__":
    main()

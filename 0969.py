'''
969. Pancake Sorting
Medium

1187

1304

Add to List

Share
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[0...k-1] (0-indexed).
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

 

Example 1:

Input: arr = [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k = 4): arr = [1, 4, 2, 3]
After 2nd flip (k = 2): arr = [4, 1, 2, 3]
After 3rd flip (k = 4): arr = [3, 2, 1, 4]
After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
Example 2:

Input: arr = [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
 

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= arr.length
All integers in arr are unique (i.e. arr is a permutation of the integers from 1 to arr.length).
Accepted
78,026
Submissions
111,520
'''


from re import A


class Solution:
    # def pancakeSort(self, arr: List[int]) -> List[int]:
    def pancakeSort(self, arr):
        n = len(arr)
        res = []
        if n <= 1: return res

        def reverse(lo, hi):
            print("Before REV:", arr)
            while(lo < hi):
                arr[lo], arr[hi] = arr[hi], arr[lo]
                lo += 1
                hi -= 1
            print("After REV:", arr)
            print()


        for i in range(n-1, 0, -1):
            indexOfMax = 0
            max = arr[0]

            for j in range(0, i + 1):
                if arr[j] > max:
                    max = arr[j]
                    indexOfMax = j
            reverse(0, indexOfMax)
            if indexOfMax != 0:
                res.append(indexOfMax + 1)
            reverse(0, i)
            res.append(i + 1)

        return res

def main():
    sol = Solution()
    arr = [3, 2, 4, 1]
    print(sol.pancakeSort(arr))

main()

''' 658. Find K Closest Elements
Medium      5423       475      Add to List     Share
Given a sorted integer array arr, two integers k and x, return the k closest
integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:    1 <= k <= arr.length
                1 <= arr.length <= 104
                arr is sorted in ascending order.
                -10^4 <= arr[i], x <= 10^4
Accepted:       343,571
Submissions:    751,793
'''

class Solution:
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    def findClosestElements(self, arr, k: int, x: int):

        n = len(arr)
        # Use binary search find the index of x, if not exist, return the clostest one.
        def binarySearch():
            mi = 0
            lo, hi = 0, n-1
            while (lo < hi):
                mi = (lo + hi)//2
                if arr[mi] == x:
                    return mi
                elif arr[mi] < x:
                    lo = mi + 1
                else:
                    hi = mi - 1
            return lo

        mi = binarySearch()
        print("mid =", mi)
        if k == 1: return [arr[mi]]

        # Using a sliding window to fillter the propoerly result.
        if k % 2 == 0: p1, p2 = mi - k//2, mi + k//2 - 1
        else: p1, p2 = mi - k//2, mi + k//2
        print("p1, p2 =", p1, p2)
        
        if p1 < 0: p1, p2 = 0, p2 - p1
        if p2 >= n: p1, p2 = p1-(p2-n+1), n-1
        print("p1, p2 =", p1, p2)
        
        d1, d2 = abs(arr[p1] - x), abs(arr[p2] - x)
        print("d1, d2 =", d1, d2)        

        while d1 > d2 and p2 < n - 1:
            p1 += 1
            p2 += 1
            d1, d2 = abs(arr[p1] - x), abs(arr[p2] - x)

        while d1 <= d2 and p1 > 0:
            p1 -= 1
            p2 -= 1
            d1, d2 = abs(arr[p1] - x), abs(arr[p2] - x)

        return arr[p1: p2+1]

def main():
    sol = Solution()
    # arr, k, x = [1,2,3,4,5], 4, 3   # Output: [1,2,3,4]
    # print(sol.findClosestElements(arr, k, x))

    # arr, k, x = [1,2,3,4,5], 4, -1   # Output: [1,2,3,4]
    # print(sol.findClosestElements(arr, k, x))

    arr, k, x = [0,0,0,1,3,5,6,7,8,8], 2, 2
    print(sol.findClosestElements(arr, k, x))


main()

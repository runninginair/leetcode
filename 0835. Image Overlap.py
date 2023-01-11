''' 835. Image Overlap
Medium      178     57      Add to List     Share

You are given two images, img1 and img2, represented as binary, square matrices
of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right,
up, and/or down any number of units. We then place it on top of the other image.
We can then calculate the overlap by counting the number of positions that have
a 1 in both images.

Note also that a translation does not include any kind of rotation.
Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.
 

Example 1:
Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.
The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:
Input: img1 = [[1]], img2 = [[1]]
Output: 1

Example 3:
Input: img1 = [[0]], img2 = [[0]]
Output: 0

Constraints:    n == img1.length == img1[i].length
                n == img2.length == img2[i].length
                1 <= n <= 30
                img1[i][j] is either 0 or 1.
                img2[i][j] is either 0 or 1.
Accepted:       49,319
Submissions:    80,781
'''

import collections

class Solution:
    def largestOverlap(self, A, B) -> int:
        A_points, B_points, d = [], [], collections.defaultdict(int)

        # Filter points having 1 for each matrix respectively.
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c]:
                    A_points.append((r, c))

                if B[r][c]:
                    B_points.append((r, c))
 
        # For every point in filtered A, calculate the
        # linear transformation vector with all points of filtered B
        # count the number of the pairs that have the same transformation vector
        for r_a, c_a in A_points:
            for r_b, c_b in B_points:
                d[(r_b - r_a, c_b - c_a)] += 1

        return max(d.values() or [0])

class Solution_v2: # Brute Force
    def largestOverlap(self, img1, img2) -> int:
        n, ans = len(img1), 0
        img3 = [[0 for _ in range(3*n)] for _ in range(3*n)]
        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    img3[i+n][j+n] = 1

        for x in range(1, 2*n - 1):
            for y in range(1, 2*n - 1):
                res = 0
                for i in range(n):
                    for j in range(n):
                        if img1[i][j] == 1 and img3[i+x][j+y] == 1:
                            res += 1
                ans = max(ans, res)
                
        return ans


def main():
    sol = Solution_v2()

    # img1, img2 = [[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]    # Output: 3
    # print(sol.largestOverlap(img1, img2))

    img1, img2 = [[0,1],[1,1]], [[1,1],[1,1]]
    print(sol.largestOverlap(img1, img2))

    img1 = [[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    img2 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0]]
    print(sol.largestOverlap(img1, img2))


main()

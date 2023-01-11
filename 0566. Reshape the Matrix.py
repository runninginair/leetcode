''' 566. Reshape the Matrix
Easy    2871    323     Add to List     Share

In MATLAB, there is a handy function called reshape which can reshape an m x n
matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the
number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original
matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal,
output the new reshaped matrix; Otherwise, output the original matrix.


Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
 

Constraints:        m == mat.length
                    n == mat[i].length
                    1 <= m, n <= 100
                    -1000 <= mat[i][j] <= 1000
                    1 <= r, c <= 300
Accepted:       304,683
Submissions:    486,005

'''

from typing import List


class Solution: # 09:55pm 11/26/2022
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n > r * c or (r >= m and c >= n): return mat
        ans = [[0 for _ in range(c)] for _ in range(r)]

        p = q = 0
        for i in range(m):
            for j in range(n):
                ans[p][q] = mat[i][j]
                q += 1
                if q == c:
                    p += 1
                    q = 0
        return ans


def main():
    sol = Solution()
    mat, r, c = [[1,2],[3,4]], 1, 4   # Output: [[1,2,3,4]]
    print(sol.matrixReshape(mat, r, c))

    mat, r, c = [[1,2],[3,4]], 2, 4   # Output: [[1,2], [3,4]]
    print(sol.matrixReshape(mat, r, c))    

main()

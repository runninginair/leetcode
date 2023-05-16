''' 54. Spiral Matrix

Medium      11.3K       1K      Companies

Given an m x n matrix, return all elements of the matrix in spiral order.


Example 1:

Input: matrix = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]


Example 2:

Input: matrix = [[1,  2,  3,  4],
                 [5,  6,  7,  8],
                 [9, 10, 11, 12]]

Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
 

Constraints:            m == matrix.length
                        n == matrix[i].length
                        1 <= m, n <= 10
                        -100 <= matrix[i][j] <= 100
Accepted:               1M
Submissions:            2.3M
Acceptance Rate:        45.3%
'''

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = list()

        def _spiralOrder(x, y, cnt) -> None:
            while cnt:
                while y + 1 < n and matrix[x][y + 1] < 101:
                    ans.append(matrix[x][y + 1])
                    matrix[x][y + 1] = 101
                    y += 1
                    cnt -= 1
                while x + 1 < m and matrix[x + 1][y] < 101:
                    ans.append(matrix[x + 1][y])
                    matrix[x + 1][y] = 101
                    x += 1
                    cnt -= 1
                while y - 1 >= 0 and matrix[x][y - 1] < 101:
                    ans.append(matrix[x][y - 1])
                    matrix[x][y - 1] = 101
                    y -= 1
                    cnt -= 1
                while matrix[x - 1][y] < 101:
                    ans.append(matrix[x - 1][y])
                    matrix[x - 1][y] = 101
                    x -= 1
                    cnt -= 1                

        _spiralOrder(0, -1, m * n)
        return ans

class Solution_v2:
    def spiralOrder(self, matrix):
        ans = [x for x in matrix[0]]
        matX, matY = len(matrix[0]), len(matrix)
        while len(ans) < matX * matY:
            matrix = self.rotate(matrix[1:])
            # for m in matrix: print(m)
            ans += [x for x in matrix[0]]
        return ans

    def rotate(self, matrix):
        rotated = []
        for i in range(len(matrix[0]), 0, -1):            
            rotated.append([matrix[j][i - 1] for j in range(len(matrix))])
        return rotated

def main():
    sol = Solution()
    # sol = Solution_v2()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(sol.spiralOrder(matrix))

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    print(sol.spiralOrder(matrix))

if __name__ == "__main__":
    main()

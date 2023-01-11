''' 74. Search a 2D Matrix
Medium      9827       306      Add to List     Share
Write an efficient algorithm that searches for a value target in an m x n
integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:    m == matrix.length
                n == matrix[i].length
                1 <= m, n <= 100
                -10^4 <= matrix[i][j], target <= 10^4
Accepted:       994,272
Submissions:    2,134,726
'''

class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 1, m*n 
        
        while lo < hi:
            mid = (lo + hi) // 2
            # 6 -> [1][1]   (6 - 1)//4, (6-1)%4
            # 5 -> [1][0]   (5-1)//4, 
            # 4 -> [0][3]
            x = (mid - 1) // n
            y = (mid - 1) % n
            if matrix[x][y] == target:
                print("mid, matrix[x][y], x, y = ", mid, matrix[x][y], x, y)
                return True
            elif matrix[x][y] < target:
                print("mid, matrix[x][y], x, y = ",mid, matrix[x][y], x, y)
                lo = mid + 1
            else:
                print("mid, matrix[x][y], x, y = ",mid, matrix[x][y], x, y)
                hi = mid
        return False

def main():
    sol = Solution()
    matrix, target = [[1,3,5,7],[10,11,16,20],[23,30,34,60]],  3    # Output: true
    print(sol.searchMatrix(matrix, target))

main()

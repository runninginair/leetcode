''' 1886. Determine Whether Matrix Can Be Obtained By Rotation
Easy    953     81      Add to List     Share

Given two n x n binary matrices mat and target, return true if it is possible
to make mat equal to target by rotating mat in 90-degree increments, or false
otherwise.


Example 1:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
 

Constraints:    n == mat.length == target.length
                n == mat[i].length == target[i].length
                1 <= n <= 10
                mat[i][j] and target[i][j] are either 0 or 1.
Accepted:       44,366
Submissions:    80,216
'''

class Solution:
    def findRotation(self, mat, target) -> bool:
        def Rotation(mat):
            n = len(mat)
            if n == 1: return mat
            
            for i in range(n >> 1):
                for j in range(i, n - i - 1):
                    temp = mat[i][j]
                    mat[i][j] = mat[n-1-j][i]
                    mat[n-1-j][i] = mat[n-1-i][n-1-j]
                    mat[n-1-i][n-1-j] = mat[j][n-1-i]
                    mat[j][n-1-i] = temp

        for _ in range(4):
            Rotation(mat)
            if mat == target: return True
        return False

def main():
    sol = Solution()
    mat, target = [[0,1],[1,0]], [[1,0],[0,1]] # Output: true
    print(sol.findRotation(mat, target))

    mat, target = [[0,1],[1,1]],  [[1,0],[0,1]] # Output: false
    print(sol.findRotation(mat, target))

    mat, target = [[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]] # Output: true    
    print(sol.findRotation(mat, target))


main()

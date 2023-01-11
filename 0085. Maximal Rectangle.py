''' 85. Maximal Rectangle
Hard    7872    127     Add to List     Share

Given a rows x cols binary matrix filled with 0's and 1's, find the largest
rectangle containing only 1's and return its area.


Example 1:
Input: matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:    rows == matrix.length
                cols == matrix[i].length
                1 <= row, cols <= 200
                matrix[i][j] is '0' or '1'.
Accepted:       325,556
Submissions:    736,757
'''

from typing import List


class Solution:     # dp solution
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        maxArea = 0
        dp = [0 for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                dp[j] = 0 if matrix[i][j] == '0' else dp[j] + 1
            # print("dp:", dp)
            maxArea = max(maxArea, self.getRowMaxArea(dp))
        return maxArea

# dp:   1   0   4   2   3   1   0
# Area: 1   0   4   4   6   4   0      
# Idx:  0   1   2   3   4   5   6

    def getRowMaxArea(self, heights):
        stack, ans = [], 0
        # n = 1
        for i, height in enumerate(heights + [0]):
            # print(heights + [0], "  i:", i, "  height:", height)
            while stack and heights[stack[-1]] >= height:
                H = heights[stack.pop()]
                W = i if not stack else i - stack[-1] - 1
                ans = max(ans, H * W)
                # print('H:', H, '\tW:', W, "\tans =", ans)
            stack.append(i)
            # print("#", n, " stack:", stack, end="\n\n")
            # n += 1
        return ans

def main():
    sol = Solution()
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]    # Output: 6
    print(sol.maximalRectangle(matrix))

    # dp = [3, 1, 3, 2, 2]
    # print(sol.getRowMaxArea(dp))

main()

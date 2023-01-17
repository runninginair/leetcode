''' 2536. Increment Submatrices by One
    6292. Increment Submatrices by One

User Accepted:1798
User Tried:4284
Total Accepted:1810
Total Submissions:5051
Difficulty:Medium

You are given a positive integer n, indicating that we initially have an n x n
0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query.
For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

Add 1 to every element in the submatrix with the top left corner (row1i, col1i)
and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for for
all row1i <= x <= row2i and col1i <= y <= col2i.

Return the matrix mat after performing every query.


Example 1:
Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).

Example 2:
Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
Explanation: The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
 

Constraints:    1 <= n <= 500
                1 <= queries.length <= 10^4
                0 <= row1i <= row2i < n
                0 <= col1i <= col2i < n

'''

from typing import List


class Solution:         ### Naïve Approach
    ''' Naïve Approach
    Following the description of this problem, for each query, we update the every element covered in the submatrix defined by (r1, c1) and (r2, c2). However, it is pretty clear to know that the time complexity for this approach is O((n^2)*q), which could be up to 500 * 500 * 10^4 = 2.5 * 10^9 and result in TLE.
    '''
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    res[r][c] += 1
        return res

class Solution_v2:      ### Range Caching Solution
    ''' Range Caching Solution Approach
    For each query, denoted as (r1, c1, r2, c2), we perform a preprocessing (range caching) on each row involved. Specifically, for each row within [r1, r2], we add 1 at column c1 and subtract 1 at the next column of c2.

    After preprocessing, we calculate the output by performing range addition (sweeping line) on all elements of the matrix, and output the answer.

    Complexity
    Time complexity: O(nq)O(n^2 + nq) approx to O(nq), if q ≫ n;
    Space complexity: O(1), if not including the O(n^2) space for output.
    '''
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                ans[r][c1] += 1
                if c2 + 1 < n: ans[r][c2 + 1] -= 1
        print(ans)
        for r in range(n):
            for c in range(1, n):
                ans[r][c] += ans[r][c - 1]
        return ans

class Solution_v3:      ### 2D Range Caching Solution
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            ans[r1][c1] += 1
            if c2 < n - 1: ans[r1][c2 + 1] -= 1
            if r2 < n - 1: ans[r2 + 1][c1] -= 1
            if c2 < n - 1 and r2 < n - 1: ans[r2 + 1][c2 + 1] += 1

        for r in range(n):
            for c in range(1, n): ans[r][c] += ans[r][c - 1]
        
        for c in range(n):
            for r in range(1, n): ans[r][c] += ans[r - 1][c]

        return ans

class Solution_v4:      ### 2D Range Caching with extra + n space Solution
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans = [[0] * (n + 1) for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            ans[r1][c1] += 1
            ans[r1][c2 + 1] -= 1
            ans[r2 + 1][c1] -= 1
            ans[r2 + 1][c2 + 1] += 1

        for r in range(n):
            for c in range(1, n): ans[r][c] += ans[r][c - 1]
        
        for c in range(n):
            for r in range(1, n): ans[r][c] += ans[r - 1][c]

        return [ans[r][:n] for r in range(n)]

def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()
    sol = Solution_v4()


    n, queries = 3, [[1,1,2,2],[0,0,1,1]]
    print(sol.rangeAddQueries(n, queries))
    # Expect Output: [[1,1,0],[1,2,1],[0,1,1]]

    n, queries = 2, [[0,0,1,1]]     # Expect Output: [[1,1],[1,1]]
    print(sol.rangeAddQueries(n, queries))

    # n, queries = 13, [[3,1,7,3],[7,5,7,8],[4,12,6,12],[2,8,6,11],[9,11,10,11],[9,3,11,11],[0,12,10,12],[10,5,11,12],[4,7,6,12],[0,2,9,6],[12,7,12,11],[2,7,3,8],[2,9,6,12],[10,7,10,12],[11,6,11,7],[3,2,12,9]]
    # print(sol.rangeAddQueries(n, queries))
    ### Expect: [[0,0,1,1,1,1,1,0,0,0,0,0,1],
    #            [0,0,1,1,1,1,1,0,0,0,0,0,1],
    #            [0,0,1,1,1,1,1,1,2,2,2,2,2],
    #            [0,1,3,3,2,2,2,2,3,3,2,2,2],
    #            [0,1,3,3,2,2,2,2,3,4,3,3,4],
    #            [0,1,3,3,2,2,2,2,3,4,3,3,4],
    #            [0,1,3,3,2,2,2,2,3,4,3,3,4],
    #            [0,1,3,3,2,3,3,2,2,1,0,0,1],
    #            [0,0,2,2,2,2,2,1,1,1,0,0,1],
    #            [0,0,2,3,3,3,3,2,2,2,1,2,1],
    #            [0,0,1,2,2,3,3,4,4,4,3,4,3],
    #            [0,0,1,2,2,3,4,4,3,3,2,2,1],
    #            [0,0,1,1,1,1,1,2,2,2,1,1,0]]

if __name__ == "__main__":
    main()

''' 0000_Netflix_OA2_Question_4

2023 Summer Netflix Bootcamp OA2 CodeSignal

Give a grid with "rows" and "cols", and a two-dementional integer array "blacks".
considering the 2 rows * 2 cols as a mini box, please count the number of black
cells in each mini box and add (update) the total number in the result.

The result is an integer array with length of 5, such as [0, 0, 0, 0, 0]

For example:

rows = 3, cols = 3, blacks = [[0,0], [0,1], [1,0]]
output: [1, 2, 0, 1, 0]

Explaination: 

we use 1 stands for black cell. 0 stands for white one.
[[1, 1, 0],
 [1, 0, 0],
 [0, 0, 0]]

step 1: mini box grid[0:2][0:2] 
[[1, 1],
 [1, 0]]    contains three black cells, so we update the result[3] by adding 1,
 such as [0, 0, 0, 1, 0]

step 2: mini box grid[0:2][1:3] 
[[1, 0],
 [0, 0]]    contains one black cells, so we update the result[1] as [0, 1, 0, 1, 0]

step 3: mini box grid[1:3][0:2] 
[[1, 0],
 [0, 0]]    contains one black cells, so we update the result[1] as [0, 2, 0, 1, 0]

step 4: mini box grid[1:3][1:3] 
[[0, 0],
 [0, 0]]    contains zero black cells, so we update the result[0] as [1, 2, 0, 1, 0]

Then, we got the final result as [1, 2, 0, 1, 0]


Example 2:

rows = 3, cols = 4, blacks = [[1,2], [1,3], [2,2], [2,3]]
output: [2, 1, 2, 0, 1]

Explaination: 

we use 1 stands for black cell. 0 stands for white one.
[[0, 0, 0, 0],
 [0, 0, 1, 1],
 [0, 0, 1, 1]]


constrains:         2 <= rows, cols <= 500,
                    blacks.length() <= 500,

'''

from typing import List

class Solution:     ### T: O(rows * cols) => O(n^2)   M: O(rows * cols) => O(n^2) 
    def countBlackBox(self, rows: int, cols: int, blacks: List[int]) -> List[int]:
        ### Start your code here.
        res = [0 for _ in range(5)]
        map = [[0 for _ in range(cols)] for _ in range(rows)]
        for x, y in blacks:
            map[x][y] = 1
        for i in range(rows - 1):
            for j in range(cols - 1):
                cnt = map[i][j] + map[i][j+1] + map[i+1][j] + map[i+1][j+1]
                res[cnt] += 1
        return res


class Solution_v2:  ### T: O(blacks.length()) => O(n)   M: O(rows * cols) => O(n^2) 
    def countBlackBox(self, rows: int, cols: int, blacks: List[int]) -> List[int]:
        map = [[0 for _ in range(cols)] for _ in range(rows)]
        res = [(rows - 1) * (cols - 1), 0, 0, 0, 0]
        def explore(x, y):
            if  0 <= x-1 and 0 <= y-1:
                cntBlk =  map[x-1][y-1] + map[x][y-1] + map[x-1][y]
                res[cntBlk] -= 1
                res[cntBlk + 1] += 1
            if 0 <= x-1 and y+1 < cols:
                cntBlk = map[x-1][y+1] + map[x][y+1] + map[x-1][y]
                res[cntBlk] -= 1
                res[cntBlk + 1] += 1
            if x+1 < rows and y-1 >= 0:
                cntBlk = map[x+1][y-1] + map[x][y-1] + map[x+1][y]
                res[cntBlk] -= 1
                res[cntBlk + 1] += 1
            if x+1 < rows and y+1 < cols:
                cntBlk = map[x+1][y+1] + map[x][y+1] + map[x+1][y]
                res[cntBlk] -= 1
                res[cntBlk + 1] += 1
        for x, y in blacks:
            map[x][y] = 1
            explore(x, y)
        return res



def main():
    sol = Solution()
    sol = Solution_v2()


    rows = 3
    cols = 3
    blacks = [[0,0], [0,1], [1,0]]
    print(sol.countBlackBox(rows, cols, blacks))    
    # Expect output: [1, 2, 0, 1, 0]


    rows = 3
    cols = 4
    blacks = [[1,2], [1,3], [2,2], [2,3]]
    print(sol.countBlackBox(rows, cols, blacks))
    # Expect output: [2, 1, 2, 0, 1]


main()
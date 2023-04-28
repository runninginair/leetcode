''' 6322. Check Knight Tour Configuration

'''

from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        que = []
        for i in range(n):
            for j in range(n):
                que.append([grid[i][j], [i, j]])
        que.sort()
        print(que)

        return True

def main():
    sol = Solution()

    grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
    # Output: true

    print(sol.checkValidGrid(grid))



main()

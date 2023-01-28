''' 909. Snakes and Ladders

Medium      1.4K      370      Companies

You are given an n x n integer matrix board where the cells are labeled from
1 to n^2 in a Boustrophedon style starting from the bottom left of the board
(i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr,
do the following:

 * Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n^2)].
    * This choice simulates the result of a standard 6-sided die roll: i.e.,
      there are always at most 6 destinations, regardless of the size of the board.
 * If next has a snake or ladder, you must move to the destination of that snake or ladder.
   Otherwise, you move to next.
 * The game ends when you reach the square n^2.

A board square on row r and column c has a snake or ladder if board[r][c] != -1.
The destination of that snake or ladder is board[r][c].
Squares 1 and n^2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move.
If the destination to a snake or ladder is the start of another snake or ladder,
you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1, 4], [-1, 3]], and on the first move, your
destination square is 2. You follow the ladder to square 3, but do not follow
the subsequent ladder to 4.

Return the least number of moves required to reach the square n^2.
If it is not possible to reach the square, return -1.


Example 1:
Input: board = [[-1,-1,-1,-1,-1,-1],    ### [36,35,34,33,32,31],
                [-1,-1,-1,-1,-1,-1],    ### [25,26,27,28,29,30],
                [-1,-1,-1,-1,-1,-1],    ### [24,23,22,21,20,19],
                [-1,35,-1,-1,13,-1],    ### [13,14,15,16,17,18],
                [-1,-1,-1,-1,-1,-1],    ### [12,11,10, 9, 8, 7],
                [-1,15,-1,-1,-1,-1]]    ### [ 1, 2, 3, 4, 5, 6]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

Example 2:
Input: board = [[-1,-1],
                [-1, 3]]
Output: 1
 

Constraints:        n == board.length == board[i].length
                    2 <= n <= 20
                    grid[i][j] is either -1 or in the range [1, n^2].
                    The squares labeled 1 and n^2 do not have any ladders or snakes.
Accepted:           97.1K
Submissions:        232.2K
Acceptance Rate:    41.8%
'''

from typing import List
import math

class Solution:     ### My Solution has bug     135 / 213 testcases passed
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n, cnt, trace = len(board), 1, []
        if n & 1:
            for r in range(n - 1, -1, -1):
                if r & 1:
                    for c in range(n - 1, -1, -1):
                        trace.append([cnt, board[r][c], math.inf])
                        cnt += 1
                else:
                    for c in range(n):
                        trace.append([cnt, board[r][c], math.inf])
                        cnt += 1
        else:
            for r in range(n - 1, -1, -1):
                if r & 1:
                    for c in range(n):
                        trace.append([cnt, board[r][c], math.inf])
                        cnt += 1
                else:
                    for c in range(n - 1, -1, -1):
                        trace.append([cnt, board[r][c], math.inf])
                        cnt += 1                        
        trace[0][2] = 0
        for i in range(n * n):
            idx, step = trace[i][1], trace[i][2]
            if idx == -1:
                for j in range(i + 1, min(i + 7, len(trace))):
                    trace[j][2] = min(trace[j][2], step + 1)
            else:
                trace[idx - 1][2] = min(trace[idx - 1][2], step)
                if trace[idx - 1][1] == n ** 2: trace[n ** 2 - 1][2] = min(trace[n**2 - 1][2], step + 1)
                trace[idx - 1][1] = -1
        return -1 if trace[n * n - 1][2] == math.inf else trace[n * n - 1][2]

class Solution_v2:      ### LeetCode ID: simsinght
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ### flatten board into a 1D array
        board.reverse()
        arr = [0]
        for i, row in enumerate(board):
            if i % 2 == 0: arr += row
            else: arr += row[::-1]
        NN, queue, visited, moves = len(board) ** 2, [1], set(), 0
        while queue:
            next_level = []
            while queue:
                square = queue.pop()
                if square == NN: return moves 
                ### visit every dice role (1 to 6)
                for i in range(1, 7):
                    ### don't visit squares we already saw, don't visit a square past N*N
                    if square + i <= NN and square + i not in visited:
                        visited.add(square + i)
                        ### if next square is a snake/ladder, take it
                        if arr[square + i] != -1: next_level.append(arr[square + i])
                        ### otherwise go to the square (1 to 6) hops away
                        else: next_level.append(square + i)
            queue, moves = next_level, moves + 1

        return -1

class Solution_v2_2:      ### LeetCode ID: simsinght
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ### flatten board into a 1D array
        board.reverse()
        # for b in board: print(b)
        arr = [0]
        for i, row in enumerate(board):
            if i % 2 == 0: arr += row
            else: arr += row[::-1]
        print(arr)
        
        NN, queue, visited, moves = len(board) ** 2, [1], set(), 0
        while queue:
            next_level = []
            while queue:
                square = queue.pop()
                print("\n-- square =", square)
                if square == NN:
                    print("# ---- square == NN")
                    return moves 

                # visit every dice role (1 to 6)
                for i in range(1, 7):
                    # don't visit squares we already saw, don't visit a square past N*N
                    if square + i <= NN and square + i not in visited:
                        visited.add(square + i)
                        print("\tvisited:",visited)
                        # if next square is a snake/ladder, take it
                        if arr[square + i] != -1:
                            print("----next_level:", next_level)
                            next_level.append(arr[square + i])
                            print("----next_level:", next_level)
                        # otherwise go to the square (1 to 6) hops away
                        else:
                            print("------next_level:", next_level)
                            next_level.append(square + i)
                            print("------next_level:", next_level)

            queue, moves = next_level, moves + 1
            print("\n-------- moves =", moves, "  queue =", queue, end="\n\n")

        return -1 

def main():

    sol = Solution()
    sol = Solution_v2()
    # sol = Solution_v2_2()

    # board = [[-1,-1,-1,-1,-1,-1],
    #          [-1,-1,-1,-1,-1,-1],
    #          [-1,-1,-1,-1,-1,-1],
    #          [-1,35,-1,-1,13,-1],
    #          [-1,-1,-1,-1,-1,-1],
    #          [-1,15,-1,-1,-1,-1]]
    # print(sol.snakesAndLadders(board))      # Output: 4

    # board = [[-1,-1], [-1, 3]]
    # print(sol.snakesAndLadders(board))      # Output: 1

    # board = [[ 9, 8, 7, 6,-1],
    #          [10,11,12,-1,-1],
    #          [-1,-1,-1,-1,-1],
    #          [-1,15,-1,13,-1],
    #          [-1,-1,-1,-1,-1]]
    # print(sol.snakesAndLadders(board))      # Output: -1

    # board = [[-1,-1,-1],
    #          [-1, 9, 8],
    #          [-1, 8, 9]]
    # print(sol.snakesAndLadders(board))      # Output: 1

    # board = [[-1, 1, 2,-1],
    #          [ 2,13,15,-1],
    #          [-1,10,-1,-1],
    #          [-1, 6, 2, 8]]
    # print(sol.snakesAndLadders(board))      # Output: 2

    # board = [[-1, -1,  2, 21, -1],          ### 136 / 213 testcases
    #          [16, -1, 24, -1,  4],          ### Solution: 1(-1) -> 4(23) -> 23(2) -> 25
    #          [ 2,  3, -1, -1, -1],
    #          [-1, 11, 23, 18, -1],
    #          [-1, -1, -1, 23, -1]]
    # print(sol.snakesAndLadders(board))      # Output: 2

    # board = [[-1, -1, -1, -1, 48,  5, -1],        ### 186 / 213 testcases
    #          [12, 29, 13,  9, -1,  2, 32],        ### Solution:
    #          [-1, -1, 21,  7, -1, 12, 49],        ### 1(-1) -> 6(-1) -> 12(35) -> 35(49) -> 49
    #          [42, 37, 21, 40, -1, 22, 12],
    #          [42, -1,  2, -1, -1, -1,  6],
    #          [39, -1, 35, -1, -1, 39, -1],
    #          [-1, 36, -1, -1, -1, -1,  5]]
    # print(sol.snakesAndLadders(board))          # Output: 3

    board = [[-1,-1,-1,46,47,-1,-1,-1],
             [51,-1,-1,63,-1,31,21,-1],
             [-1,-1,26,-1,-1,38,-1,-1],
             [-1,-1,11,-1,14,23,56,57],
             [11,-1,-1,-1,49,36,-1,48],
             [-1,-1,-1,33,56,-1,57,21],
             [-1,-1,-1,-1,-1,-1,2,-1],
             [-1,-1,-1,8,3,-1,6,56]]
    print(sol.snakesAndLadders(board))          # Output: 4


if __name__ == "__main__":
    main()

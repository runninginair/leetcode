''' 79. Word Search
Medium      11086       424     Add to List     Share
Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.
 

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

Accepted:       1,106,772
Submissions:    2,776,508

'''


from typing import List


class Solution:     # DFS >>>>> has bug <<<<<< Not corret for test case 3
    # def exist(self, board: List[List[str]], word: str) -> bool:
    def exist(self, board, word: str) -> bool:    
        m, n = len(board), len(board[0])
        
        # DFS the word
        def dfs(i, j, m, n) -> bool:
            stack = [[i, j]]
            t = [[False for _ in range(n)] for _ in range(m)]
            x = y = index_word = 0
            while stack:
                pos = stack.pop(-1)
                
                x, y = pos[0], pos[1]
                
                t[x][y] = True
                index_word += 1
                # print("t =", t, " pos =", [x, y], "  i =", index_word)

                if index_word == len(word): return True

                if x > 0 and not t[x-1][y] and board[x-1][y] == word[index_word]:
                    stack.append([x-1, y])
                    # print("# UP --", stack)

                if x < m-1 and not t[x+1][y] and board[x+1][y] == word[index_word]:
                    stack.append([x+1, y])
                    # print("# down --", stack)

                if y > 0 and not t[x][y-1] and board[x][y-1] == word[index_word]:
                    stack.append([x, y-1])
                    # print("# LEFT --", stack)
                    
                if y < n-1 and not t[x][y+1] and board[x][y+1] == word[index_word]:
                    stack.append([x, y+1])
                    # print("# RIGHT --", stack)

            t = [[False for _ in range(n)] for _ in range(m)]            
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    # do DFS the whole word
                    if dfs(i, j, m, n): return True

        return False

class Solution_v2:
    def exist(self, board, word: str) -> bool:    
        m, n = len(board), len(board[0])
        visited = set()

        # DFS -- Backtrack 
        def dfs(x, y, k) -> bool:
            if k == len(word): return True
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[k] or (x, y) in visited:
                return False
            visited.add((x, y))
            res = (dfs(x, y-1, k+1) or dfs(x, y+1, k+1) or dfs(x-1, y, k+1) or dfs(x+1, y, k+1))
            visited.remove((x, y))
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0): return True
        return False

class Solution_v3:  ### 11/23/2022
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, visited = len(board), len(board[0]), set()

        def dfs(x: int, y: int, k: int) -> bool:
            if k == len(word): return True
            if (x, y) in visited or x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[k]:
                return False
            visited.add((x, y))
            res = dfs(x+1, y, k+1) or dfs(x-1, y, k+1) or dfs(x, y+1, k+1) or dfs(x, y-1, k+1)
            visited.remove((x, y))
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0): return True
        return False


def main():
    sol = Solution()    # BuG in Test case 3
    sol = Solution_v2()
    sol = Solution_v3()

    board = [["a","b"],
             ["c","d"]]
    word = "cdba"                       # True
    print(sol.exist(board, word))

    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = "SEE"                        # True
    print(sol.exist(board, word))

    board = [["A","B","C","E"],
             ["S","F","E","S"],
             ["A","D","E","E"]]
    word = "ABCEFSADEESE"               # True
    print(sol.exist(board, word))

    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = "ABCB"                       # Output: false
    print(sol.exist(board, word))

main()

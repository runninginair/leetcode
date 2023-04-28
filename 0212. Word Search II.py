''' 212. Word Search II
Hard    6950    302     Add to List     Share
Given an m x n board of characters and a list of strings words, return all
words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.


Example 1:
Input: board = [["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"]], 
       words = ["oath", "pea", "eat", "rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],
                ["c","d"]],
       words = ["abcb"]
Output: []
 
Constraints:    m == board.length
                n == board[i].length
                1 <= m, n <= 12
                board[i][j] is a lowercase English letter.
                1 <= words.length <= 3 * 10 ^ 4
                1 <= words[i].length <= 10
                words[i] consists of lowercase English letters.
                All the strings of words are unique.
Accepted:       489,660
Submissions:    1,326,790
'''

class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        def dfs(i, j, word) -> bool:
            l = len(word)
            index = 1
            q = [(i, j, l, index)]
            while q:
                x, y, l, idx = q.pop()
                if x > 0 and board[x - 1][y] == words[idx]:
                    if idx + 1 == l: return True
                    else: q.append((x - 1, y, l - 1, idx + 1))
                if x < m - 1 and board[x + 1][y] == words[idx]:
                    if idx + 1 == l: return True
                    else: q.append((x + 1, y, l - 1, idx + 1))
                if y > 0 and board[x][y - 1] == words[idx]:
                    if idx + 1 == l: return True
                    else: q.append((x, y - 1, l - 1, idx + 1))
                if y < n - 1 and board[x][y + 1] == words[idx]:
                    if idx + 1 == l: return True
                    else: q.append((x, y + 1, l - 1, idx + 1))
            return False
        
        res = []
        for i in range(m):
            for j in range(n):
                for k in range(len(words)):
                    if board[i][j] == words[k][0]:
                        if dfs(i, j, words[k]):
                            res.append(words[k])
        return res


def main():
    sol = Solution()
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]], 
    words = ["oath", "pea", "eat", "rain"]
    # Output: ["eat","oath"]
    print(sol.findWords(board, words))

main()

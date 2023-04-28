''' 1444. Number of Ways of Cutting a Pizza

Hard        757         44          Companies

Given a rectangular pizza represented as a rows x cols matrix containing the following
characters: 'A' (an apple) and '.' (empty cell) and given the integer k.
You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut
position at the cell boundary and cut the pizza into two pieces. If you cut the pizza
vertically, give the left part of the pizza to a person. If you cut the pizza
horizontally, give the upper part of the pizza to a person. Give the last piece of
pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least
one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.


Example 1:
Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza.
Note that pieces must contain at least one apple.

Example 2:
Input: pizza = ["A..","AA.","..."], k = 3
Output: 1

Example 3:
Input: pizza = ["A..","A..","..."], k = 1
Output: 1
 

Constraints:        1 <= rows, cols <= 50
                    rows == pizza.length
                    cols == pizza[i].length
                    1 <= k <= 10
                    pizza consists of characters 'A' and '.' only.
Accepted:           26.9K
Submissions:        47.3K
Acceptance Rate:    56.7%
'''


from typing import List


class Solution:     ### Time Limit Exceeded     25 / 53 testcases passed
    def ways(self, pizza: List[str], k: int) -> int:
        # if k == 1: return 1
        row, col = len(pizza), len(pizza[0])
        self.ans = sumApple = 0
        def cntApple(row_start, row_end, col_start, col_end):
            cnt = 0
            for r in range(row_start, row_end):
                for c in range(col_start, col_end):
                    if pizza[r][c] == 'A':
                        cnt += 1
            return cnt
        sumApple = cntApple(0, row, 0, col)
        # print(sumApple)

        def dfs(row_rem, col_rem, k):   ### Back tracking DFS
            if cntApple(row_rem, row, col_rem, col) < k: return 
            if k == 1: self.ans += 1
            for i in range(row_rem, row - 1):
                if cntApple(row_rem, i + 1, col_rem, col) > 0:
                    dfs(i + 1, col_rem, k - 1)
            for i in range(col_rem, col - 1):
                if cntApple(row_rem, row, col_rem, i + 1) > 0:
                    dfs(row_rem, i + 1, k - 1)

        dfs(0, 0, k)
        return self.ans % (10 ** 9 + 7)


class Solution_v2:     ### Time Limit Exceeded      52 / 53 testcases passed
    def ways(self, pizza: List[str], k: int) -> int:
        row, col = len(pizza), len(pizza[0])
        self.ans = sumApple = 0
        def cntApple(row_start, row_end, col_start, col_end):
            cnt = 0
            for r in range(row_start, row_end):
                for c in range(col_start, col_end):
                    if pizza[r][c] == 'A':
                        cnt += 1
            return cnt
        sumApple = cntApple(0, row, 0, col)
        # print(sumApple)

        def dfs(row_rem, col_rem, k, total):   ### Back tracking DFS
            if total < k: return 
            if k == 1:
                self.ans += 1
                return
            for i in range(row_rem, row - 1):
                cutOut = cntApple(row_rem, i + 1, col_rem, col)
                remApple = total - cutOut
                if cutOut > 0 and remApple >= k - 1:
                    dfs(i + 1, col_rem, k - 1, remApple)
            for i in range(col_rem, col - 1):
                cutOut = cntApple(row_rem, row, col_rem, i + 1)
                remApple = total - cutOut
                if cutOut > 0 and remApple >= k - 1:
                    dfs(row_rem, i + 1, k - 1, remApple)

        dfs(0, 0, k, sumApple)
        return self.ans % (10 ** 9 + 7)


class Solution_v3:     ### DP solution
    def ways(self, pizza: List[str], k: int) -> int:
        row, col = len(pizza), len(pizza[0])
        top = [[0 for _ in range(col)] for _ in range(row)]
        left = [[0 for _ in range(col)] for _ in range(row)]
        ### Record Top-down:
        for i in range(col):
            if pizza[row - 1][i] == 'A': top[row - 1][i] = 1
        for j in range(col):
            for i in range(row - 2, -1, -1):
                if pizza[i][j] == 'A': top[i][j] = top[i + 1][j] + 1
                else: top[i][j] = top[i + 1][j]
        
        ### Record left-right:
        for i in range(row):
            if pizza[i][col - 1] == 'A': left[i][col - 1] = 1
        for i in range(row):
            for j in range(col - 2, -1, -1):
                if pizza[i][j] == 'A': left[i][j] = left[i][j + 1] + 1
                else: left[i][j] = left[i][j + 1]

        # for to in top: print(to)
        # print()
        # for le in left: print(le)

        def dfs(row_rem, col_rem, k, total):   ### Back tracking DFS
            if total < k: return 
            if k == 1:
                self.ans += 1
                return
            rowCutOff = 0
            for i in range(row_rem, row - 1):
                rowCutOff = left[i][col_rem]
                remApple = total - rowCutOff
                if rowCutOff > 0 and remApple >= k - 1:
                    dfs(i + 1, col_rem, k - 1, remApple)
            colCutOff = 0
            for i in range(col_rem, col - 1):
                colCutOff = top[row_rem][i]
                remApple = total - colCutOff
                if colCutOff > 0 and remApple >= k - 1:
                    dfs(row_rem, i + 1, k - 1, remApple)


        self.ans = sumApple = 0
        def cntApple(row_start, row_end, col_start, col_end):
            cnt = 0
            for r in range(row_start, row_end):
                for c in range(col_start, col_end):
                    if pizza[r][c] == 'A':
                        cnt += 1
            return cnt
        sumApple = cntApple(0, row, 0, col)

        dfs(0, 0, k, sumApple)
        return self.ans

def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()


    pizza, k = ["A..", "AAA", "..."], 3   # Output: 3
    print(sol.ways(pizza, k))

    pizza, k = ["A..", "AA.", "..."], 3   # Output: 1
    print(sol.ways(pizza, k))

    pizza, k = ["A..","A..","..."], 1   # Output: 1
    print(sol.ways(pizza, k))

    pizza, k = ["A...",
                ".A..",
                "..A.",
                "...A"], 3   # Output: 12
    print(sol.ways(pizza, k))

    pizza, k = ["AAAA...A.A",
                "...A.AAA.A",
                "A.A..AA.AA",
                ".A..A...A.",
                ".A..AAAA.A",
                "AA..A.A...",
                ".A..AAAAA.",
                ".AAAAAAA.A",
                "A..A.AAA.A"], 1    # Output: 1
    print(sol.ways(pizza, k))

    # pizza, k = ["..A.A.AAA...AAAAAA.AA..A..A.A......A.AAA.AAAAAA.AA",
    #             "A.AA.A.....AA..AA.AA.A....AAA.A........AAAAA.A.AA.",
    #             "A..AA.AAA..AAAAAAAA..AA...A..A...A..AAA...AAAA..AA",
    #             "....A.A.AA.AA.AA...A.AA.AAA...A....AA.......A..AA.",
    #             "AAA....AA.A.A.AAA...A..A....A..AAAA...A.A.A.AAAA..",
    #             "....AA..A.AA..A.A...A.A..AAAA..AAAA.A.AA..AAA...AA",
    #             "A..A.AA.AA.A.A.AA..A.A..A.A.AAA....AAAAA.A.AA..A.A",
    #             ".AA.A...AAAAA.A..A....A...A.AAAA.AA..A.AA.AAAA.AA.",
    #             "A.AA.AAAA.....AA..AAA..AAAAAAA...AA.A..A.AAAAA.A..",
    #             "A.A...A.A...A..A...A.AAAA.A..A....A..AA.AAA.AA.AA.",
    #             ".A.A.A....AAA..AAA...A.AA..AAAAAAA.....AA....A....",
    #             "..AAAAAA..A..A...AA.A..A.AA......A.AA....A.A.AAAA.",
    #             "...A.AA.AAA.AA....A..AAAA...A..AAA.AAAA.A.....AA.A",
    #             "A.AAAAA..A...AAAAAAAA.AAA.....A.AAA.AA.A..A.A.A...",
    #             "A.A.AA...A.A.AA...A.AA.AA....AA...AA.A..A.AA....AA",
    #             "AA.A..A.AA..AAAAA...A..AAAAA.AA..AA.AA.A..AAAAA..A",
    #             "...AA....AAAA.A...AA....AAAAA.A.AAAA.A.AA..AA..AAA",
    #             "..AAAA..AA..A.AA.A.A.AA...A...AAAAAAA..A.AAA..AA.A",
    #             "AA....AA....AA.A......AAA...A...A.AA.A.AA.A.A.AA.A",
    #             "A.AAAA..AA..A..AAA.AAA.A....AAA.....A..A.AA.A.A...",
    #             "..AA...AAAAA.A.A......AA...A..AAA.AA..A.A.A.AA..A.",
    #             ".......AA..AA.AAA.A....A...A.AA..A.A..AAAAAAA.AA.A",
    #             ".A.AAA.AA..A.A.A.A.A.AA...AAAA.A.A.AA..A...A.AAA..",
    #             "A..AAAAA.A..A..A.A..AA..A...AAA.AA.A.A.AAA..A.AA..",
    #             "A.AAA.A.AAAAA....AA..A.AAA.A..AA...AA..A.A.A.AA.AA",
    #             ".A..AAAA.A.A.A.A.......AAAA.AA...AA..AAA..A...A.AA",
    #             "A.A.A.A..A...AA..A.AAA..AAAAA.AA.A.A.A..AA.A.A....",
    #             "A..A..A.A.AA.A....A...A......A.AA.AAA..A.AA...AA..",
    #             ".....A..A...A.A...A..A.AA.A...AA..AAA...AA..A.AAA.",
    #             "A...AA..A..AA.A.A.AAA..AA..AAA...AAA..AAA.AAAAA...",
    #             "AA...AAA.AAA...AAAA..A...A..A...AA...A..AA.A...A..",
    #             "A.AA..AAAA.AA.AAA.A.AA.A..AAAAA.A...A.A...A.AA....",
    #             "A.......AA....AA..AAA.AAAAAAA.A.AA..A.A.AA....AA..",
    #             ".A.A...AA..AA...AA.AAAA.....A..A..A.AA.A.AA...A.AA",
    #             "..AA.AA.AA..A...AA.AA.AAAAAA.....A.AA..AA......A..",
    #             "AAA..AA...A....A....AA.AA.AA.A.A.A..AA.AA..AAA.AAA",
    #             "..AAA.AAA.A.AA.....AAA.A.AA.AAAAA..AA..AA.........",
    #             ".AA..A......A.A.AAA.AAAA...A.AAAA...AAA.AAAA.....A",
    #             "AAAAAAA.AA..A....AAAA.A..AA.A....AA.A...A.A....A..",
    #             ".A.A.AA..A.AA.....A.A...A.A..A...AAA..A..AA..A.AAA",
    #             "AAAA....A...A.AA..AAA..A.AAA..AA.........AA.AAA.A.",
    #             "......AAAA..A.AAA.A..AAA...AAAAA...A.AA..A.A.AA.A.",
    #             "AA......A.AAAAAAAA..A.AAA...A.A....A.AAA.AA.A.AAA.",
    #             ".A.A....A.AAA..A..AA........A.AAAA.AAA.AA....A..AA",
    #             ".AA.A...AA.AAA.A....A.A...A........A.AAA......A...",
    #             "..AAA....A.A...A.AA..AAA.AAAAA....AAAAA..AA.AAAA..",
    #             "..A.AAA.AA..A.AA.A...A.AA....AAA.A.....AAA...A...A",
    #             ".AA.AA...A....A.AA.A..A..AAA.A.A.AA.......A.A...A.",
    #             "...A...A.AA.A..AAAAA...AA..A.A..AAA.AA...AA...A.A.",
    #             "..AAA..A.A..A..A..AA..AA...A..AA.AAAAA.A....A..A.A"], 8
    # print(sol.ways(pizza, k))



if __name__ == "__main__":
    main()

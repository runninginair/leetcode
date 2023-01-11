''' 22. Generate Parentheses
Medium      15242       581     Add to List     Share

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:    1 <= n <= 8
Accepted:       1,212,371
Submissions:    1,693,445
'''

class Solution_v1:  # Brute Force
    # def generateParenthesis(self, n: int) -> List[str]:
    def generateParenthesis(self, n: int):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                print("# 1-1:", A)
                generate(A)
                A.pop()
                print("# 1-2:", A)
                # print()

                A.append(')')
                print("# 2-1:", A)
                generate(A)
                A.pop()
                print("# 2-2:", A)
                # print()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans


'''
                           (
                     /           \
                ((                 ()
              /    \                |
            (((     (()            ()(   
           /       /   \          /   \
       ((()))   (()(   (())     ()()  ()((
                  |     |        |      |
                (()()  (())(  ()()()   ()(())
                  |     |
               (()())  (())()
'''
class Solution_v2:  # Backtracking
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        res = []
        self.helper(n, n, '', res)
        return res

    def helper(self, l, r, cur, res):
        if l > r:
            return
        if l == 0 and r == 0:
            res.append(cur)
        if l > 0:
            self.helper(l-1, r, cur + '(', res)
        if r > 0:
            self.helper(l, r-1, cur + ')', res)


def main():
    # sol = Solution_v1()
    sol = Solution_v2()

    # print(sol.generateParenthesis(1))
    print(sol.generateParenthesis(2))       # Output: ['(())', '()()']
    # print(sol.generateParenthesis(3))
    # print(sol.generateParenthesis(4))

main()
''' 32. Longest Valid Parentheses
Hard    9944    316     Add to List     Share
Given a string containing just the characters '(' and ')', return the length of
the longest valid (well-formed) parentheses substring.


Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
 
Constraints:    0 <= s.length <= 3 * 10^4
                s[i] is '(', or ')'.
Accepted:       573,416
Submissions:    1,754,012
'''

class Solution:     ### Sliding window solution O(n)
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack = []
        res_1 = res_2 = credit = 0

        for c in s:
            if c == ')':
                if credit == 0:
                    stack.clear()
                    continue
                else:
                    stack.append(')')
                    credit -= 1
                    if credit == 0:
                        res_1 = max(res_1, len(stack) - credit)
            else:
                stack.append('(')
                credit += 1

        credit, stack = 0, []
        for c in s[::-1]:
            if c == '(':
                if credit == 0: 
                    stack.clear()
                    continue
                else:
                    stack.append('(')
                    credit -= 1
                    if credit == 0:
                        res_2 = max(res_2, len(stack) - credit)
            else:
                stack.append(')')
                credit += 1
        
        return max(res_1, res_2)

def main():
    sol = Solution()

    s = ")()())"    # Output 4
    print(sol.longestValidParentheses(s))

    s = ")()"       # Output 2
    print(sol.longestValidParentheses(s))

    s = ""       # Output 0
    print(sol.longestValidParentheses(s))

    s = ")))(((())()()"       # Output 8
    print(sol.longestValidParentheses(s))

    s = "()(()"       # Output 2
    print(sol.longestValidParentheses(s))

    s = "))))())()()(()"    # Output 4
    print(sol.longestValidParentheses(s))    

main()

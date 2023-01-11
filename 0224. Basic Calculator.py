''' 224. Basic Calculator
Hard    4508    345     Add to List     Share

Given a string s representing a valid expression, implement a basic calculator
to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings
as mathematical expressions, such as eval().


Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:    1 <= s.length <= 3 * 10^5
                s consists of digits, '+', '-', '(', ')', and ' '.
                s represents a valid expression.
                '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
                '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
                There will be no two consecutive operators in the input.
                Every number and running calculation will fit in a signed 32-bit integer.
Accepted:       337,908
Submissions:    813,770

'''


class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        sum = i = 0
        stack = []
        N = len(s)

        while i < N:    
            if '0' <= s[i] <= '9':
                num = 0
                while i < N and '0' <= s[i] <= '9':
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                sum += num * sign
                i -= 1
            elif s[i] == '+': sign = 1
            elif s[i] == '-': sign = -1
            elif s[i] == '(':
                stack.append(sum)
                stack.append(sign)
                sum = 0
                sign = 1
            elif s[i] == ')':
                sum = stack.pop() * sum
                sum += stack.pop()
            i += 1
        return sum

def main():
    sol = Solution()
    print(sol.calculate("1 + 1"))                   # 2
    print(sol.calculate(" 2-1 + 2 "))               # 3
    print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))     # 23
    print(sol.calculate("2147483647"))
    print(sol.calculate("1234567"))

main()

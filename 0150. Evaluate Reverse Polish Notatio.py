''' 150. Evaluate Reverse Polish Notation
Medium      4.4K      763       Companies

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the
expression would always evaluate to a result, and there will not be any
division by zero operation.


Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:        1 <= tokens.length <= 104
                    tokens[i] is either an operator: "+", "-", "*", or "/",
                    or an integer in the range [-200, 200].
Accepted:           546.5K
Submissions:        1.2M
Acceptance Rate:    44.3%
'''

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack, operators  = [], set(["+", "-", "*", "/"])
        for token in tokens:
            if token in operators:
                b, a, c = stack.pop(), stack.pop(), 0
                if token == "+": c = a + b
                elif token == "-": c = a - b
                elif token == "*": c = a * b
                else: c = int(a / b)
                stack.append(c)
            else:
                stack.append(int(token))
        return stack.pop()

def main():
    sol = Solution()
    tokens = ["2","1","+","3","*"]      # Output: 9
    print(sol.evalRPN(tokens))

    tokens = ["4","13","5","/","+"]     # Output: 6
    print(sol.evalRPN(tokens))

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]  # Output: 22
    print(sol.evalRPN(tokens))

    tokens = ["4","-2","/","2","-3","-","-"]    # Output: -7
    print(sol.evalRPN(tokens))


main()

'''
1597. Build Binary Expression Tree From Infix Expression

A binary expression tree is a kind of binary tree used to represent arithmetic
expressions. Each node of a binary expression tree has either zero or two children.

Leaf nodes (nodes with 0 children) correspond to operands (numbers), and
internal nodes (nodes with 2 children) correspond to the operators
'+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

For each internal node with operator o, the infix expression that it represents
is (A o B), where A is the expression the left subtree represents and B is the
expression the right subtree represents.

You are given a string s, an infix expression containing operands, the
operators described above, and parentheses '(' and ')'.

Return the binary expression tree, which its in-order traversal reproduce s.

Please note that order of operations applies in s. That is, expressions in
parentheses are evaluated first, and multiplication and division happen before
addition and subtraction.

 Example 1:
 Input: s = "2 - 3 / ( 5 * 2 ) + 1"
 Output: [+, -, 1, 2, /, null, null, null, null, 3, *, null, null, 5, 2]

 Example 2:
 Input: s = "3 * 4 - 2 * 5"
 Output: [-, *, *, 3, 4, 2, 5]

 Example 3:
 Input: s = "1 + 2 + 3 + 4 + 5"
 Output: [+, +, 5, +, 4, null, null, +, 3, null, null, 1, 2]


 Constraints:
     1 <= s.length <= 10^5
     s consists of digits and the characters '+', '-', '*', '/', '(', and ')'.
     Operands in s are exactly 1 digit.
     It is guaranteed that s is a valid expression.

'''



# AWS Nodkarni, Akshay inteview workflows:
'''
Q1. Can you creat a date structure or class to represent a binary expression tree?

 Example:
 A binary expression tree is:

     *               +            
    / \             / \
   +   c           a   b
  / \
 a   b

 (a+b)*c           (a+b)

'''

from copy import Error
import string


class Node:
    def __init__(self, key) -> None:
        self.val = key
        self.left = None
        self.right = None

    def postOrder(self, root)->string:
        if (root.left is None) and (root.right is None):
            return root.val
        res = ""
        if root.left:
            res += self.postOrder(root.left)
        if root.right:
            res += self.postOrder(root.right)
        res += root.val
        
        return res


'''
Q2. Give an instance of your Node/Tree class, can you write a method /function
that returns the (infix) express the tree represents?

 What is input? -- A tree node.
 What is output? -- An infix express the tree represents. type: string 
 Valued question: 
 Is the tree guarutined to be a valid expression? 
 Do we need to virify the tree is an a valid infix expression?
 Is it possible the tree root is null?

'''

class Solution:
    def getInfix(self, node: Node):
        if node is None:
            return Error
        output = ""
        if (node.left is None) and (node.right is None):
            return node.val
        output += "("
        output += self.getInfix(node.left)
        output += node.val
        output += self.getInfix(node.right)
        output += ")"

        return output


'''
Q3. Can you write a method/function that given the PPN expression string,
returns back the expression tree (of Nodes) representing it?
(RPN: Reverse Polish Notation)
 Example:
 *  ab+ = a+b
 *  ab+c* = (a+b)*c
 *  ab+cd+* = (a+b)*(c+d)
 *  ab+cd+*5* = ((a+b)*(c+d))*5

'''

class Q3Solution:
    def getExpressionTree(self, str)->Node:
        if str == "": return None
        n = len(str)
        stack, root = [], None

        for i in range(n):
            if str[i] != ("+" or "-" or "*" or "/"):
                stack.append(Node(str[i]))
            else:
                root = Node(str[i])
                root.right = stack.pop()
                root.left = stack.pop()
                stack.append(root)

        def combine(ops, stack):
            root = 

        return stack[-1]


def main():

    sol = Solution()
    root, n1, n2, n3, n4 = Node("*"), Node("+"), Node("c"), Node("a"), Node("b")
    root.left, root.right = n1, n2
    n1.left, n1.right = n3, n4
    print(sol.getInfix(root)) # ((a+b)*c)

    sol_3 = Q3Solution()
    str = "ab+"
    res = sol_3.getExpressionTree(str)
    print(sol.getInfix(res))

    str = "ab+cd+*5*"  # Output: ((a+b)*(c+d))*5
    res = sol_3.getExpressionTree(str)
    print(sol.getInfix(res))

main()

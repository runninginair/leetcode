''' 0606. Construct String from Binary Tree

Easy        2.5K        3K         Companies

Given the root of a binary tree, construct a string consisting of parenthesis
and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping
relationship between the string and the original binary tree.


Example 1:          (1)
                   /   \
                (2)     (3)
               /
            (4)

Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to
omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"


Example 2:          (1)
                   /   \
                (2)     (3)
                  \
                  (4)

Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the
first parenthesis pair to break the one-to-one mapping relationship between the
input and the output.
 

Constraints:        The number of nodes in the tree is in the range [1, 10^4].
                    -1000 <= Node.val <= 1000
Accepted:           213.9K
Submissions:        334.4K
Acceptance Rate:    64.0%
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return
        elif not root.left and not root.right: return str(root.val)
        elif root.left and root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"
        elif root.right:
            return str(root.val) + "()(" + self.tree2str(root.right) + ")"
        else:
            return str(root.val) + "(" + self.tree2str(root.left) + ")" 

def main():
    sol = Solution()

    n1, n2, n3, n4 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4)
    n1.left, n1.right, n2.left = n2, n3, n4
    print(sol.tree2str(n1))     # Expect Output: "1(2(4))(3)"

    m1, m2, m3, m4 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4)
    m1.left, m1.right, m2.right = m2, m3, m4
    print(sol.tree2str(m1))     # Expect Output: "1(2()(4))(3)"   

main()

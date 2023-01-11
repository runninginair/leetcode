''' 1339. Maximum Product of Splitted Binary Tree
Medium      1.5K    68      Companies

Given the root of a binary tree, split the binary tree into two subtrees by
removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees.
Since the answer may be too large, return it modulo 10^9 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.


Example 1:
                 1                          1
              /    \                          \
            2        3   ==>           2       3    ==>     (2+4+5) * (1+3+6) = 110
          /   \     /                /   \    /
         4     5   6               4      5   6

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. 
Their product is 110 (11*10)


Example 2:
                1                      1
                  \                     \
                   2         ==>         2        ==>     (1+2+3) * (4+5+6) = 90
                 /   \                  /
                3     4                3     4
                    /   \                  /  \
                   5     6                5    6

Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)


Constraints:    The number of nodes in the tree is in the range [2, 5 * 104^].
                1 <= Node.val <= 10^4
Accepted:           66K
Submissions:        151.4K
Acceptance Rate:    43.6%

'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ### First loop get the sum of all nodes.
        def getSum(root: Optional[TreeNode]) -> int:
            if not root: return 0
            sum, stack = 0, [root]
            while stack:
                node = stack.pop()
                sum += node.val
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            return sum

        self.total = getSum(root)
        self.ans = 0

        def dfs_v1(root) -> None:
            if root:
                if root.left:
                    left_part = getSum(root.left)
                    self.ans = max(self.ans, left_part * (self.total - left_part))
                    dfs_v1(root.left)
                if root.right:
                    right_part = getSum(root.right)
                    self.ans = max(self.ans, right_part * (self.total - right_part))                    
                    dfs_v1(root.right)
        # dfs(root)

        def dfs_v2(root) -> int:    # V2 version is more efficient than 
            if not root: return 0
            left_part = dfs_v2(root.left)
            right_part = dfs_v2(root.right)
            self.ans = max(self.ans, (self.total - left_part) * left_part, (self.total - right_part) * right_part)
            return root.val + left_part + right_part

        dfs_v2(root)

        return self.ans




def main():
    sol = Solution()
    n1, n2, n3, n4, n5, n6 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
    n1.left, n1.right, n2.left, n2.right, n3.left = n2, n3, n4, n5, n6
    print(sol.maxProduct(n1))

    m1, m2, m3, m4, m5, m6 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
    m1.right, m2.left, m2.right, m4.left, m4.right = m2, m3, m4, m5, m6
    print(sol.maxProduct(m1))


main()
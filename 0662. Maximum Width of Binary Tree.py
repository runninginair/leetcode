''' 0662. Maximum Width of Binary Tree

Medium        7.4K        997         Companies

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 

Constraints:        The number of nodes in the tree is in the range [1, 3000].
                    -100 <= Node.val <= 100
Accepted:           292.2K
Submissions:        684.7K
Acceptance Rate:    42.7%

'''

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = root.val = 1
        q = [root]
        while q:
            level = []
            while q:
                level.append(q.pop(0))
            res = max(res, level[-1].val - level[0].val + 1)
            for node in level:
                if node.left:
                    node.left.val = node.val * 2 - 1
                    q.append(node.left)
                if node.right:
                    node.right.val = node.val * 2
                    q.append(node.right)
        return res


class Solution_v2:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q, width = deque([(root, 0)]), 0
        while q:
            width = max(width, q[-1][1] - q[0][1])
            for _ in range(len(q)):
                node, k = q.popleft()
                if node.left:
                    q.append((node.left, k * 2 - 1))
                if node.right:
                    q.append((node.right, k * 2))
        return width + 1 if root else 0


class Solution_v3:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q, width = [(root, 0)], 1
        while q:
            width = max(width, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                n, k = q.pop(0)
                if n.left: q.append((n.left, k * 2 - 1))
                if n.right: q.append((n.right, k * 2))
        return width if root else 0


def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()

    # root = [1,3,2,5,3,null,9]   # Output: 4
    n1, n2, n3, n4, n5, n7 = TreeNode(1), TreeNode(3), TreeNode(2), TreeNode(5), TreeNode(3), TreeNode(9)
    n1.left, n1.right, n2.left, n2.right, n3.right = n2, n3, n4, n5, n7
    print(sol.widthOfBinaryTree(n1))


if __name__ == "__main__":
    main()

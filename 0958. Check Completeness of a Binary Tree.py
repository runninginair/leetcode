''' 0958. Check Completeness of a Binary Tree

Medium      2.4K        33         Companies

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h
nodes inclusive at the last level h.


Example 1:          (1)
                   /    \
                (2)     (3)
               /   \    /
            (4)   (5)  (6)

Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and
{2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.


Example 2:          (1)
                   /    \
                (2)     (3)
               /   \       \
            (4)   (5)       (7)

Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 

Constraints:        The number of nodes in the tree is in the range [1, 100].
                    1 <= Node.val <= 1000
Accepted:           134.7K
Submissions:        249.6K
Acceptance Rate:    54.0%
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        q, arr = [root], []
        while q:
            level = []
            while q:
                level.append(q.pop(0))
            for node in level:
                if node:
                    arr.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else: arr.append(-1)
        while arr[-1] == -1: arr.pop()
        return -1 not in arr

def main():
    sol = Solution()
    
    m1, m2, m3, m4, m5, m6 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
    m1.left, m1.right, m2.left, m2.right, m3.left = m2, m3, m4, m5, m6
    print(sol.isCompleteTree(m1))

    n1, n2, n3, n4, n5, n7 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(7)
    n1.left, n1.right, n2.left, n2.right, n3.right = n2, n3, n4, n5, n7
    print(sol.isCompleteTree(n1))


if __name__ == "__main__":
    main()
 
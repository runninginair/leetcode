''' 114. Flatten Binary Tree to Linked List
Medium      9512      496       Add to List     Share

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer
points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:
                (1)                     (1)
              /     \                      \
            (2)     (5)         ==>        (2) 
           /   \       \                      \
        (3)    (4)     (6)                    (3)
                                                 \
                                                 (4)
                                                    \
                                                    (5)
                                                      \
                                                       (6)
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]


Constraints:    The number of nodes in the tree is in the range [0, 2000].
                -100 <= Node.val <= 100
 
Follow up: Can you flatten the tree in-place (with O(1) extra space)?

Accepted:       726,114
Submissions:    1,188,641
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                print(" # 1 -- stack_len =", len(stack), " Stack[-1] =", stack[-1].val)
            if node.left:
                stack.append(node.left)
                print(" # 2 -- stack_len =", len(stack), " Stack[-1] =", stack[-1].val)                    
            if stack:
                node.right = stack[-1]
                print(" # 3 -- stack_len =", len(stack), " Stack[-1] =", stack[-1].val)
            node.left = None

class Solution_v2:  ### Recursion Solution
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root) -> Optional[TreeNode]:
            if not root: return None
            leftTail, rightTail = dfs(root.left), dfs(root.right)
            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            last = rightTail or leftTail or root
            return last
        dfs(root)            


def printBinaryTree(root: TreeNode):
    print_helper(root, 1)

def print_helper(root: TreeNode, depth: int):
    tab = "   " * depth
    if not root:
        print(tab, "None")
        return
    print_helper(root.right, depth + 2)
    print(tab, root.val)
    print_helper(root.left, depth + 2)

def main():
    sol = Solution()
    sol = Solution_v2()

    # n1, n2, n3, n4, n5, n6 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
    # n1.left, n1.right, n2.left, n2.right, n5.right = n2, n5, n3, n4, n6
    # printBinaryTree(n1)
    # sol.flatten(n1)
    # printBinaryTree(n1)

    n11, n22, n33, n44 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(1.5)
    n22.left, n22.right, n11.right = n11, n33, n44
    printBinaryTree(n22)
    sol.flatten(n22)
    printBinaryTree(n22)

main()

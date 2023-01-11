''' 543. Diameter of Binary Tree
Easy    9900    629     Add to List     Share

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 
Constraints:    The number of nodes in the tree is in the range [1, 10^4].
                -100 <= Node.val <= 100
Accepted:       908,868
Submissions:    1,624,538
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/diameter-of-binary-tree/discuss/2678310/python-or-recursion
class Solution:
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def diameterOfBinaryTree(self, root) -> int:
        self.max_diameter = 0
        self.getDiameter(root)
        return self.max_diameter
    
    def getDiameter(self, root):
        if not root: return 0
        else: print("root =", root.val)
        
        left_depth = self.getDiameter(root.left)
        right_depth = self.getDiameter(root.right)
        # get the diameter between two nodes
        diameter = left_depth + right_depth
        print("diameter =", diameter)

        # get the maximum diameter
        self.max_diameter = max(self.max_diameter, diameter)
        print("left_depth =", left_depth, "  right_depth =", right_depth, end="\n\n")
        return max(left_depth, right_depth) + 1


def main():
    sol = Solution()
    # Input: root = [1,2,3,4,5]     Output: 3
    n1, n2, n3, n4, n5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
    n1.left, n1.right, n2.left, n2.right = n2, n3, n4, n5
    print(sol.diameterOfBinaryTree(n1))

main()

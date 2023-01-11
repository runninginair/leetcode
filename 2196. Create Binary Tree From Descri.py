''' 2196. Create Binary Tree From Descriptions
Medium

629

15

Add to List

Share
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

 

Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
Example 2:


Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
 

Constraints:

1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
The binary tree described by descriptions is valid.
Accepted
22,361
Submissions
31,034

'''


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        d = descriptions
        ## dic = {key: int TreeNode.val | parent.val: int, self: TreeNode}
        dic = {}
        for n in d:
            if n[0] not in dic:
                dic[n[0]] = [n[0], TreeNode(n[0])]
            if n[1] not in dic:
                dic[n[1]] = [n[0], TreeNode(n[1])]
            else:
                dic[n[1]][0] = n[0]
            if n[2] == 1:
                dic[n[0]][1].left = dic[n[1]][1]
            else:
                dic[n[0]][1].right = dic[n[1]][1]

        for n in d:
            if dic[n[0]][0] == dic[n[0]][1].val:
                return dic[n[0]][1]

def printBST(root: TreeNode):
    print_helper(root, 1)

def print_helper(root: TreeNode, depth: int):
    tab = "   "*depth
    if not root:
        print(tab, "None")
        return
    print_helper(root.right, depth + 1)
    print(tab, root.val)
    print_helper(root.left, depth + 1)


def main():
    sol = Solution()
    descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    n50, n20, n80, n15, n17, n19 = TreeNode(50), TreeNode(20), TreeNode(80), TreeNode(15), TreeNode(17), TreeNode(19)
    n50.left, n50.right, n20.left, n20.right, n80.left = n20, n80, n15, n17, n19
    # printBST(n50)
    printBST(sol.createBinaryTree(descriptions))


main()
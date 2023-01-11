''' 653. Two Sum IV - Input is a BST
Easy    4548    216 Add to List     Share
Given the root of a Binary Search Tree and a target number k, return true if
there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 

Constraints:    The number of nodes in the tree is in the range [1, 104].
                -10^4 <= Node.val <= 10^4
                root is guaranteed to be a valid binary search tree.
                -10^5 <= k <= 10^5
Accepted:       365,383
Submissions:    613,090

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    def findTarget(self, root, k: int) -> bool:
        lis = []
        dic = {}
        i = 0
        q = [root]
        while q:
            n = q.pop()
            lis.append(n.val)
            dic.update({n.val: i})
            i += 1
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        print(lis)
        print(dic)
        for i in range(len(lis)):
            dif = k - lis[i]
            if dif in dic and i != dic[dif]: 
                return True
        return False


class Solution_v2:
    def findTarget(self, root, k: int) -> bool:
        dic = {}
        i = 0
        # travesal the tree DFS/BFS
        stack = [root]
        while stack:
            n = stack.pop(0)
            if n.left: stack.append(n.left)
            if n.right: stack.append(n.right)
            # add node.val to a dictronary
            dic.update({n.val:i})
            i += 1
        # Iterate the dictionary to check if there exist two ele.
        print(dic)      
        for key in dic:
            dif = k - key
            if dif in dic and dic[dif] != dic[key]:
                return True
        return False
def main():
    sol = Solution_v2()
    n0, n1, n2, n3, n4, n6 = TreeNode(5), TreeNode(3), TreeNode(6), TreeNode(2), TreeNode(4), TreeNode(7)
    n0.left, n0.right = n1, n2
    n1.left, n1.right = n3, n4
    n2.right = n6

    print(sol.findTarget(n0, 9))    # Output: Ture


main()
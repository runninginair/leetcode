''' 0652. Find Duplicate Subtrees

Medium      Liked 4.1K      Disliked 346        Companies

Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.
''' 
''' Example 1:
                (1)
               /   \
            {2}     (3)
            /       /   \
         {4}       {2}   (4)
                  /
                {4}

Input: root = [1, 2, 3, 4, null, 2, 4, null, null, 4]
Output: [[2, 4], [4]]
'''
''' Example 2:
                (2)
               /   \
            {1}     {1}

Input: root = [2,1,1]
Output: [[1]]
'''
''' Example 3:
                (2)
               /   \
            {2}     {2}
           /        /
        {3}       {3}

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
''' 
''' Constraints:    The number of the nodes in the tree will be in the range [1, 5000]
                    -200 <= Node.val <= 200
    Accepted:           185.7K
    Submissions:        327K
    Acceptance Rate:    56.8%
'''

''' # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self) -> str:   ### Level traversal printout the val of the node.
        res = []
        def levelTraversal(node: Optional[TreeNode]) ->None:
            q = [node]
            if not node: return
            while q:
                level = []
                while q: level.append(q.pop(0))
                for u in level:
                    if u:
                        res.append(str(u.val))
                        q.append(u.left)
                        q.append(u.right)
                    else: res.append("null")
        levelTraversal(self)
        while len(res) > 1 and res[-1] == 'null': res.pop()
        return "[" + ", ".join(res) + "]"
        
class Solution:

    def isDuplicate(self, root1: TreeNode, root2: TreeNode) ->bool:
        if root1 and not root2: return False
        if not root1 and root2: return False
        if root1.val != root2.val: return False
        return root1.val == root2.val and self.isDuplicate(root1.left, root2.left) and self.isDuplicate(root1.right, root2.right)

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        map, res = {}, []
        def helper(root: Optional[TreeNode]) -> str:
            if not root: return ""
            left = helper(root.left)
            right = helper(root.right)
            curr = str(root.val) + "l" + left + "r" + right
            if curr in map: map[curr] += 1
            else: map[curr] = 1
            if map[curr] == 2: res.append(root)
            return curr
        helper(root)
        for r in res: print(r)
        return res

''' Official Java Solution
class Solution {
    Map<String,Integer> map=new HashMap<>();
    List<TreeNode> res=new ArrayList<>();
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        helper(root);
        return res;
    }
    public String helper(TreeNode root){
        if(root==null) return "";
        String left= helper(root.left);
        String right= helper(root.right);
        String curr= root.val +" "+left +" "+ right;
        map.put(curr, map.getOrDefault(curr, 0)+ 1);
        if(map.get(curr) == 2)
            res.add(root);
        return curr;
    }
}
'''

def main():
    ### To Test the __str__(), let's printout those three example trees,
    l0, l1, l2, l3, l4, l5, l6 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(2), TreeNode(4), TreeNode(4)
    l0.left, l0.right, l1.left, l2.left, l2.right, l4.left = l1, l2, l3, l4, l5, l6
    print(l0)

    m0, m1, m2 = TreeNode(2), TreeNode(1), TreeNode(1)
    m0.left, m0.right = m1, m2
    print(m0)
    
    n0, n1, n2, n3, n4 = TreeNode(2), TreeNode(2), TreeNode(2), TreeNode(3), TreeNode(3)
    n0.left, n0.right, n1.left, n2.left = n1, n2, n3, n4
    print(n0)

    sol = Solution()

    print(sol.findDuplicateSubtrees(l0))
    print(sol.findDuplicateSubtrees(m0))
    print(sol.findDuplicateSubtrees(n0))

if __name__ == "__main__":
    main()
